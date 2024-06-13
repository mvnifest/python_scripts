import sys
import shutil

# Initialize an empty list to store the parameters
lista = []

# Path to the source and destination files
source_path = 'sba-tests.yaml'
destination_path = 'sba-tests_origin.yaml'

# Copy the content of the source file to the destination file
shutil.copy(source_path, destination_path)

# Open the source file for writing (this will erase its contents)
with open("sba-tests.yaml", "w") as help_file:
    # Open the destination file for reading
    with open("sba-tests_origin.yaml", "r") as origin_file:
        lines = origin_file.readlines()
        for line in lines:
            # Remove the leading '#' from comment lines and write them to the help file
            if line.startswith("#"):
                help_file.write(line[1:])
            else:
                help_file.write(line)

# Process the input parameters
input_params = sys.argv

# Extract the test name and the list of parameters
test_name = []
test = []
indx = -1

# Identify the index of the '#' character
for i, char in enumerate(input_params[1]):
    if char != "#":
        test_name.append(char)
    else:
        indx = i
        break

# If '#' character is found, process the parameters
if indx != -1:
    for i in input_params[1][indx+1:]:
        if i == ',':
            word = ''.join(test)
            lista.append(word)
            test = []
        else:
            test.append(i)

    if test:
        word = ''.join(test)
        lista.append("- '@" + word + "'")

# Modify the destination file based on the collected parameters
with open("sba-tests_origin.yaml", "w") as nowy:
    with open("sba-tests.yaml", "r") as plik:
        linie = plik.readlines()
        for linia in linie:
            myslnik = linia.strip()
            if myslnik and myslnik[0]=="-" and myslnik in lista:
                nowy.write("#" + linia)
            else:
                nowy.write(linia)
shutil.copy(destination_path,source_path)