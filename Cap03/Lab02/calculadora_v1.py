# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")
opcao = input('''Selecione o número da opção desejada:
             1 - Soma
             2 - Subtração
             3 - Multiplicação
             4 - Divisão   
             Digite sua opção (1/2/3/4): ''')

if int(opcao) == 1:
    num_1 = int(input('Digite o primeiro número: '))
    num_2 = int(input('Digite o segundo número: '))
    s = num_1 + num_2
    print('Soma de {} + {} é: {}'.format(num_1, num_2, s))
elif int(opcao) == 2:
    num_1 = int(input('Digite o primeiro número: '))
    num_2 = int(input('Digite o segundo número: '))
    s = num_1 - num_2
    print('Subtração de {} + {} é: {}'.format(num_1, num_2, s))
elif int(opcao) == 3:
    num_1 = int(input('Digite o primeiro número: '))
    num_2 = int(input('Digite o segundo número: '))
    s = num_1 * num_2
    print('Multiplicação de {} + {} é: {}'.format(num_1, num_2, s))
elif int(opcao) == 4:
    num_1 = int(input('Digite o primeiro número: '))
    num_2 = int(input('Digite o segundo número: '))
    s = num_1 / num_2
    print('Divisão de {} + {} é: {}'.format(num_1, num_2, s))
else:
    print('Opção Inválida! Tente novamente.')
