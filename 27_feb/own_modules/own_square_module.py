x = int(input("enter x value: "))
def main():
    square(x)
    message()
def square(x):
    return x*x
def message():
      print("sample message")

"""
The if __name__ == "__main__": 
block ensures that main() is called only when the script is executed directly,
not when it's imported as a module into another script.
"""

#with  if __name__ == "__main__": 
#output
"""
enter x value: 8
4
"""
#without if __name__ == "__main__": 
#output
"""
enter x value: 3
sample message
4
"""
if __name__ == "__main__":
 # if we dont use this line while importing the own_square_module ,, the two methods will be called instead of square().
    main()