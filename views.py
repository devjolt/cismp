import json
import logging
from random import randint, shuffle
import re
import time

from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView

from .cismp_modules import _1, _2, _3, _4, _5, _6, _7, _8, _9
from cismp.utilities import utilities as utl
"""
logging.basicConfig(filename='cismp_question_logger.log', encoding='utf-8', level=logging.ERROR)
logging.disable(logging.INFO)
"""

cismp_logger = logging.getLogger(__name__) # custom logger

cismp_handler = logging.FileHandler('cismp_question_feedback.log') # handler
cismp_handler.setLevel(logging.ERROR)

cismp_format = logging.Formatter('%(asctime)s - %(message)s') # formatting
cismp_handler.setFormatter(cismp_format)

cismp_logger.addHandler(cismp_handler) # add formatting to handler


class HomeView(TemplateView):
    template_name = "cismp/home.html"

class RandomModuleView(TemplateView):
    modules = ()#set this in views
    template_name = 'cismp/multichoice.html'
    
    def get_context_data(self, **kwargs):
        start = time.time()
        context = super().get_context_data(**kwargs)#we're going to mess with context data, so making a context object
        module = utl.pick_one(self.modules)#select a module from the dict in that module
        print('module:',module)
        key = utl.pick_one(tuple(module.questions.keys()))#from module, get key
        print('key:',key)
        question_type = 'multi-choice'
        #uncomment for a specific question in a specific module:
        #module = _1
        #key = 'test_question'
        if type(module.questions[key]) == dict:#if that module and key contains a dict, we can use it directly to produce question and items
            question_dict = module.questions[key]#get the dict
            #try all the question types from most to least likely...correct/incorrect, pairs, pairs code, correct/incorrect code
            #print(question_dict['question'])#to see what the problem is if a question dict isn't playing ball
            if 'positive' in question_dict:
                if randint(0,1)==0:#from correct incorrect type, we can build...
                    print('standard correct incorrect')
                    template_question, items = utl.make_items_question_from_correct_incorrect(
                        question_dict['question'], 
                        question_dict['positive'],question_dict['negative'], 
                        question_dict['correct'],question_dict['incorrect']
                        )
                else:#or try...
                    try:
                        print('multi option correct incorrect')
                        template_question, items = utl.multi_option_from_correct_incorrect(question_dict)
                    except IndexError:#usually occurs on trying to pop from an empty list
                        print('back to standard correct incorrect')#go back to what works!
                        template_question, items = utl.make_items_question_from_correct_incorrect(
                            question_dict['question'], 
                            question_dict['positive'],question_dict['negative'], 
                            question_dict['correct'],question_dict['incorrect']
                            )

            elif 'question_with_0' in question_dict:
                print('Pairs')
                template_question, items = utl.make_items_question_from_pairs(
                    question_dict['question_with_0'],question_dict['question_with_1'], 
                    question_dict['pairs'], question_dict['fillers']
                    )
        else:
            print('logic type question')#self contained generating its own question and items
            template_question, items = module.questions[key]()
            #print('items:', items)
            #print('question:', question)
        
        shuffle(items)
        context['url'] = self.request.path
        context['module'] = f"{str(module)[-6]}"
        context['question'], context['items'] = template_question, items
        context['question_type'] = question_type
        context['key'] = key
        key_link = key.replace(',', '')
        context['key_link'] = key_link.replace(' ', '+').lower()
        stop = time.time()
        print('time taken:', stop-start)#interesting to know...
        return context

def test_question(request):
    module = e_files_os
    key = 'SQLite3 methods and attributes'
    #callable
    #items, question = module.questions[key]()
    context = {
        'question_type':'multi-choice',
        'items':items, 
        'question':question,
        'key':key,
        }
    return render(request, 'cismp/multichoice.html', context)

def log_problem(request):
    # post question details through
    # problem should include module, question key, question text and answer text
    # should get saved to a log
    other = request.POST.get('other')
    problem = request.POST.get('problem') if other == "" else other
    from_url = request.POST.get('url')
    module = request.POST.get('module')
    key = request.POST.get('key')
    question_type = request.POST.get('question_type')
    question = request.POST.get('question')
    
    items = request.POST.get('items')
    items = re.sub('\'', '"', items)
    items = json.loads(items)
    items_str = ''
    for item in items:
        items_str+= ('\n\t'+str(item))
        
    cismp_logger.error(f"{problem}: Module {module}, {key} ({question_type}):\n\t{question}{items_str}")
    
    return HttpResponseRedirect(from_url)
