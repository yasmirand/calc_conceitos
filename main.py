'''
* Autor: Yasmin Miranda
* Linguagem: Python
* Data: 2024.12.29
* Descrição: uma calculadora de conceitos
* Funcionalidades: calcula a nota do aluno em conceitos
'''

def linha_50():
    print("**************************************************")

def OP():
    print("Digite:\n1 - se você quer ser otimista\n2 - se você quer ser pessimista")
    linha_50()
    n = int(input("-> "))
    linha_50()
    if n == 1:
        A = 10
        B = 8
        C = 6
    elif n == 2:
        A = 10
        B = 8
        C = 6
    return A, B, C

def notaFinal():
    notaa = 0
    A, B, C = OP()
    for i in range (4):
        nota = input(f"digite o {i+1}º conceito: ")
        if (nota == "A" or "a"):
            notaa += A
        elif (nota == "B" or "b"):
            notaa += B
        elif (nota == "C" or "c"):
            notaa =+ C
    conceito = notaa/4
    return conceito

def notaBimestre():
    notaa = 0
    n = int(input("digite quantas notas você tem: "))
    linha_50()
    A, B, C = OP()
    for i in range (n):
        nota = input(f"digite o {i+1}º conceito: ")
        if (nota == "A" or "a"):
            notaa += A
        elif (nota == "B" or "b"):
            notaa += B
        elif (nota == "C" or "c"):
            notaa =+ C
    conceito = notaa/n
    return conceito

def main():
    linha_50()
    print("Digite:\n1 - Nota do bimestre\n2 - Nota final\n3 - Sair")
    linha_50()
    n = int(input("-> "))
    linha_50()
    if(n == 1):
        conceito = notaBimestre() 
    elif(n == 2):
        conceito = notaFinal()
    return conceito 
   

conceito = main()
linha_50()
if conceito >= 9:
    print("Seu conceito provavelmente será A")
elif conceito >= 7:
    print("Seu conceito provavelmente será B")
elif conceito >= 5:
    print("Seu conceito provavelmente será C")
else:
    print("Seu conceito provavelmente será D")
linha_50()