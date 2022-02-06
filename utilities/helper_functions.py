from random import randint


def pick_one_many_times(item):
    while True:
        print('Outside class picking one many times')
        print('item:',item)
        if type(item) not in [tuple, list]:
            print(item, 'is a string')
            return item
        else:
            item=item[randint(0, len(item)-1)]

def pick_one(item):
    item = item[randint(0, len(item)-1)]
    return item