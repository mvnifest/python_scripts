import sys


import shutil

lista=[]
input_params = sys.argv
lista_jakie_usunac=[]
# origin = open("sba-tests_origin.yaml", "w")


source_path = 'sba-tests_origin.yaml'

# Path to the destination file
destination_path = 'sba-tests.yaml'

# Copy the content of the source file to the destination file
shutil.copy(source_path, destination_path)



test=[]
for i in input_params[1][16:]:

    if i == ',':
        slowo =''.join(test)
        lista.append(slowo)
        test[:]=[]
    else:
        test.append(i)
if test:
    slowo = ''.join(test)
    lista.append(slowo)

# with open("sba-tests.yaml", "r") as plik:
#     linie = plik.readlines()
#     for linia in linie:
#         origin.write(linia)

nowy=open("sba-tests.yaml", "w")
with open("sba-tests_origin.yaml", "r") as plik:
    linie = plik.readlines()
    nowy.write(linie[0])
    nowy.write(linie[1])
    for linia in linie[2:]:
        slowo = linia[7:].strip()
        if slowo in lista:
            nowy.write("#"+ linia)
        else:
            nowy.write(linia)

'''

with open("new_sba-tests.yaml", "r") as new_file, \
        open("sba-tests.yaml", "w") as source_file:
    for line in new_file:
        source_file.write(line)

'''

