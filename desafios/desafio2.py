#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivvo e todas as informações possíveis sobre ele;

var = input('Digite qualquer coisa: ')
print('É um número', var.isnumeric())
print('Só tem espaço', var.isspace() )
print('Só tem letra maiuscula', var.islower())
print('É alfanumerico', var.isalnum())