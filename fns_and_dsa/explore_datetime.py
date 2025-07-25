from datetime import datetime, timedelta


def display_current_datetime():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print('Current date and time: ', current_date)


display_current_datetime()


def calculate_future_date():
    current_date = datetime.now()
    days_to_add = int(input(
        'Enter the number of days to add to the current date: '))
    future_date = current_date + timedelta(days=days_to_add)
    formateddate = future_date.strftime("%Y-%m-%d")
    print('Future date: ', formateddate)


calculate_future_date()
