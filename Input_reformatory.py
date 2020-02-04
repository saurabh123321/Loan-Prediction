import csv
file_name = input("Enter the location of file")  # this may change
input_file = open("train.csv", "r")   # directly added data file in the project folder with address C:\Users\khule\PycharmProjects\Loan-Prediction

temp_input = []
rf = input_file.read()
while rf != "":
    temp_input.append(rf)
    rf = input_file.readline()
final_input = []
for i in temp_input:
    final_input.append(i.split(","))
print(final_input)
