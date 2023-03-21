# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     temperatures = temperatures[1:]
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))  # DataFrame type
# print(data["temp"])  # Series type

# data_dict  = data.to_dict()  # converts DataFrame to dict
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# max_temp = data["temp"].max()
# print(max_temp)
#
# # Get Data in Columns
# print(data["condition"])
#
# # Get Data in Columns using attributes (Pandas can do this!)
# print(data.condition)

# # Get Data in Row
# print(data[data.temp == "Monday"])  # Get all rows where day is equal to "Monday"
#
# # Get Data in Row with highest temp
# print(data[data.temp == data.temp.max()])  # said aloud: "get data where data.temp is equal to the highest temp"

# # Get Monday's temp and convert to fahrenheit
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# print(monday_temp * 1.8 + 32)
#
# # Create a DataFrame from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# new_dataframe = pandas.DataFrame(data_dict)  # construct DataFrame from your dictionary
# new_data_csv = new_dataframe.to_csv("new_data.csv")

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")  # gets a dataframe

# Count how many grey, red, and black squirrels there are
gray_squirrel_data = squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]  # Gets dataframe
num_gray_squirrels = len(gray_squirrel_data)  # counts all rows
print(num_gray_squirrels)

black_squirrel_data = squirrel_data[squirrel_data["Primary Fur Color"] == "Black"]
num_black_squirrels = len(black_squirrel_data)
print(num_black_squirrels)

cinnamon_squirrel_data = squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"]
num_cinnamon_squirrels = len(cinnamon_squirrel_data)
print(num_cinnamon_squirrels)

new_data = {
    "Fur Color": ["gray", "cinnamon", "black"],
    "Count": [num_gray_squirrels, num_cinnamon_squirrels, num_black_squirrels]
}
new_dataframe = pandas.DataFrame(new_data)
new_squirrel_csv = new_dataframe.to_csv("squirrel_count.csv")