import sys

#handling the indexerror
try :
    print("hello , my name is",sys.argv[1]) #if no argument is passed to command line generally it raises the error. : index out of range
except IndexError:
    print("please provide command line argments")