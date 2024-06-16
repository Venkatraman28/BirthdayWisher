import smtplib
import random
import pandas as pd
import datetime as dt

MY_EMAIL = ""
PASSWORD = ""
BIRTHDAY_CSV = "birthdays.csv"
CONTENT_TO_REPLACE = "[NAME]"


def main():
    now = dt.datetime.now()
    day = now.day
    month = now.month

    df = pd.read_csv(BIRTHDAY_CSV)
    target_rows = df[(df['day'] == day) & (df['month'] == month)]
    result = target_rows[['name', 'email']].to_dict(orient="records")

    for r in result:
        name = r['name']
        email = r['email']

        pick_letter_number = random.randint(1, 3)
        with open(f'letter_templates/letter_{pick_letter_number}.txt', 'r') as read_file:
            read_letter = read_file.read()

        personalized_content = read_letter.replace(CONTENT_TO_REPLACE, name)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email,
                msg=f"Subject:Happy Birthday!\n\n{personalized_content}"
            )


if __name__ == "__main__":
    main()
