"""
Wow cada vez me sorprendo mas
J 
Salas
"""
# funcion


from datetime import datetime
from email import message
import string


def print_header():
    print("- " * 25)
    print("Calculo")
    print("-" * 25)

    print("[1] - Suma")
    print("[2] - Resta")
    print("[3] - Multi")
    print("[4] - Divi")
    print("[5] - Repeat message")
    print("q - Quit")


# ciclos
option = ""
while(option != "q"):
    print_header()

    option = input("Selecione uno: ")
    if option == "q":
        break

    n1 = float(input("N1: "))
    n2 = float(input("N2: "))
    if option != "5":
        n1 = float(input("N1: "))
        n2 = float(input("N2: "))
    if option == "1":
        sum = n1+n2
        print("Total: " + str(sum))
    if option == "2":
        res = n1-n2
        print("Total: " + str(res))
    if option == "3":
        multi = n1*n2
        print("Total: " + str(multi))
    if option == "4":
        if n2 == 0:
            print("Error")
        else:
            div = n1/n2
            print("Total: " + str(div))
    if option == "5":
        message = input("Ingrese un mensaje: ")
        times = int(input("Cuantas veces?"))
        time = times-1

        for i in range(time):
            print(message)

        n = 0
        while(n < times):
            print(message)
            n += 1

        print((message+"\n")*time)

    input("Presione enter para continuar")

print("Ya nos vamos a dormir")
