import sys
lista=[]
input_params = sys.argv
lista_jakie_usunac=[]
nowy = open("new_sba-tests.yaml", "w")

def usuwanie(lista):
    liczby = ['1', '2', '3']
    for i in lista:
        if i not in liczby:
            indeks=lista.index(i)
            lista.pop(indeks)
            usuwanie(lista)
    return(lista)


for i in input_params[1][16:]:
    lista.append(i)
for i in usuwanie(lista):
    lista_jakie_usunac.append(i)
with open("sba-tests.yaml") as plik:
    linie = plik.readlines()
    nowy.write(linie[0])
    nowy.write(linie[1])
    for linia in linie[2:]:
        logic = True
        for i in linia:
            if i in lista_jakie_usunac:
                logic = False
        if logic == True:
            nowy.write(linia)
        else:
            nowy.write("#"+linia)


