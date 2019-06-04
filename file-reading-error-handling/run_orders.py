from function_read_write import *

# read from one file and write to another
# open a file with a function that returns a list
# save list to variable
# send list to a function

list_items = open_read_return_list('order.txt')
print(list_items)

write_to_file_multiple('order_write.txt', 'a', list_items)