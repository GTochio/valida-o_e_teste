import sys
while True:
    try:
        num = int(input('Digite um numero inteiro : '))
        if(num < 0):
            num = num *-1
        break
    except ValueError:
        print('Você não digitou um número inteiro :')


primo = True
cont = 1
if(num <= 1):
    print("Não é primo")
    sys.exit()
for i in range(2,num):
            if (num%i==0):
                cont = cont + 1
            if (cont > 1):
                print("Não é Primo")
                sys.exit()

print("É Primo")
