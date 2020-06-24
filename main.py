import re

def get_string():
  string = input('Enter a string:')
  if string == string[::-1]:
    print('The string is a palindrome')
  else:
    print('Try again, the string is not a palidrome')


def get_number():
  number = input('Enter your age:')
  if number == number[::-1]:
    print('You are a palindrome!')
  else:
    print('You are not a palindrome')

def get_school():
    School = input('Enter the school you attended:')
    cleaned_phrase = re.sub(r'[^A-Za-z]','', school.lower())
  if school == school[::-1]:
    print('Your school is a palindrome')
  else:
    print('Your school is not a palindrome')

def get_tests():
  get_string()
  get_number()
  get_school()

get_tests()
