"""
F-String DateTime Formatting

This script demonstrates how to use f-strings to format datetime objects.
F-strings can format datetime objects using format codes similar to strftime().

Common format codes:
- %d: Day of month (01-31)
- %m: Month (01-12)
- %y: Year (2-digit), %Y: Year (4-digit)
- %H: Hour (24-hour, 00-23)
- %I: Hour (12-hour, 01-12)
- %M: Minute (00-59)
- %S: Second (00-59)
- %p: AM or PM
- %c: Locale's appropriate date and time
"""

from datetime import datetime

# Get the current date and time
now: datetime = datetime.now()

print("F-String DateTime Formatting Examples")
print("=" * 40)
print(f"Current datetime object: {now}")
print()

# Format the datetime object using a custom format string
# %d: day, %m: month, %y: year (2-digit), %H: hour (24h), %M: minute, %S: second
print(f"Custom format (DD.MM.YY HH:MM:SS): '{now:%d.%m.%y (%H:%M:%S)}'")

# Format the datetime object using a locale's appropriate date and time representation
print(f"Locale format: '{now:%c}'")

# Format the datetime object to show the hour in 12-hour format with AM/PM
# %I: hour (12h), %p: AM/PM
print(f"12-hour format: '{now:%I%p}'")

print()
print("Common datetime format codes:")
print("%d - Day (01-31)")
print("%m - Month (01-12)")
print("%y - Year (2-digit), %Y - Year (4-digit)")
print("%H - Hour (24-hour), %I - Hour (12-hour)")
print("%M - Minute, %S - Second")
print("%p - AM/PM")
print("%c - Full locale date and time")
print("%x - Locale date, %X - Locale time")

# Additional formatting examples
print(f"\nMore examples:")
print(f"Date only: {now:%x}")
print(f"Time only: {now:%X}")
print(f"ISO format: {now:%Y-%m-%d %H:%M:%S}")
print(f"US format: {now:%m/%d/%Y}")
print(f"European format: {now:%d/%m/%Y}")

print(f"\nPractical applications:")
print("- Logging with timestamps")
print("- User-friendly date displays")
print("- File naming with dates")
print("- International date formatting")
