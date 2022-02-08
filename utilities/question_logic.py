from random import randint, shuffle
import re
from . import utilities as lf
"""
Question templates in this file:
generic_correct_order(num_choices, question_text, ascending_order, descending_order, correct_list, fillers)
"""

def raw_question_to_template_question(raw_question, placeholder_str):
    """Either way, placeholders need to be replaced as they appear...
    if raw_question is...
    - a string: assign one item as text and replace placeholder
    - a list of strings: for each item, replace placeholder, then assign each item as either text or code
    """
    template_question = []
    if type(raw_question) is str:#assume that strings will never just be pure code... I can't think why they would ever be
        template_question.append({'text':raw_question.replace('PLACEHOLDER', placeholder_str)})
    else:
        for line in raw_question:
            #replace PLACEHOLDER
            replaced_question = line.replace('PLACEHOLDER', placeholder_str)
            if replaced_question[0] != '$':
                template_question.append({'text':replaced_question})
            else:
                template_question.append({'code':replaced_question[1:]})
    return template_question

def add_item(item, indicator, items, id, used):
    """add item to items and used list
    """
    items.append({'item':item, 'indicator':indicator, 'id':f'item{id}'})
    id+=1
    used.append(item)
    return items, id, used
    
def add_possible_code_item(item, indicator, items, id, used, comment = False):
    print('adding item', id)
    items = list(items)
    if item[0] == '$':
        items.append({'code':item[1:], 'indicator':indicator, 'id':f'item{id}'})
    else:
        if comment != True:
            items.append({'item': item, 'indicator':'incorrect', 'id':f'item{id}'})
        else:
            items.append({'code':'#' + item, 'indicator':'incorrect', 'id':f'item{id}'})
    id+=1
    used.append(item)
    return items, id, used

def populate_items(incorrect, items, id, used, comment = False):
    while len(items) != 4:
        item = pick_one(incorrect)
        if item not in used:
            items = add_possible_code_item(item, 'incorrect', items, id, used, comment)   
    return items

def add_code_line(self, line, code):
    line= lf.pick_one(line)
    code+= line + '\n'
    return code

def make_items_question_from_pairs(raw_question_0, raw_question_1, pairs, fillers):
    used = []
    id = 1
    items = []
    chosen_pair = pick_one(list(pairs))
    print(chosen_pair)

    item_question_num = (0, 1) if randint(0,1) == 0 else (1, 0)#if 0,1 code goes into question, if 1,0 code is in items
    item_num, question_num = item_question_num[0], item_question_num[1]
    
    if question_num == 0:
        raw_question = raw_question_0
    else:   
        raw_question = raw_question_0 if raw_question_1 == '' else raw_question_1
    #get one correct and incorrect item
    correct_item, question_item = pick_one(chosen_pair[item_num]), pick_one(chosen_pair[question_num])
    print('correct', correct_item)
    print('question', question_item)
    list(pairs).remove(chosen_pair)
    incorrect = [item[item_num] for item in pairs] + [item[item_num] for item in fillers]

    question_template = raw_question_to_template_question(raw_question, question_item)

    comment = False
    if item_num == 0:    
        items, id, used = add_possible_code_item(correct_item, 'correct', items, id, used)
    else:
        if question_item[0] == '$':
            comment = True
            items.append({'code':'#' + correct_item, 'indicator':'correct', 'id':f'item{id}'})
        else:
            items.append({'item':correct_item, 'indicator':'correct', 'id':f'item{id}'})
        used.append(chosen_pair[item_num])
        id+= 1
    
    items, id, used = populate_items(incorrect, items, id, used, comment)
    return question_template, items

def correct_incorrect_helper(correct, incorrect):         
    id = 1
    used = []
    items = []
    correct_item = pick_one(correct)
    items, id, used = add_possible_code_item(correct_item, 'correct', items, id, used)
    items = populate_items(incorrect, items, id, used)
    return items

def make_items_question_from_correct_incorrect(raw_question, positive, negative, correct, incorrect):
    use_in_question = positive if randint(0,1) == 1 else negative
    if use_in_question == positive:
        items = correct_incorrect_helper(correct, incorrect)
        placeholder_str = positive
    else:
        items = correct_incorrect_helper(incorrect, correct)
        placeholder_str = negative
    template_question = raw_question_to_template_question(raw_question, placeholder_str)
    return template_question, items

