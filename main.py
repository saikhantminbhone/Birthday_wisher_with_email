
import random
import smtplib
import pandas
import datetime as dt


now = dt.datetime.now()
this_month = now.month
this_day = now.day
today = (this_month,this_day)


email = "saikhantminbhoe@gmail.com"
password ="Saikhant174735"

with open("birthdays.csv") as data:
    datas = pandas.read_csv(data)
    birthday_dict = {(data_row.month,data_row.day): data_row for (index,data_row) in datas.iterrows()}


    if (this_month,this_day) in birthday_dict:
        brithday_person = birthday_dict[(this_month,this_day)]
        file_path = f"birthday_wishes/letter_{random.choice(range(1,4))}.txt"
        with open(file_path) as letter_file:
            contents = letter_file.read()
            contents=contents.replace("[NAME]",brithday_person["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()

            connection.login(user=email,password=password)
            connection.sendmail(
                from_addr=email,
                to_addrs="saikhantminbhone@gmail.com",
                msg=f"Subject:Happy Birthday \n\n {contents}")