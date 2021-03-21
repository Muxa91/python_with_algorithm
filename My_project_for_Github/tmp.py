second = 600000

year = second//31536000
second = second - year*31536000

month = second//2678400
second = second - month*2678400

week = second//604800
second = second-week*604800

day = second//86400
second = second-day*86400

hour = second//3600
second = second-hour*3600

minute = second//60
second = second-minute*60


print(year)
print(month)
print(week)
print(day)
print(hour)
print(minute)