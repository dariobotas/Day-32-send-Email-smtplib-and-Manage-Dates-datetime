import datetime as dt
import smtplib as mail
import random
import pandas as pd

USER_MAIL = 'dario.botas@gmail.com'
PASS ='ubstcodixrpnzoay'

today = (dt.datetime.now().month, dt.datetime.now().day)

data = pd.read_csv("part7/birthdays.csv")
birthdays_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}

def main():

  if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_{random.randint(1,4)}.txt"
    with open(file_path, 'r') as file:
      contents = file.read()
      contents = contents.replace('[NAME]', birthday_person['name'])
      
    with mail.SMTP('smtp.gmail.com', 587) as connection:
      connection.starttls()
      connection.login(user=USER_MAIL, password=PASS)
      connection.sendmail(from_addr=USER_MAIL, 
                          to_addrs=birthday_person['email'], 
                          msg=f"Subject:Happy Birthday!\n\n{contents}")
    print(f"{birthday_person['name']}'s birthday is today. Happy Birthday!")