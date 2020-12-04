#import a module and change the value
import module1
module1.lst[1]=53
print(module1.lst)
print('\n')


#to fetch a random number from the module
import rand #rand is a module
print(rand.randno()) #randno is function in rand to fetch the random number
print('\n')


#import sys and find the python path
import sys
print(sys.path)
