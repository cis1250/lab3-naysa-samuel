#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
while True:
  user_input = input("Enter the number of terms you'd like to see:")
  # Validate that the input is a positive integer 
  if user_input is digit(): 
     num_terms = int(user_input)
    if user_input >0:
          break
       else:
          print("Invalid input. Positive integers only.") 
    else:
        print("Invalid input. Positive integers only.")
   # Use a for loop to print the Fibonacci sequence up to that many terms.
 a = 0
 b = 1
 for i in range (num_terms): 
  print(a, end=' ')
  a = b
  b = a + b


