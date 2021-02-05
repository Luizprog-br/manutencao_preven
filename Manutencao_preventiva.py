from os import popen as p
from shutil import rmtree as r
from time import sleep as s

opc = ['Defragmentação', 'Drivers', 'Arquivos Temporarios']


while True:
    try:
        print(f'1 {opc[0]}\n2 {opc[1]}\n3 {opc[2]}\n')
        resp = int(input('Digite uma opção(0 para encerrar o programa):'))
        if resp == 1:
            print('Opção um Digitada')
            s(1)
            print('Abrindo o Programa...\n')
            s(2)
            p('SmartDefragPortable.exe')
        elif resp == 2:
            print('Opção dois Digitada')
            s(1)
            print('Abrindo o Programa...\n')
            s(2)
            p('DriverEasyPortable.exe')
        elif resp == 3:
            print('Opção três Digitada')
            s(1)
            print('Excluindo Pasta...\n')
            s(2)
            r('C:\\Windows\\Temp', ignore_errors=True)
        elif resp == 0:
            print('Encerrando o Programa.')
            s(2)
            input('Programa Finalizado')
            break
        else: 
            print('Valor digitado invalido !\n')
    except ValueError:
        print('Valor digitado invalido !\n')
