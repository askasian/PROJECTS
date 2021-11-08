from faker import Faker
import datetime
import numpy as np
import pandas as pd

fake = Faker()

# print(fake.date_between(start_date='today', end_date='+3y'))
# datetime.date(2025, 3, 12)

# print(fake.date_time_between(start_date='-30y', end_date='now'))
# datetime.datetime(2007, 2, 28, 11, 28, 16)

# Or if you need a more specific date boundaries, provide the start
# and end dates explicitly.


start_date = datetime.date(year=2020, month=1, day=1)
dates = []
for _ in range(20):
    fake_date = fake.date_between(start_date=start_date, end_date='+1y')
    dates.append(fake_date)

print(dates)

df1 = pd.DataFrame(np.random.randn(20, 4))
print(df1)

df1['Date'] = dates
df1.index = 'Date'
print(df1)
