# Projeto AMQP com RabbitMQ

## Integrantes:
#### Adilson Lucas Nogueira Almeida - RA: 1272117609;
#### Gustavo Rafael Vieira Goes - RA: 1272117750;
#### Lucas Gabriel Maciel Marinho - RA: 1272115763;
#### Lucas Nery Moreno - RA: 1272121356;
#### Marina Fernandes Porto Leite - RA: 1272121593;

## Requisitos para instalação:
#### É necessário ter o Python 3 instalado. Usamos a versão 3.10.6;

    Mais informações de como instalar python aqui: https://www.python.org/downloads/

#### Após ter instalado o python, use o pip para instalar a biblioteca "pika". Se você tiver mais de uma versão do python em sua máquina, tenha atenção à qual versão do python a biblioteca "pika" será instalada na sua máquina e use essa versão para executar a aplicação. Segue abaixo comandos que você pode usar para instalar: 

    pip install pika 
    pip3 install pika
    python3 -m pip install pika;
    
    Mais informações de como instalar o pika aqui: https://pika.readthedocs.io/en/stable/

#### É necessário instalar o RabbitMQ.

    Segue link: https://www.rabbitmq.com/download.html 

    Se você tiver o docker no seu computador, basta usar o seguinte comando: docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.11-management (dependendo de como foi instalado o docker na sua máquina, talvez precise usar o "sudo" antes do comando e colocar a sua senha)

#### Caso você queira visualizar melhor o código, será necessário uma IDE, recomendamos usar Visual Studio Code;

    Para instalar o VSCode acesse: https://code.visualstudio.com/

#### Você pode usar um terminal para execucar a aplicação. Ex.: CMD, PowerShell, Shell;

#### Para o sistema operacional, pode-se usar o mac os, windows ou sistemas linux. Testamos no ubuntu e windows.


## Instrução para instalação:
#### 1 - Baixe a pasta do projeto;

#### 2 - Rode o RabbitMQ, com o docker ou instalado na sua máquina. Tenha atenção ao enderenço do RabbitMQ. Usando o docker, com o comando citado acima, acessamos o RabbitMQ com o seguinte enderenço: http://localhost:15672/. Geralmente o Username é: guest e o password também é: guest;

#### 3 - Caso você for usar a mesma máquina para executar os 7 códigos-fonte (1 da matriz e 6 das filiais), não precisa realizar nenhuma alteração HOST(IP), pois usamos "localhost" no código e o python geralmente conseguira acessar o RabbitMQ. Mas caso você tenha alguma configuração diferente no seu RabbitMQ, é importante fica atentando ao enderenço e se necessário mudá-lo nos códigos-fonte da matriz e das filiais;

#### 4 - Executando a aplicação na mesma máquina, você precisará abrir 6 terminais na pasta do projeto e execute primeiramente os códigos-fontes das filiais. Você pode usar o comando: 
    py lavanderia_filial01.py (Windows) ou
    python lavanderia_filial01.py (Windows) ou
    python3 lavanderia_filial01.py (Ubuntu);

#### 5 - Após as 6 fialias abertas, você verá que será exibido uma texto informando o número da filial e que ela está aguardando mensagens da matriz;

#### 6 - Abra outro terminal e execute a matriz. 
    Ex.: py lavanderia_matriz.py (Windows), python lavanderia_matriz.py (Windows), python3 lavanderia_matriz.py (Ubuntu);

#### 7 - A matriz enviará 5 mensagens uma de cada vez para cada filial e depois o cliente será finalizado;

#### 8 - Você notará que nos terminais das filiais, será exibida as mensagens enviada pela matriz;

#### 9 - Caso você queirá enviar mais cinco mensagens, é só iniciar a matriz novamente e enviar mais mensagens.

## Tutorial de uso das aplicações:
#### 1 - Vamos executar o RabbitMQ. Aqui usamos o docker: 

<div align = "center">
    <img src= "https://user-images.githubusercontent.com/84135761/203670937-170eeaf2-92eb-4c12-b916-2ef9c1e0c4d8.png" width = "800px"/>
</div>

#### 2 - Agora vamos executar as lavanderias: lavanderia_filial01.py, lavanderia_filial02.py, lavanderia_filial03.py, lavanderia_filial04.py, lavanderia_filial05.py, lavanderia_filial06.py. 
<div align = "center">
    <img src= "https://user-images.githubusercontent.com/84135761/203670934-1c0e3302-f42e-4a84-a3da-17b62d1584ed.png" width = "800px"/>
</div>

#### 3 - Acessando o RabbitMQ, você verá que na opção de "Connections" será possível vê as 6 lavanderias conectadas:
<div align = "center">
    <img src= "https://user-images.githubusercontent.com/84135761/203670933-04d60de5-aa08-4b4d-914b-d3bc9a8a3f1d.png" width = "800px"/>
</div>

#### 4 - Vamos executar a lavanderia_matriz.py para enviar as 5 mensagens. Você perceberá que após enviar as mensagens a matriz é encerrada. Se quiser enviar mais mensagens é só executar a lavanderia_matriz.py novamente:
<div align = "center">
    <img src= "https://user-images.githubusercontent.com/84135761/203670929-3ee05eee-d14e-4993-86a1-59463f156aa7.png" width = "800px"/>
</div>

#### 5 - Perceba que as 6 lavanderias recebeu as 5 mensagens:
<div align = "center">
    <img src= "https://user-images.githubusercontent.com/84135761/203670928-e19cd3c8-6b48-499d-b635-f03b64b83b87.png" width = "800px"/>
</div>


#### Obs.: Para finalizar as lavanderias, você pode usar o comando "CTRL + C".