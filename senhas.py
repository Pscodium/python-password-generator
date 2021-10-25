import random
import time
from os import system
print('\nOlá, qual é seu nome?')
nome = input('Resposta: ')
time.sleep(2)
print('HMMM..., ok')
time.sleep(2)
system('cls')

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
          'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'z']

while True:
    print('\n#####################################')
    print('#          GERADOR DE SENHAS        #')
    print('#####################################')
    print('#                                   #')
    print('#     1 - Gerar senha               #')
    print('#     2 - Sair                      #')
    print('#                                   #')
    print('#####################################')
    opcao = input('\nResposta: ')
    if opcao == '2':
        break
    ativo = True
    while ativo:
        x = random.randint(111, 999)
        y = random.randint(1, 99)
        primeira = random.choice(letras)
        senha = (primeira.upper() + random.choice(letras) + str(x) + random.choice(letras) + str(y) + random.choice(
            letras))
        if opcao == '1':
            system('cls')
            print('\nGerando senha...')
            time.sleep(2)
            print("\nA senha gerada é:", senha, '\n')
            time.sleep(2)
            desejo = input('\nDeseja gerar outra senha?(s/n)\nResposta: ')
            if desejo == 's':
                system('cls')
                continue
                time.sleep(2)
            else:
                system('cls')
                ativo = False
time.sleep(2)
system('cls')
print('\n\n######################################\n')
print('Obrigado por testar o programa', nome.title(), ":)")
print('\n######################################\n')