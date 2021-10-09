# Pipelines - Broadcasting

import csv

def data_reader(f_name):
    f = open(f_name)

    try:
        dialect = csv.Sniffer().sniff(f.read(2000))
        f.seek(0)
        reader = csv.reader(f,dialect=dialect)
        yield from reader
    finally:
        f.close()

file_name = './car_data.csv'
# for row in data_reader(file_name):
#     print(row)


idx_make = 0
idx_model = 1
idx_year = 2
idx_vin = 3
idx_color = 4

headers = ('make', 'model', 'year', 'vin', 'color')
converters = (str, str, int, str, str)

def data_parser():
    data = data_reader(file_name)
    next(data)

    for row in data:
        parsed_data = [converter(item) for converter, item in zip(converters, row)]
        yield parsed_data

data = data_parser()
for _ in range(5):
    print(next(data))

