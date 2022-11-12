# Projeto AMQP com RabbitMQ

## Integrantes:
#### Adilson Lucas Nogueira Almeida - RA: 1272117609;
#### Gustavo Rafael Vieira Goes - RA: 1272117750;
#### Lucas Gabriel Maciel Marinho - RA: 1272115763;
#### Lucas Nery Moreno - RA: 1272121356;
#### Marina Fernandes Porto Leite - RA: 1272121593;

## Requisitos para instalação:
#### É necessário ter o Python 3 instalado. Usamos a versão 3.10.6;
#### Após ter instalado o python, use o pip para instalar a biblioteca "pika". Se você tiver mais de uma versão do python em sua máquina, tenha atenção à qual versão do python a biblioteca "pika" será instalada na sua máquina e use essa versão para executar a aplicação. Comandos que você pode usar para instalar: pip install pika/ pip3 install pika/ python3 -m pip install pika;
#### É necessário instalar o RabbitMQ. Segue link: https://www.rabbitmq.com/download.html. Se você tiver o docker no seu computador, basta usar o seguinte comando: docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.11-management (dependendo de como foi instalado o docker na sua máquina, talvez precise usar o "sudo" antes do comando e colocar a sua senha);
#### Você pode usar um terminal para execucar a aplicação. Ex.: CMD, PowerShell, Shell;
#### Para o sistema operacional, pode-se usar o mac os, windows ou sistemas linux. Testamos no ubuntu.


## Instrução para instalação:
#### 1 - Baixe a pasta do projeto;
#### 2 - Rode o RabbitMQ, com o docker ou instalado na sua máquina. Tenha atenção ao enderenço do RabbitMQ. Usando o docker, com o comando citado acima, acessamos o RabbitMQ com o seguinte enderenço: http://localhost:15672/. Geralmente o Username é: guest e o password também é: guest;
#### 3 - Caso você for usar a mesma máquina para executar os 7 códigos-fonte (1 da matriz e 6 das filiais), não precisa realizar nenhuma alteração HOST(IP), pois usamos "localhost" no código e o python geralmente conseguira acessar o RabbitMQ. Mas caso você tenha alguma configuração diferente no seu RabbitMQ, é importante fica atentando ao enderenço e se necessário mudá-lo nos códigos-fonte da matriz e das filiais;
#### 4 - Executando a aplicação na mesma máquina, você precisará abrir 6 terminais na pasta do projeto e execute primeiramente os códigos-fontes das filiais. Você pode usar o comando: py lavanderia_filial01.py (Windows) ou python3 lavanderia_filial01.py (Ubuntu);
#### 5 - Após as 6 fialias abertas, você verá que será exibido uma texto informando o número da filial e que ela está aguardando mensagens da matriz;
#### 6 - Abra outro terminal e execute a matriz. Ex.: py lavanderia_matriz.py (Windows), python3 lavanderia_matriz.py (Ubuntu);
#### 7 - A matriz receberá 5 mensagens escritas por você e enviará uma de cada vez para cada filial e depois será finalizada;
#### 8 - Você notará que nos terminais das filiais, será exibida as mensagens enviada pela matriz;
#### 9 - Caso você queirá enviar mais cinco mensagens, é só iniciar a matriz novamente e enviar mais mensagens.
