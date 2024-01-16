import sys

try:
  x = int(input("x: "))
  y = int(input("y: "))
except ValueError:
  print("Error: Invalid input.")
  sys.exit(1)

try:
  result = x/y
except ZeroDivisionError:
  print("Error:Can not divide by 0,are you idot?")
  sys.exit(1)

print(f"{x}/{y} = {result}")
