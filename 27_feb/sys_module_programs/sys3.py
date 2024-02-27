import sys
#taking multiple arguments
if len(sys.argv)< 2:
    sys.exit("no arguments provided")
for arg in sys.argv:# executing this takes the file name also as an argument to avoid this use the following code below
    print("hello",arg)

print("\n")
print("avoiding the file name as an argument")

#like slicing.
for args in sys.argv[1:]:
    print("hello",args)