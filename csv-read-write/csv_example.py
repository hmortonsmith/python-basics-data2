
import csv
# here we load CSV
# open the file
# read line by line


# with open('user_details.csv', newline='') as csv_file:
#     csvreader = csv.reader(csv_file, delimiter=',')
#     for row in csvreader:
#         print(row[-1])


# # iter allows you to skip over headers
# # next() to go to next line
# with open('user_details.csv', newline='') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     iterable = iter(csv_reader)
#     # for row in csv_reader:
#     #     print(row[-1];
#     print(iterable)
#     headers = next(iterable)
#     for row in iterable:
#         print(row)


# list()
with open('user_details.csv', newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    list_list = list(csv_reader)
    print(type(list_list))
    print(len(list_list))
    for row in list_list:
        print(row)


# Transforming and writing to csv


