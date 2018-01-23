def my_func(**kwargs):
    """A function that shows how powerful '**kwargs' is.
       Please feel free to Put whatever you like."""
    first_arg = kwargs.get('first_arg', -1)
    if type(first_arg) == list:
        print ("first_arg is a list")
    else:
        print ("first_arg is not a list")
    print ("first arg: !", kwargs.get('first_arg', -1))
    print("second arg: !", kwargs.get('second_arg', -2))
    print("third arg: !", kwargs.get('third_arg',-3))
    print("Fourth_arg: ", kwargs.get('fourth_arg', -4))

help(my_func) # The help function

my_func(first_arg = ['a', 'b', 'c'],
        second_arg={'x' : 1, 'y' : 2, 'z' : 3})