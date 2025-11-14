class metodos():
    def __init__(self):
        pass
        
    def fibonacci(self, num1):
        
            n1 = 0
            n2 = 1
            cont = 3

            print('{}->{}'.format(n1,n2), end="")

            while cont <= num1:
                n3 = n1 + n2
                print('->{}'.format(n3), end="")
                n1 = n2
                n2 = n3
                cont += 1
            print('FIM')

    def numPar(self, num2):
        self.n = num2

        if num2 % 2 == 0:
            print('{} é par'.format(num2))
        
        else:
            print('{} é ímpar'.format(num2))


    def Potencia(self, base, exp):
        
        result = base ** exp
        print('A potencia do {} é:'.format(base), result)


    def numPrimo(self, num4):
        
        if num4 % 2 == 0:
            print('{} não é primo'.format(num4))
        
        else:
            print('{} é primo'.format(num4))


obj = metodos()

num1 = int(input("Escreva a quantidade de caracteres dessa Sequencia de Fibonacci: "))
print('-'*10)
obj.fibonacci(num1)

num2 = int(input("Escreva o número para verificar se é par: "))
obj.numPar(num2)
print('-'*10)

base = int(input("Escreva o número: "))
potencia = int(input("Escreva a potencia para o número: "))
obj.Potencia(base, potencia)
print('-'*10)

num4 = int(input("Escreva o número para verificar se é primo: "))
obj.numPrimo(num4)