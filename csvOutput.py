import csv

csv_file = open('values.csv', 'a')

def func(data):
    with csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["start", "accurate", "not accurate", "epsilon", "percentage"])
        writer.writerows(data)