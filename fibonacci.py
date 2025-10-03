#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.
def main():
  # Usage: run this file and enter a positive integer when prompted.
  while True:
    fib = input("Enter how many terms of the Fibonacci sequence you want: ")
    if fib.isdigit() and int(fib) > 0:
      fib = int(fib)
      break
    print("Please enter a positive integer.")

  total = 0
  previous_term = 1
  current_term = 1
  # iterate terms 1..fib (range is 1-based here)
  for i in range(1, fib + 1):
    if i == 1 or i == 2:
      print(1)
    else:
      total = previous_term + current_term
      previous_term = current_term
      current_term = total
      print(total)
    