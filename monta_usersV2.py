#!/usr/bin/python3
# monta_users.py - versao 2
# * Opcao de retirar acentos dos nomes completos
# * Opcao de mudar a forma de criacao de username para inicias e sobrenome)
# Desenvolvido por Eduardo Maronas Monks - 2024
# Uso permitido, venda proibida!
# Arquivo de entrada devera conter o nome completo do usuario
# Formato da saida para uso com o comando newusers do Linux
# professor15:senac2010:::Professor 15:/home/professor15:/bin/bash

 
import csv
import sys
import random
import string
import re
import argparse

# Gera senha aleatorias
def generate_password(length, data):
    password = ''
    for i in range(length):
        index = random.randint(0, len(data) - 1)
        character = data[index]
        password += character
    return password

# Gera o arquivo conflitos.csv com os conflitos encontrados
def write_to_csv(lista):
    with open('conflitos.csv', 'w') as csvfile:
        for cada in lista:
            csvfile.write(cada + '\n')

# Remove acentos do username
def f_remove_accents(old):
    new = old.lower()
    new = re.sub(r'[àáâãäå]', 'a', new)
    new = re.sub(r'[èéêë]', 'e', new)
    new = re.sub(r'[ìíîï]', 'i', new)
    new = re.sub(r'[òóôõö]', 'o', new)
    new = re.sub(r'[ùúûü]', 'u', new)
    new = re.sub(r'[ç]', 'c', new)
    new = re.sub(r'[ñ]', 'n', new)
    return new


parser = argparse.ArgumentParser(prog='monta_users', description='Gera nome de usuarios (nome.sobrenome), com a saida para uso com o comando newusers do Linux',  epilog='Versao 2 - 2024')
parser.add_argument('-a', '--arquivo', required=True, type=str, help='Nome do Arquivo')
parser.add_argument('-s', '--senha', required=False, default=12, type=int, help='Define o tamanho da senha')
parser.add_argument('-e', '--estatisticas', required=False, default=1, type=int, choices=range(0,2), help='Gera estatisticas- 0 desativa e 1 ativa')
parser.add_argument('-o', '--saida', required=False, default=1, type=int, choices=range(0,2), help='Formato da saida - 1 para uso com newusers e 0 - para saida em CSV')
parser.add_argument('-u', '--usuarios', required=False, default=1, type=int, choices=range(0,2), help='Formato do usuario - 1 para nome.sobrenome e 0 - iniciailsobrenome')
parser.add_argument('-c', '--acentos', required=False, default=1, type=int, choices=range(0,2), help='Remover acentos do nome completo - 1 para manter e 0 - para remover')
args = parser.parse_args()


arquivo=args.arquivo
tamsenha=int(args.senha)
estatisticas=int(args.estatisticas)
saida=int(args.saida)
fusuarios=int(args.usuarios)
acentos=int(args.acentos)

# Abre o arquivo com o nome completo dos usuarios

try:
        reader = csv.reader(open(arquivo, "r", encoding='utf-8'), delimiter=';')
except FileNotFoundError:
        print ("Erro na abertura do arquivo: " + arquivo)
        sys.exit()

# Lista auxiliares
usuarios = []
conflitos = []
completo = []
# Variaveis de contagem e flags
conflito_flag=0
conflito_count=0
tentativa1=0
tentativa2=0
tentativa3=0
linhas=0
# Composicao das senhas
listasenha = string.ascii_uppercase + string.digits + string.ascii_lowercase + "@#$!()&"


# Lista conteudo do arquivo
for row in reader:
        linhas=linhas+1 
        cont = row
# Remove os sobrenomes curtos "de, do, da, dos, das"
        nome=cont[0].split()
        nomelista=cont[0].split()
        for item in nome:
            if (item.lower() == 'de' or item.lower() == 'do' or item.lower() == 'da' or item.lower() == 'dos' or item.lower() == 'das'):
                nome.remove(item)
        if acentos == 0:
            for i in range(len(nomelista)):
                nomelista[i]=f_remove_accents(nomelista[i])
        nomecompleto = " ".join(str(element) for element in nomelista)
        elemento=nome
        qelemento=len(elemento)
