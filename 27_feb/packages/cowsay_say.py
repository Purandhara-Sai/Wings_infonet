import cowsay
import sys

if len(sys.argv) == 2:
    #print the cow image 
    cowsay.cow("hello " + sys.argv[1])