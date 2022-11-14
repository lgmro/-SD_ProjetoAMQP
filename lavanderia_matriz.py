import pika

def main():
    conexao_parametros = pika.ConnectionParameters("localhost")

    conexao = pika.BlockingConnection(conexao_parametros)

    channel = conexao.channel()

    channel.exchange_declare(exchange="messagens_matriz", exchange_type="fanout")

    print('''
  	=========================================================
	|                                                       |
	|                   LAVANDERIA: MATRIZ                  |
	|                                                       | 
	|       VAMOS COMEÇAR A ENVIAR O LOTE DE MENSAGENS      | 
	|                                                       | 
  	|                 PARA FECHAR USE CTRL+C                | 
  	=========================================================
  	''')

    for i in range(1,6):
        mensagem = f"Cliente solicitou o uso de uma maquina na lavanderia 0{i}"
        mensagem_matriz = f"Mensagem 0{i}: {mensagem}"
        channel.basic_publish(exchange="messagens_matriz", routing_key="", body=mensagem_matriz)
        print(f"Enviado a mensagem 0{i} -> {mensagem}")
      

    conexao.close()

main()