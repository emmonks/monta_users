# monta_users
Script em Pyhton 3 para gerar username a partir de nomes completos, com tratamento de conflitos. O script trata os conflitos de nomes de usuários iguais, usando o formato "nome.sobrenome". Não são usadas
bibliotecas fora do padrão da instalação do Python3.

Foi criado para uso com o utilitário "newusers" do Linux, mas pode ser adaptado para qualquer uso. 

Para utilizar o script, passar o tamanho da senha e o nome do arquivo com os nomes do usuários, um por linha.

Em caso de conflitos que não sejam resolvidos pelo script, será gerado um arquivo "conflitos.csv" no mesmo diretório do arquivo. Nestes casos, deverá ser feito de forma manual.


usage: monta_users [-h] -a ARQUIVO [-s SENHA] [-e ESTATISTICAS] [-o {0,1}]


Gera nome de usuarios (nome.sobrenome), com a saida para uso com o comando newusers do Linux


options:

  -h, --help            show this help message and exit
  
  -a ARQUIVO, --arquivo ARQUIVO
  
                        Nome do Arquivo
                        
  -s SENHA, --senha SENHA
  
                        Define o tamanho da senha
                        
  -e ESTATISTICAS, --estatisticas ESTATISTICAS
  
                        Gera estatisticas- 0 desativa e 1 ativa
                        
  -o {0,1}, --saida {0,1}
  
                        Formato da saida - 1 para uso com newusers e 0 - para saida em CSV
                        

Versao 1 - 2024

======================================================

usage: monta_users [-h] -a ARQUIVO [-s SENHA] [-e {0,1}] [-o {0,1}] [-u {0,1}] [-c {0,1}]


Gera nome de usuarios (nome.sobrenome), com a saida para uso com o comando newusers do Linux


options:

  -h, --help            show this help message and exit
  
  -a ARQUIVO, --arquivo ARQUIVO
  
                        Nome do Arquivo
                        
  -s SENHA, --senha SENHA
  
                        Define o tamanho da senha
                        
  -e {0,1}, --estatisticas {0,1}
  
                        Gera estatisticas- 0 desativa e 1 ativa
                        
  -o {0,1}, --saida {0,1}
  
                        Formato da saida - 1 para uso com newusers e 0 - para saida em CSV
                        
  -u {0,1}, --usuarios {0,1}
  
                        Formato do usuario - 1 para nome.sobrenome e 0 - iniciailsobrenome
                        
  -c {0,1}, --acentos {0,1}
  
                        Remover acentos do nome completo - 1 para manter e 0 - para remover
                        

Versao 2 - 2024


