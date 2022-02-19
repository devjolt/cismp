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
        #we're going to mess with context data, so making a context object
        context = super().get_context_data(**kwargs)
        #possible modules to select from passed in from
        module = utl.pick_one(self.modules)#select a key from the dict in that module
        print(module)
        key = utl.pick_one(tuple(module.questions.keys()))#random item from list at top of module, then get from dict?
        print(key)
        #print(module)
        #print(key)
        question_type = 'multi-choice'
        #to test:
        #module = d_rest_api
        #module = e_files_os
        #key = 'sqlite_find_the_line'
        if type(module.questions[key]) == dict:#else, run standard stuff to generate question from:
            question_dict = module.questions[key]
            #try all the question types from most to least likely...
            #correct/incorrect, pairs, pairs code, correct/incorrect code
            if 'positive' in question_dict:
                #print(question_dict['question'])
                if randint(0,1)==0:
                    print('standard correct incorrect')
                    template_question, items = utl.make_items_question_from_correct_incorrect(
                        question_dict['question'], 
                        question_dict['positive'],question_dict['negative'], 
                        question_dict['correct'],question_dict['incorrect']
                        )
                else:
                    try:
                        print('multi option correct incorrect')
                        template_question, items = utl.multi_option_from_correct_incorrect(question_dict)
                    except IndexError:
                        print('back to standard correct incorrect')
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
            print('logic question')
            template_question, items = module.questions[key]()
            #print('items', items)
            #print('question', question)
        
        shuffle(items)
        context['question'], context['items'] = template_question, items
        context['question_type'] = question_type
        context['key'] = key
        key_link = key.replace(',', '')
        context['key_link'] = key_link.replace(' ', '+').lower()
        stop = time.time()
        print(stop-start)
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



