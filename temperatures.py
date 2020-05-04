import datetime

temperatures = {
    datetime.date.today(): 20,
    datetime.date.today() - datetime.timedelta(days=1): 15,
    datetime.date.today() - datetime.timedelta(days=2): 12,
    datetime.date.today() - datetime.timedelta(days=3): 9,
    datetime.date.today() - datetime.timedelta(days=4): 7,
    datetime.date.today() - datetime.timedelta(days=5): 19,
    datetime.date.today() - datetime.timedelta(days=6): 21,
}

s = input('enter a date (yyyy-mm-dd): ')
date = datetime.datetime.strptime(s, '%Y-%m-%d').date()
temperature = temperatures.get(date)

if not temperature:
    print(f'Temperature was not recorded on {s}')
    exit(0)

print(f'The temperature on {s} was {temperature} degrees Celcius')
exit(0)