# 1a tentativa: primeiro_nome.ultimo_sobrenome
        if fusuarios == 1:
            username = elemento[0].lower() + "." + elemento[-1].lower()
        if fusuarios == 0:
            username = elemento[0][0].lower() +  elemento[-1].lower()
        username=f_remove_accents(username)
        if username not in usuarios and elemento[0].lower() != elemento[-1].lower():
             usuarios.append(username)
             completo.append(cont[0].title())
             tentativa1=tentativa1+1
             if saida == 1:
                 print (username + ":" + generate_password(tamsenha,listasenha) + ":::" + nomecompleto.title().rstrip() + ":/home/" + username + ":/bin/bash")
             if saida == 0: 
                 print (username + ";" + generate_password(tamsenha,listasenha) + ";" + nomecompleto.title().rstrip())
        else:
# 2a tentativa: se houver mais de um sobrenome, primeiro_nome.nome_do_meio
            if qelemento >= 3:
                if fusuarios == 1:
                    username = elemento[0].lower() + "." + elemento[-2].lower()
                if fusuarios == 0:
                    username = elemento[0][0].lower() +  elemento[-1][0].lower() + elemento[-2].lower()
                username=f_remove_accents(username)
                if username not in usuarios and elemento[0].lower() != elemento[-2].lower():
                   if saida == 1:
                       print (username + ":" + generate_password(tamsenha,listasenha) + ":::" + nomecompleto.title().rstrip() + ":/home/" + username + ":/bin/bash")
                   if saida == 0:
                      print (username + ";" + generate_password(tamsenha,listasenha) + ";" + nomecompleto.title().rstrip())
                   usuarios.append(username)
                   completo.append(cont[0].title())
                   tentativa2=tentativa2+1
                else:
# 3a tentativa:  primeiro_nome.nome_do_meio2
                    if fusuarios == 1:
                        username = elemento[0].lower() + "." + elemento[-3].lower()
                    if fusuarios == 0:
                        username = elemento[0][0].lower() +  elemento[-3].lower()
                    username=f_remove_accents(username)
                    if username not in usuarios and elemento[0].lower() != elemento[-3].lower():
                       if saida == 1:
                           print (username + ":" + generate_password(tamsenha,listasenha) + ":::" + nomecompleto.title().rstrip() + ":/home/" + username + ":/bin/bash")
                       if saida == 0:
                           print (username + ";" + generate_password(tamsenha,listasenha) + ";" + nomecompleto.title().rstrip())
                       usuarios.append(username)
                       completo.append(cont[0].title()) 
                       tentativa3=tentativa3+1
# Caso nao seja possivel nenhuma das tentativas, considera conflito
        if cont[0].title() not in completo:
            conflitos.append(username + ";" + cont[0].title().rstrip())
            conflito_flag=1
            conflito_count=conflito_count+1

if conflito_flag == 1:
    print ("#######################")
    print ("#" + str(conflito_count) + " conflito(s) detectado(s)!")
    print ("#######################")
    # Salva os usuarios em conflito no arquivo confitos.csv
    write_to_csv(conflitos)

if estatisticas == 1:
    total=tentativa1 + tentativa2 + tentativa3 + conflito_count
    print ("#########################")
    print ("Estatisticas")
    print ("#########################")
    print ("Total de linhas: " + str(linhas) )
    print ("Total processado: " + str(total) )
    print ("1a tentativa: " + str(tentativa1) + " -  " + "%.2f" % ((tentativa1/total)*100)  + "%")
    print ("2a tentativa: " + str(tentativa2) + " -  " + "%.2f" % ((tentativa2/total)*100)  + "%")
    print ("3a tentativa: " + str(tentativa3) + " -  " + "%.2f" % ((tentativa3/total)*100)  + "%")
    print ("Conflitos: " + str(conflito_count) + " -  " + "%.2f" % ((conflito_count/total)*100)  + "%")