########### dealing with code block questions. This all seems to work fine vvvvv
class Question():
    id = 1
    items = []
    used = []
    code = ''''''
    template_question = []

    def pick_one_many_times(self, item):
        while True:
            print('Inside class picking  one many times')
            if type(item) is str:
                print(item, 'is a string')
                return item
            else:
                item= item[randint(0, len(item)-1)]

    def pick_one(self, item):
        print('Inside class picking one')
        return item[randint(0, len(item)-1)]
        
    def raw_question_to_template_question(self, raw_question, placeholder_str):
        """Either way, placeholders need to be replaced as they appear...
        if raw_question is...
        - a string: assign one item as text and replace placeholder
        - a list of strings: for each item, replace placeholder, then assign each item as either text or code
        """
        if type(raw_question) is str:#assume that strings will never just be pure code... I can't think why they would ever be
            self.template_question.append({'text':raw_question.replace('PLACEHOLDER', placeholder_str)})
        else:
            for line in raw_question:
                #replace PLACEHOLDER
                replaced_question = line.replace('PLACEHOLDER', placeholder_str)
                if replaced_question[0] != '$':
                    self.template_question.append({'text':replaced_question})
                else:
                    self.template_question.append({'code':replaced_question[1:]})

    def populate_items(self, incorrect, comment = False):
        while len(self.items) != 4:
            item = pick_one(incorrect)
            print(item)
            print(self.used)
            if item not in self.used:
                self.add_possible_code_item(item, 'incorrect', comment)   
        
    def add_item(self, item, indicator):
        self.items.append({'item':item, 'indicator':indicator, 'id':f'item{self.id}'})
        self.id+=1
        self.used.append(item)
        
    def add_possible_code_item(self, item, indicator, comment = False):
        print('adding item', self.id)
        if item[0] == '$':
            self.items.append({'code':item[1:], 'indicator':indicator, 'id':f'item{self.id}'})
        else:
            if comment != True:
                self.items.append({'item': item, 'indicator':'incorrect', 'id':f'item{self.id}'})
            else:
                self.items.append({'code':'#' + item, 'indicator':'incorrect', 'id':f'item{self.id}'})
        self.id+=1
        self.used.append(item)

    def add_code_line(self, line):
        line= self.pick_one_many_times(line)
        self.code+= line + '\n'


class ErrorLines(Question):
    def __init__(self, valid, invalid):
        self.make_error_line_items_code(valid, invalid)

    def make_error_line_items_code(valid, invalid):
        """Relies on valid and invalid being the same length...
        """
        if randint(0, 1) == 0:#the code will fail...
            #pick which line will cause failure
            error_line = randint(0, len(valid)-1)
            self.items.append({'item':error_line+1, 'indicator':'correct', 'id':f'item{self.id}'})
            self.id+=1
            #pick three numbers which are not the same as error line
            if randint(0,1) == 0:#chance for statement that the code will run without error
                self.used.append('No failure')
                self.items.append({'item':'The code will execute successfully', 'indicator':'incorrect', 'id':f'item{self.id}'})
                self.id+=1
            while len(self.used) != 3:
                num = randint(0, len(valid)-1)
                if num != error_line:
                    self.used.append(num)
                    self.used = list(set(self.used))
            for num in self.used:
                if num != 'No failure':
                    self.items.append({'item': num+1, 'indicator':'incorrect', 'id':f'item{self.self.id}'})
                    self.id+=1
            #build a string with all but failing line correct
            for i in range(len(valid)):
                if i == error_line:
                    self.code+= pick_one(invalid[i]) + '\n'
                else: 
                    self.code+= pick_one(valid[i]) + '\n'
        else:#the code will actually not fail
            self.items.append({'item':'The code will execute successfully', 'indicator':'correct', 'id':f'item{self.id}'})
            self.id+=1
            while len(self.used) != 3:
                num = randint(0, len(valid)-1)
                if num not in self.used:
                    self.add_item(self, num+1, 'incorrect')
            for line in valid:
                self.add_code_line(line)

