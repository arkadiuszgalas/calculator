def add(num1,num2):
   return num1 + num2

first_num = float(input("What's the first number?:"))
print(f"First number is {first_num}")
print("+")
print("-")
print("*")
print("/")
operation_sel = input("Pick an operation: ")
second_num = float(input("What's the next number?: "))
if operation_sel == "+":
   result = add(first_num,second_num)
   print(f"Result is: {result}")
