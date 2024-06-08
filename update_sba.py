import sys
lista=[]
input_params = sys.argv
lista_jakie_usunac=[]
origin = open("sba-tests_origin.yaml", "w")
nowy=open("new_sba-tests.yaml", "w")


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

with open("sba-tests.yaml") as plik:
    linie = plik.readlines()
    for linia in linie:
        origin.write(linia)
with open("sba-tests.yaml") as plik:
    linie = plik.readlines()
    nowy.write(linie[0])
    nowy.write(linie[1])
    for linia in linie[2:]:
        slowo = linia[7:].strip()
        if slowo in lista:
            nowy.write("#"+ linia)
        else:
            nowy.write(linia)

