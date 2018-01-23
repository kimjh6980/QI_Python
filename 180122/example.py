'''
#---------------------------------------------------------
def my_func(first_arg, second_arg):
	print "first_arg:", first_arg
	print "second_arg:", second_arg
	
my_func(3, 5);

#---------------------------------------------------------
def my_func(**kwargs):
	# A Function that shows how powerful **kwargs is
	# please feet free to put whatever you like
	print "first_arg:", kwargs.get('first_arg', -1)
	print "second_arg:", kwargs.get('second_arg', -2)
	print "third_arg:", kwargs.get('third_arg', -3)
	print "fourth_arg:", kwargs.get('fourth_arg', -4)
	
help(my_func)

my_func(first_arg=['a','b','c'], second_arg={'x':1,'y':2,'z':3})

#---------------------------------------------------------
def my_func(**kwargs):
	# A Function that shows how powerful **kwargs is
	# please feet free to put whatever you like
	first_arg = kwargs.get('first_arg', -1)
	if isinstance(first_arg, list):
		print "first_arg is a list"
		
	print "first_arg:", kwargs.get('first_arg', -1)
	print "second_arg:", kwargs.get('second_arg', -2)
	print "third_arg:", kwargs.get('third_arg', -3)
	print "fourth_arg:", kwargs.get('fourth_arg', -4)

help(my_func)

my_func(first_arg=['a', 'b', 'c'], second_arg={'x': 1, 'y': 2, 'z': 3})

#---------------------------------------------------------
def my_func(**kwargs):
	# A Function that shows how powerful **kwargs is
	# please feet free to put whatever you like
	first_arg = kwargs.get('first_arg', -1)
	if isinstance(first_arg, list):
		print "first_arg is a list"
	
	print "first_arg:", kwargs.get('first_arg', -1)
	print "second_arg:", kwargs.get('second_arg', -2)
	print "third_arg:", kwargs.get('third_arg', -3)
	print "fourth_arg:", kwargs.get('fourth_arg', -4)


help(my_func)

my_func(first_arg=['a', 'b', 'c'], second_arg={'x': 1, 'y': 2, 'z': 3})
'''
#---------------------------------------------------------
from pdb import help


def my_func(o, **kwargs):
	# A Function that shows how powerful **kwargs is
	# please feet free to put whatever you like
	first_arg = kwargs.get('first_arg', -1)
	
	print "first_arg:", kwargs.get('first_arg', -1)
	print "second_arg:", kwargs.get('second_arg', -2)
	print "third_arg:", kwargs.get('third_arg', -3)
	print "fourth_arg:", kwargs.get('fourth_arg', -4)

	for i in xrange(101, 0, -3):
		print i
	pass

	help(my_func())
	my_func(first_arg['a', 'b', 'c'], second_arg={'x': 1, 'y': 2, 'z': 3})