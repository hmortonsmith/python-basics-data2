# here we will iterate nested lists and/or dictionaries

list_data = [1, 2, 3]
embedded_list = [[1, 2, 3], [7, 8, 9]]
dict_data = {
    1: {
        'name': 'James',
        'money': '£30,000'
        },
    2: {'name': 'Isabella',
        'money': '£301,000'
        },
    3: {'name': 'Phillip',
        'money': '£1,000'
        }
    }

for key in dict_data:
    hash = dict_data[key]
    print(hash)
    for inner_key in hash:
        print(inner_key)
        print(inner_key + ':', hash[inner_key])


# print(dict_data)
#
#
# for data in embedded_list:
#     print(data)  # data is a list
#     for embedded_data in data:
#         print(embedded_data)
