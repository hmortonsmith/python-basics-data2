# Opening files and error handling
# We will use:
# open
# try
# except
# with
# finally

# try:
#     file = open("order.txt")
#     # do another thing
#     # this is a block of code
# except:
#     print('THERE HAS BEEN AN ERROR! \n\nPANIC NOW!')

# try:
#     file = open("order.txt")
#     # do another thing
#     # this is a block of code
# except FileNotFoundError:
#     print('File not found \nPlease check the name\n(Do not panic)')


# try:
#     file = open("order.txt", 'r')
#     file_list_lines = file.readlines()
#
#     for line in file_list_lines:
#         print(line.rstrip('\n'))
#     # do another thing
#     # this is a block of code
#     #file.close
# except FileNotFoundError as error_message:
#     print('File not found \nPlease check the name\n(Do not panic)')
#     print(error_message)

# try:
#     with open('order.txt', 'r') as file:
#         for line in file.readlines():
#             print(line.rstrip('\n'))
# except FileNotFoundError as error_message:
#     print('no file found')
# finally:
#     print('All done')

def open_print_line_by_line(file_name):
    try:
        with open(file_name, 'r') as file:
            for line in file.readlines():
                print(line.rstrip('\n'))
    except FileNotFoundError as error_message:
        print('No file found')
    finally:
        print('All done')


open_print_line_by_line('order.txt')

open_print_line_by_line('drinks.txt')















