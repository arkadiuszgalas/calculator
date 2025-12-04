import os
import art

def clear():
   if os.name == 'nt' or os.name == 'posix':
      os.system('clear')
   else:
      os.system('cls')

def add(num1,num2):
   return num1 + num2

def subtract(num1,num2):
   return num1 - num2

def multiply(num1,num2):
   return num1 * num2

def divide(num1,num2):
   return num1 / num2

start_new_calc = True

while start_new_calc:
   #clear()
   print(art.logo)
   first_num = float(input("What's the first number?:"))
   continue_calc_with_output = True

   while continue_calc_with_output:
      print("+")
      print("-")
      print("*")
      print("/")
      operation_sel = input("Pick an operation: ")
      second_num = float(input("What's the next number?: "))

      result = 0
      if operation_sel == "+":
         result = add(first_num,second_num)
      elif operation_sel == "-":
         result = subtract(first_num,second_num)
      elif operation_sel == '*':
         result = multiply(first_num,second_num)
      elif operation_sel == '/':
         result = divide(first_num,second_num)

      print(f"{first_num} {operation_sel} {second_num} = {result}")
      continue_calc_with_output_check = input(f"Type 'y' to continue calculating with {result}, ir type 'n' to start a new calculation:")
      if continue_calc_with_output_check.upper() == 'N':
         continue_calc_with_output = False
      else:
         continue_calc_with_output = True
         first_num = result