class Outcome(Question):
    def __init__(self, valid, invalid):
        self.code_outcome(valid, invalid)

    def code_outcome(self, valid, invalid):
        """items in invalid:
        (
            (('line0','outcome'),(('line0','alt line0'),'code outcome'), ....),
            ...
        )
        Each item is index[nth] line of code containing:
        [0] = either str or iterable of sample code
        [1] = code outcome of all code in [0]
        valid:
        (('sample code', ))
        [0] contains items which are each line of code
        [1] contains single string stating outcome of completed code 
        """
        #check that length of valid and invalid are the same
        if len(valid[0]) != len(invalid):
            print(f'Valid len ({len(valid[0])}) != invalid len ({len(invalid)})')
            return None
        #choose between one incorrect vs all correct
        if randint(0,3) in [0,1,2]:#one incorrect
            print('one correct')
            invalid_index = randint(0, len(valid[0])-1)#choose index of incorrect line   
            self.items.append({'item':valid[1], 'indicator':'incorrect', 'id':f'item{self.id}'})#incorrect item: code outcome successful
            self.id+=1#increment id
            correct_invalid_line_options = invalid[invalid_index]#get all entries
            correct_invalid_line = pick_one(correct_invalid_line_options)#get one entry
            self.add_possible_code_item(correct_invalid_line[1], 'correct')
            #select two other invalid outcomes NOT THE SAME AS THE correct answer
            while len(self.used)!=3:
                #select another invalid answer NOT matching index of correct_answer
                line= pick_one(invalid)#picking a line to take an error from
                if type(line) is not str:
                    attempt= pick_one(line)[1]#pick an item from the line and get the error at index[1] 
                else: 
                    attempt= line
                
                if attempt not in self.used:
                    self.add_possible_code_item(attempt, 'incorrect')

            #build code string
            for i in range(len(valid[0])):
                if i == invalid_index:
                    self.add_code_line(correct_invalid_line)
                else:
                    valid_line = valid[0][i]
                    self.add_code_line(valid_line)
        else:#all correct
            print('all correct')
            self.items.append({'item':valid[1], 'indicator':'correct', 'id':f'item{self.id}'})#use a correct answer
            self.id+=1#increment id
            #select three random unique incorrect answers
            while len(self.used)!=3:
                line_options = pick_one(invalid)#pick a line
                attempt = pick_one(line_options)[1]
                if attempt not in self.used:
                    self.add_possible_code_item(attempt, 'incorrect')
            for line in valid[0]:
                self.code+= line + '\n'


def raw_question_to_template_question(raw_question, placeholder_str):
    """Either way, placeholders need to be replaced as they appear...
    if raw_question is...
    - a string: assign one item as text and replace placeholder
    - a list of strings: for each item, replace placeholder, then assign each item as either text or code
    """
    template_question = []
    if type(raw_question) is str:#assume that strings will never just be pure code... I can't think why they would ever be
        template_question.append({'text':raw_question.replace('PLACEHOLDER', placeholder_str)})
    else:
        for line in raw_question:
            #replace PLACEHOLDER
            replaced_question = line.replace('PLACEHOLDER', placeholder_str)
            if replaced_question[0] != '$':
                template_question.append({'text':replaced_question})
            else:
                template_question.append({'code':replaced_question[1:]})
    return template_question
    
def add_item(item, indicator, items, id, used):
    items.append({'item':item, 'indicator':indicator, 'id':f'item{id}'})
    id+=1
    used.append(item)
    return items, id, used
    
def add_possible_code_item(item, indicator, items, id, used, comment = False):
    items = list(items)
    if item[0] == '$':
        items.append({'code':item[1:], 'indicator':indicator, 'id':f'item{id}'})
    else:
        if comment != True:
            items.append({'item': item, 'indicator':indicator, 'id':f'item{id}'})
        else:
            items.append({'code':'#' + item, 'indicator':indicator, 'id':f'item{id}'})
    id+=1
    used.append(item)
    return items, id, used

def populate_items(incorrect, items, id, used, comment = False):
    while len(items) != 4:
        item = lf.pick_one_many_times(incorrect)
        if item not in used:
            items, id, used = add_possible_code_item(item, 'incorrect', items, id, used, comment)   
    return items


