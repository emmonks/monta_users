# monta_users
Script em Pyhton 3 para gerar username a partir de nomes completos, com tratamento de conflitos. O script trata os conflitos de nomes de usuários iguais, usando o formato "nome.sobrenome". Não são usadas
bibliotecas fora do padrão da instalação do Python3.

Foi criado para uso com o utilitário "newusers" do Linux, mas pode ser adaptado para qualquer uso. 

Para utilizar o script, passar o tamanho da senha e o nome do arquivo com os nomes do usuários, um por linha.

Em caso de conflitos que não sejam resolvidos pelo script, será gerado um arquivo "conflitos.csv" no mesmo diretório do arquivo. Nestes casos, deverá ser feito de forma manual.


