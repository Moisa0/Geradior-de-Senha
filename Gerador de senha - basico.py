#---------Bibliotecas utilizadas-----------
import random
import string 


#----------Função gerar senha --------------
def criar_senha(lmin, lmai, num, car):
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    global combinar
    combinar = ""

    #---- Condição para Minusculo ----
    if lmin == 1:
        combinar = combinar +  s1
    
    else:
        pass

    #---- Condição para Maiúsculo ----
    if lmai == 1:
        combinar = combinar + s2
    
    else:
        pass

    #---- Condição para Números ----
    if num == 1:
        combinar = combinar + s3
    
    else:
        pass

    #---- Condição para Caracteres especiais ----
    if car == 1:
        combinar = combinar + s4
    
    else:
        pass


    
    senha = "".join(random.sample(combinar, total ))
    print('Sua nova senha é:',senha)




s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.digits
s4 = string.punctuation

print('>>>>>>>GERADOR DE SENHAS<<<<<<<')

total = int(input('Qual o tamanho total que deseja na senha?'))


print('\nDeseja que a senha contenha letras minusculas?')
lmin = int(input('1 [Sim] ou 0 [Não]'))


print('\nDeseja que a senha contenha letras maiusculas?')
lmai = int(input('1 [Sim] ou 0 [Não]'))


print('\nDeseja que a senha contenha numeros?')
num = int(input('1 [Sim] ou 0 [Não]'))

print('\nDeseja que a senha contenha caracteres especiais?')
car = int(input('1 [Sim] ou 0 [Não]'))
criar_senha(lmin, lmai, num,car)