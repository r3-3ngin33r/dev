#@author: r33 - r33ngin33r@gmail.com
#@timestamp_creation: 02/18/2019 - 16:55 GMT-3

def reversed_args(f):
    def innerf(*args):
        args_list = list(args)[:100] #Convert a tuple in a list limited by one hundred elements
        for arg in args_list:
            if ( (isinstance(arg, str)) and (len(arg) > 11) ):
                args_list.remove(arg) #Remove any string parameters with length greater or equal ten       
        args = tuple(args_list)
        args = tuple(reversed(args)) #Get the reversed tuple of arguments
        return f(*args)

    return innerf

int_func_map = {
    'pow': pow,
    'cmp': lambda a, b: 0 if a == b else [1, -1][a < b],
}

string_func_map = {
    'join_with': lambda separator, *args: separator.join(args),
    'capitalize_first_and_join': lambda first, *args: ''.join([first.upper()] + list(args)),
}

def test():#ADDED
    queries = int(input())
    for _ in range(queries):
        line = input().split()
        func_name, args = line[0], line[1:]
        if func_name in int_func_map:
            args = list(map(int, args))
            print(reversed_args(int_func_map[func_name])(*args))
        else:
            print(reversed_args(string_func_map[func_name])(*args))

if __name__ == "__main__":#ADDED
    """
    queries = int(input())
    for _ in range(queries):
        print(_)
    """
    test()
