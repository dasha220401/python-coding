from datetime import datetime

date_input = input('Enter a date(MM DD YYYY H:M): ')
# date1 = 'Feb 12 2019 2:41PM'
# date2 = '2019-02-12 14:41:00'

obj = datetime.strptime(date_input, "%b %d %Y %I:%M%p")

print(obj)
