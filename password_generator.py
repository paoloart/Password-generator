#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

my_letters = []
my_symbols =[]
my_numbers = []

num_of_letters = len(letters)
num_of_numbers = len(numbers)
num_of_symbols = len(symbols)

for i in range(0, nr_letters):
  x=random.randint(0,num_of_letters-1)
  my_letters.append(letters[x])

for i in range(0, nr_symbols):
  x=random.randint(0,num_of_symbols-1)
  my_symbols.append(symbols[x])


for i in range(0, nr_numbers):
  x=random.randint(0,num_of_numbers-1)
  my_numbers.append(numbers[x])

entire_list = my_letters + my_numbers + my_symbols

password=""
for i in entire_list:
  i = str(i)
  password=password+i

password2=""

list_of_numbers =random.sample(range(0,len(password)), len(password))

for i in list_of_numbers:
  password2 += password[i]

print(password2)