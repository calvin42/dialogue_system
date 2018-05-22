from inspect import stack

def get_caller_func():
    return stack()[2][3]

def print_log(string):
    line = "#########################"
    print(line)
    print((get_caller_func()))
    print (string)
    print(line)
