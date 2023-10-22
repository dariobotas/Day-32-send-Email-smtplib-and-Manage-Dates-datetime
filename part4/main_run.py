import datetime as dt

def main():
  print(dt.datetime.now())

  now = dt.datetime.now()
  year = now.year
  month = now.month
  day = now.day
  hour = now.hour
  minute = now.minute
  second = now.second

  if year == 2020:
    print(f"{year} is the current year")
    if month == 12:
      print(f"{month} is the current month")
      if day == 25:
        print(f"{day} is the current day")
        if hour == 12:
          print(f"{hour} is the current hour")
          if minute == 00:
            print(f"{minute} is the current minute")
            if second == 00:
              print(f"{second} is the current second")
              print(f"{year}-{month}-{day} {hour}:{minute}:{second}")
              print(f"{year}-{month}-{day} {hour}:{minute}:{second} is the current time")
              print(f"{year}-{month}-{day} {hour}:{minute}:{second}")