def make_items_question_from_pairs(raw_question_0, raw_question_1, pairs, fillers):
    used = []
    id = 1
    items = []
    chosen_pair = lf.pick_one(list(pairs))
    print(chosen_pair)

    item_question_num = (0, 1) if randint(0,1) == 0 else (1, 0)#if 0,1 code goes into question, if 1,0 code is in items
    item_num, question_num = item_question_num[0], item_question_num[1]
    
    if question_num == 0:
        raw_question = raw_question_0
    else:   
        raw_question = raw_question_0 if raw_question_1 == '' else raw_question_1
    #get one correct and incorrect item
    print('item_num:', item_num, 'question_num:',question_num)
    correct_item, question_item = lf.pick_one_many_times(chosen_pair[item_num]), lf.pick_one_many_times(chosen_pair[question_num])
    print('correct', correct_item)
    print('question', question_item)
    list(pairs).remove(chosen_pair)
    incorrect = [item[item_num] for item in pairs] + [item[item_num] for item in fillers]

    question_template = raw_question_to_template_question(raw_question, question_item)

    comment = False
    if item_num == 0:    
        items, id, used = add_possible_code_item(correct_item, 'correct', items, id, used)
    else:
        if question_item[0] == '$':
            comment = True
            items.append({'code':'#' + correct_item, 'indicator':'correct', 'id':f'item{id}'})
        else:
            items.append({'item':correct_item, 'indicator':'correct', 'id':f'item{id}'})
        used.append(chosen_pair[item_num])
        id+= 1
    
    items = populate_items(incorrect, items, id, used, comment)
    return question_template, items

def correct_incorrect_helper(correct, incorrect):         
    id = 1
    used = []
    items = []
    correct_item = lf.pick_one(correct)
    items, id, used = add_possible_code_item(correct_item, 'correct', items, id, used)
    items = populate_items(incorrect, items, id, used)
    return items

def make_items_question_from_correct_incorrect(raw_question, positive, negative, correct, incorrect):
    use_in_question = positive if randint(0,1) == 1 else negative
    if use_in_question == positive:
        items = correct_incorrect_helper(correct, incorrect)
        placeholder_str = positive
    else:
        items = correct_incorrect_helper(incorrect, correct)
        placeholder_str = negative
    template_question = raw_question_to_template_question(raw_question, placeholder_str)
    return template_question, items

def add_code_line(lines, code):
    line= lf.pick_one_from_nested(lines)
    code+= line + '\n'
    return code

def make_error_line_items_code(valid, invalid):
    """Relies on valid and invalid being the same length...
    """
    items, id, used = [], 1, []
    code = ''''''

    if randint(0, 1) == 0:#the code will fail...
        print('Code will fail')
        #pick which line will cause failure
        error_line = randint(0, len(valid)-1)
        items.append({'item':error_line+1, 'indicator':'correct', 'id':f'item{id}'})
        id+=1
        #pick three numbers which are not the same as error line
        if randint(0,2) in [0,1]:#chance for statement that the code will run without error
            used.append('No failure')
            items.append({'item':'The code will execute successfully', 'indicator':'incorrect', 'id':f'item{id}'})
            id+=1
        nums = [i for i in range(len(valid))]
        used = [str(error_line+1)]
        while len(items) != 4:
            num = str(lf.pick_one(nums) +1)
            print(num, used)
            if num not in used:
                items, id, used = add_possible_code_item(num, 'incorrect', items, id, used)
        
        #build a string with all but failing line correct
        for i in range(len(valid)):
            if i == error_line:
                code+= lf.pick_one_from_nested(invalid[i]) + '\n'
            else: 
                code+= lf.pick_one_from_nested(valid[i]) + '\n'
    else:#the code will actually not fail
        print('Code will NOT fail WILL RUN')
        items.append({'item':'The code will execute successfully', 'indicator':'correct', 'id':f'item{id}'})
        id+=1
        nums = [i for i in range(len(valid))]
        shuffle(nums)    
        for num in nums[:3]:
            items, id, used  = add_item(num+1, 'incorrect', items, id, used)
        for line in valid:
            code = add_code_line(line, code)
    return items, code

