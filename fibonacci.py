#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.
total = 0;
previous_term = 1
current_term = 1
fib = input("Enter what term in Fibonacci sequnce you want")
for i range(fib):
  if(i == 1 || i == 2):
    print("1")
else:
  total = previous_term + current_term
  previous_term = current term
  current_term = total
  print(total)
