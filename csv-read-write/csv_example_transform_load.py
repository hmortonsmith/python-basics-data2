import csv


# get data and remove gender and title
# return transformed data
def transform_user_details(csv_full_name):
    new_user_data = []

    with open('user_details.csv', newline='') as csv_file:
        user_details_csv = csv.reader(csv_file, delimiter=',')

        for row_list in user_details_csv:
            transformed_row = []
            transformed_row.append(row_list[1].capitalize())
            transformed_row.append(row_list[2].capitalize())
            transformed_row.append(row_list[4])
            # strip it
            # capitalize
            # concatenate
            new_user_data.append(transformed_row)
        return new_user_data


new_transformed_data = transform_user_details('user_details.csv')

# let's create a function to write our transformed data
# write to csv


def create_new_csv_user_data(transformed_data, new_user_file_name):
    # have our transformed data
    # open a new file - use option to write
    new_file = open(new_user_file_name, 'w', newline='')
    # write to that file
    with new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerows(transformed_data)


print(new_transformed_data)
create_new_csv_user_data(new_transformed_data, 'transformed_csv.csv')
