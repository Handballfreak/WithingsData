import csv
import datetime

#creating a csv file for aggregates_distance to test the Visualization
with open("distance_test_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(['date', 'value'])

    dt = datetime.datetime(2019, 1, 1)
    end = datetime.datetime(2020, 8, 4)
    step = datetime.timedelta(days=1)

    distance = 0

    while dt < end:
        distance = distance + 1
        writer.writerow([dt.strftime('%Y-%m-%d'), distance])
        dt += step