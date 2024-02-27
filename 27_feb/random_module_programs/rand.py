import random

coin = random.choice(["head","tail"])
print("probability of head and tail")
print(coin)
print("\n")

#printing random number in between  1 to 10.
number = random.randint(1,10)
print("getting a random number from 1 to 10")
print(number)
print("\n")
#shuffle the list

l=[1,2,3,4,5,6]
print(l)
print("shuffling the above list")
random.shuffle(l)
for i in l:
  print(i)
