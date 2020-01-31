file_name = input("Enter the location of file\n")  # this may change
input_file = open(file_name, "r")
temp_input = []
rf = input_file.readline()
while rf != "":
    temp_input.append(rf)
    rf = input_file.readline()
final_input = []
for i in temp_input:
    final_input.append(i.split(","))
print(final_input)
