# with open("weather_data.csv") as csv_file:
#     data = csv_file.readlines()
#     print(data)


# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     # print(data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

#     print(temperatures)


import pandas

data = pandas.read_csv("weather_data.csv")
# print(data["temp"])


temp_list = data["temp"].to_list()

# result = sum(temp_list) / len(temp_list)

# result = data["temp"].mean()

result = data["temp"].max()

print(result)


print(data[data.temp == data.temp.max()])
