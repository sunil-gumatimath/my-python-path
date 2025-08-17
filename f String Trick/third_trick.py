from datetime import datetime

# Get the current date and time
now: datetime = datetime.now()

# Format the datetime object using a custom format string
# %d: day, %m: month, %y: year (2-digit), %H: hour (24h), %M: minute, %S: second
print(f'{now:%d.%m.%y (%H:%M:%S)}')

# Format the datetime object using a locale's appropriate date and time representation
print(f'{now:%c}')

# Format the datetime object to show the hour in 12-hour format with AM/PM
# %I: hour (12h), %p: AM/PM
print(f'{now:%I%p}')
