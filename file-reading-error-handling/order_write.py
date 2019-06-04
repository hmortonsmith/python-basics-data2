# same logic
# define function that takes a file to write on
# also takes an item to write into a file

# open the file with the write option
# write our amazing item into the file
# handle for errors


# def write_to_file(file_name, option, item):
#
#     try:
#         # with #action file as #placeholder
#         with open(file_name, option) as file:
#             file.write(item + '\n')
#
#     except FileNotFoundError as error_message:
#         print('Please check file exists')
#         print(error_message)
#     finally:
#         print('Execution done')
#
#
# write_to_file('order_write2.txt', 'a', 'spicy rice')

def write_to_file(file_name, option, list):

    try:
        # with #action file as #placeholder
        with open(file_name, option) as file:
            for item in list:
                file.write(item + '\n')

    except FileNotFoundError as error_message:
        print('Please check file exists')
        print(error_message)
    finally:
        print('Execution done')


write_to_file('order_write.txt', 'a', ['potato salad', 'steak', 'fries'])

