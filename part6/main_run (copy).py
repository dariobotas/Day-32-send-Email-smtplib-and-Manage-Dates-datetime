import datetime as dt
import smtplib as mail
import random
import pandas as pd


today = (dt.datetime.now().month, dt.datetime.now().day)

dates = pd.read_csv('part6/birthdays.csv')
dates_dict = dates.to_dict('records')

#version 1
#def todays_birthday():
#  for person in dates_dict:
#    if person['month'] == today[0] and person['day'] == today[1]:
#      return person['name']

#version 2
def todays_birthday():
  return [(person['name'], person['email']) for person in dates_dict if person['month'] == today[0] and person['day'] == today[1]]

def prepare_email_letter(name, email):
  todays_bday = todays_birthday()
  if todays_bday:
    name, email = todays_bday[0]
    message = f'Hi {name},\n\n'
    message += f'Happy birthday! Hope you have a great day!\n\n'
    message += f'Best wishes,\n\n'
    message += f'{name}\n\n'
    message += f'{email}\n\n'
    message += f'{dt.datetime.now().strftime("%d/%m/%Y")}'
    return message
  else:
    return 'No birthday today.'

def main():
  ##################### Extra Hard Starting Project ######################

  # 1. Update the birthdays.csv

  # 2. Check if today matches a birthday in the birthdays.csv

  # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

  # 4. Send the letter generated in step 3 to that person's email address.
  print(dates_dict)
  print(today)
  print(todays_birthday())
  print(random.randint(1, 3))
  print(prepare_email_letter())