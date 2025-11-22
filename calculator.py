def add(num1,num2):
   return num1 + num2

def subtract(num1,num2):
   return num1 - num2

def multiply(num1,num2):
   return num1 * num2

def divide(num1,num2):
   return num1 / num2

first_num = float(input("What's the first number?:"))
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
