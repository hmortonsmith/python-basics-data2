# open and print line by line
def open_print_line_by_line(file_name):
    try:
        with open(file_name, 'r') as file:
            for line in file.readlines():
                print(line.rstrip('\n'))
    except FileNotFoundError as error_message:
        print('No file found')
    finally:
        print('All done')


# returns all the lines as a list
def open_read_return_list(file_name):
    try:
        with open(file_name, 'r') as file:
            return file.readlines()
    except FileNotFoundError as error_message:
        print('file not found')
        print(error_message)


#  write to file
def write_to_file(file_name, option, item):
    try:
        # with #action file as #placeholder
        with open(file_name, option) as file:
            file.write(item + '\n')
    except FileNotFoundError as error_message:
        print('Please check file exists')
        print(error_message)
    finally:
        print('Execution done')
# write_to_file('order_write.txt', 'a', 'potato salad')


# write multiple to file
def write_to_file_multiple(file_name, option, list):
    try:
        # with #action file as #placeholder
        with open(file_name, option) as file:
            for item in list:
                file.write(item)
    except FileNotFoundError as error_message:
        print('Please check file exists')
        print(error_message)
    finally:
        print('Execution done')
# write_to_file_multiple('order_write.txt', 'a', ['potato salad', 'steak', 'fries'])

