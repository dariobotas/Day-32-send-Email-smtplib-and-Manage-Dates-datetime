import datetime as dt
import random
import smtplib as mail

MONDAY = 0
TUESDAY = 1
WEDNESDAY = 2
THURSDAY = 3
FRIDAY = 4
SATURDAY = 5
SUNDAY = 6

with open("quotes.txt") as f:
  quotes = f.readlines()
  quotes_list = [q.strip() for q in quotes]
#print(quotes_list)

def main():
  now = dt.datetime.now()
  day_of_week = now.weekday() #Monday is 0 and Sunday is 6

  #change code to send only monday
  if day_of_week == MONDAY:
    print("Today is Monday")
  else:
    quote_of_day = random.choice(quotes_list)
    with mail.SMTP("smtp.gmail.com") as connection:
      connection.starttls()
      connection.login(user='dario.botas@gmail.com', password='ubstcodixrpnzoay')
      connection.sendmail("dario.botas@gmail.com", 
                          "dbotas@getnada.com", 
                          msg=f"Subject:Monday Motivation\n\n{quote_of_day}")
    #print(quote_of_day)