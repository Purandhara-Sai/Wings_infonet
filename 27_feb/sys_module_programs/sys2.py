import sys
#handling the index error/ number of arguments without try and except

if len(sys.argv) <2:
    print("two few arguments") #in place of print we can use sys.exit("two few arguments").
elif len(sys.argv) >2:
    print("two many argv")
else:
    print("hello ",sys.argv[1])