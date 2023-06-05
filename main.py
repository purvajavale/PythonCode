# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from array import array


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# When a Python interpreter reads a Python file, it first sets a few special variables.
# Then it executes the code from the file.
# One of those variables is called __name__.

# Python files are called modules, they are identified by the .py file extension.
# A module can define functions, classes, and variables.
# So when the interpreter runs a module,
# the __name__ variable will be set as  __main__ if the module that is being run is the main program.
# But if the code is importing the module from another module,
# then the __name__  variable will be set to that module’s name.

# File two __name__ is set to: file_two
# File one __name__ is set to: __main__
if __name__ == '__main__':
    print_hi('PyCharm')


def print_num():
    num_add = 2 + 3
    num_div = 2 / 3
    num_divide = 2 // 3
    print(f'Add : {num_add}', f'Decimal : {num_div}', f'Without Decimal : {num_divide}')


if __name__ == '__main__':
    print_num()


def print_swap():
    a = 6
    b = 5
    print(a, b)
    temp = a
    a = b
    b = temp
    print(f'Swap 1 : {a, b}')

    # Without 3rd variable
    a = 6
    b = 5
    print(a, b)
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print(f'Swap 2 : {a, b}')

    # Without 3rd variable
    a = 6
    b = 5
    print(a, b)
    a = a + b
    b = a - b
    a = a - b
    print(f'Swap 3 : {a, b}')


if __name__ == '__main__':
    print_swap()


def print_menu_driven():
    x = int(input('Enter 1st number : '))
    y = int(input('Enter 2nd number : '))
    z = x + y

    if z == 0:
        print(f'Output is 0')
    elif z == -1:
        print(f'Output is -1')
    else:
        print(f'Output : {z}')
        print(f'Output id : {id(z)}')
        print(f'Output type : {type(z)}')


if __name__ == '__main__':
    print_menu_driven()


def print_while():
    i = 1
    while i <= 5:
        print('Purvey')
        i = i + 1


if __name__ == '__main__':
    print_while()


def print_for():
    q = ['pj', 3, 1]
    for i in q:
        print(i)


if __name__ == '__main__':
    print_for()


def print_prime():
    num = 10

    for i in range(2, num):
        if num % 2 == 0:
            print(f'Prime number')
            break
        else:
            print(f'Not a Prime Number')


if __name__ == '__main__':
    print_prime()


def print_array():
    vals = array('u', ['a', 'e', 'i'])
    for e in vals:
        print(e)
# u - unicode
# i - int
# f - float


if __name__ == '__main__':
    print_array()
