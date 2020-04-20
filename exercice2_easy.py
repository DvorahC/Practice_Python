"""
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.
Extras:
Add: asking the user for another number and printing out that many copies of the previous message.
 (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines.
 (Hint: the string "\n is the same as pressing the ENTER button)
"""
name = input('What is your name? ')
age = int(input('How old are you? '))
print(f'Hello {name}, in {(100 - age)+ 2014} you will be 100 years old!')
new_number = int(input('Enter a second number please: '))
for n in range(0, new_number):
    print('WHAOU \n')