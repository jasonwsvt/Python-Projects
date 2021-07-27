mySentence = 'list of colors'
color_list = ['red', 'blue', 'green', 'orange', 'yellow', 'purple']

def color_function(name):
    lst = []
    for i in color_list:
        lst.append("{} {} {}".format(name, mySentence, i))
    return lst

for i in color_function('Jason'):
    print(i)

lst = [1, 2, 5, 4, 3]
lst.sort()
print(lst)

def get_name():
    go = True
    while go:
        name = input('What is your name? ')
        if name == '':
            print('You need to provide your name.')
        elif name == 'Sally':
            print('Sally, you may not use this software.')
        else:
            print('Welcome, {}.'.format(name))

get_name()
