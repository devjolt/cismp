from django.views.generic.base import TemplateView
from django.shortcuts import render
from random import randint, shuffle

import time

from .cismp_modules import _1, _3, _4#, _2, _3
from cismp.utilities import utilities as utl

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