def make_outcome_items_code(valid, invalid):
    items, id, used = [], 1, []
    code = ''''''
    """items in invalid:
    (
        (('line0','outcome'),(('line0','alt line0'),'code outcome'), ....),
        ...
    )
    Each item is index[nth] line of code containing:
    [0] = either str or iterable of sample code
    [1] = code outcome of all code in [0]
    valid:
    (('sample code', ))
    [0] contains items which are each line of code
    [1] contains single string stating outcome of completed code 
    """
    #check that length of valid and invalid are the same
    if len(valid[0]) != len(invalid):
        print(f'Valid len ({len(valid[0])}) != invalid len ({len(invalid)})')
        return None
    #choose between one incorrect vs all correct
    if randint(0,3) not in [0]:#3/4 chance of having question with one incorrect line
        print('one incorrect')
        invalid_index = randint(0, len(valid[0])-1)#choose index of incorrect line   
        items.append({'item':valid[1], 'indicator':'incorrect', 'id':f'item{id}'})#incorrect item: code outcome successful
        id+=1#increment id

        #finding a correct answer
        correct_invalid_item_options = invalid[invalid_index]#get all entries at that index
        correct_invalid_line, correct_invalid_outcome = lf.pick_one(correct_invalid_item_options)#get one entry from that
        #making sure the correct answer line is just one line
        correct_invalid_line = lf.pick_one(correct_invalid_line)

        items, id, used = add_possible_code_item(correct_invalid_outcome, 'correct', items, id, used)
        
        #select two other invalid outcomes NOT THE SAME AS THE correct answer
        while len(used)!=3:
            #select another invalid answer NOT matching index of correct_answer
            line= lf.pick_one(invalid)#picking a line to take an error from
            attempt= lf.pick_one(line)[1]#pick an item from the line and get the error at index[1] 
            if attempt not in used:
                items, id, used, = add_possible_code_item(attempt, 'incorrect', items, id, used)

        valid_lines = valid[0]
        print(valid_lines)
        #build code string
        for i in range(len(valid_lines)):
            if i == invalid_index:
                code = add_code_line(correct_invalid_line, code)
            else:
                valid_line = valid_lines[i]#first item in valid[i] tuple
                code = add_code_line(valid_line, code)
    else:#all correct
        print('all correct')
        items.append({'item':valid[1], 'indicator':'correct', 'id':f'item{id}'})#use a correct answer
        id+=1#increment id
        #select three random unique incorrect answers
        while len(used)!=3:
            line_options = lf.pick_one(invalid)#pick a line
            attempt = lf.pick_one(line_options)[1]
            if attempt not in used:
                items, id, used = add_possible_code_item(attempt, 'incorrect', items, id, used)
        for line in valid[0]:
            code+= line + '\n'
    return items, code

def generic_correct_order(num_choices, question_text, ascending_order, descending_order, correct_list, fillers):
    """Creates random question and item string for questions about correct order e.g.
    Question: What is the correct order to count in from lowest to highest:
    1. 1,2,3
    2. 3,2,4
    3. 1,2,9
    4. 3,2,1
    num_choices=number of choices to be in item list
    question_text = "What is the correct order to count in from PLACEHOLDER?"
    ascending_order="lowest to highest"
    descending_order="highest to lowest"
    correct_list=[1,2,3]
    fillers=[4,6,7,8]
    """
    item_id=1
    order= ascending_order if randint(0,1)==0 else descending_order
    
    question_text=re.sub('PLACEHOLDER', order, question_text)
    question=[
        {'text':question_text}
    ]
    correct_str=', '.join(correct_list) if order==ascending_order else ', '.join(correct_list[::-1])
    used=[correct_str]
    items=[{'item':correct_str, 'indicator':'correct', 'id':'item1'}]
    all_options=correct_list+fillers
    while len(used)!=num_choices:
        shuffle(all_options)
        new_str=', '.join(all_options[-len(correct_list):])
        if new_str not in used:
            used.append(new_str)
            item_id+=1
            items.append({'item':new_str, 'indicator':'incorrect', 'id':f'item{item_id}'})
    shuffle(items)
    shuffle(items)
    return question, items