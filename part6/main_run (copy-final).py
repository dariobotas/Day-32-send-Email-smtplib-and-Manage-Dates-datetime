import datetime as dt
import smtplib as mail
import random
import pandas as pd

USER_MAIL = 'dario.botas@gmail.com'
PASS ='ubstcodixrpnzoay'

today = (dt.datetime.now().month, dt.datetime.now().day)

dates = pd.read_csv('part6/birthdays.csv')
dates_dict = dates.to_dict('records')

def todays_birthday():
  return [(person['name'], person['email']) for person in dates_dict if person['month'] == today[0] and person['day'] == today[1]]

def prepare_email_letter(name_mail):
  """Based on name, return the tuple subject and email body that were random select from the letter_1, letter_2, letter_3, letter_4 that have the text and need to replace the place holder [NAME] for the name on the input"""
  letter_selected = random.randint(1, 4)
  name = name_mail[0]
  email = name_mail[1]
  with open(f"part6/letter_{letter_selected}.txt") as f:
    letter_text = f.read()
    letter_text = letter_text.replace("[NAME]", name)
  return (email,f"Happy Birthday {name}!", letter_text)

def main():
  ##################### Extra Hard Starting Project ######################

  # 1. Update the birthdays.csv

  # 2. Check if today matches a birthday in the birthdays.csv

  # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

  # 4. Send the letter generated in step 3 to that person's email address.
  #print(dates_dict)
  #print(today)
  #print(todays_birthday())
  #print(random.randint(1, 3))
  #print(prepare_email_letter("Dario"))
  birthday_people = todays_birthday()
  letters_birthday = [prepare_email_letter(person) for person in birthday_people]
  print(letters_birthday)
  for letter in letters_birthday:
    #print(letter[0]+ f"\nSubject: {letter[1]}\n\n{letter[2]}")
    #print()
    with mail.SMTP("smtp.gmail.com", 587) as connection:
      connection.starttls()
      connection.login(user=USER_MAIL, password=PASS)
      connection.sendmail(from_addr=USER_MAIL, to_addrs=letter[0], msg=f"Subject: {letter[1]}\n\n{letter[2]}")