import smtplib


def main():
  #connection = smtplib.SMTP('smtp.gmail.com', 587)
  #connection.starttls()
  #connection.login(user='dario.botas@gmail.com', password='ubstcodixrpnzoay')
  #connection.sendmail(from_addr='dario.botas@gmail.com', to_addrs='botasdario@gmail.com', msg="Subject:Hello\n\nThis is the body of my email.")
  #connection.close()

  with smtplib.SMTP('smtp.gmail.com', 587) as connection:
    connection.stsrttls()
    connection.login(user='dario.botas@gmail.com', password='ubstcodixrpnzoay')
    connection.sendmail(
      from_addr='dario.botas@gmail.com', 
      to_addrs='botasdario@gmail.com', 
      msg="Subject:Hello\n\nThis is the body of my email.")