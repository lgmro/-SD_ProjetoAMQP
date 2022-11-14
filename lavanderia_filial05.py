import pika

def main():
    conexao_parametros = pika.ConnectionParameters("localhost")

    conexao = pika.BlockingConnection(conexao_parametros)

    channel = conexao.channel()

    channel.exchange_declare(exchange="messagens_matriz", exchange_type="fanout")

    fila = channel.queue_declare(queue="", exclusive=True)

    channel.queue_bind(exchange="messagens_matriz", queue=fila.method.queue)

    def callback(ch, method, properties, body):
        print(f"MATRIZ ENVIOU A SEGUINTE MENSAGEM:\n {body}\n")

    channel.basic_consume(queue=fila.method.queue, auto_ack=True, on_message_callback=callback)


    print('''
  	=========================================================
	|                                                       |
	|                   LAVANDERIA: FILIAL 05               |
	|                                                       | 
	|              ESPERANDO MENSAGENS DA MATRIZ            | 
	|                                                       | 
  	|                 PARA FECHAR USE CTRL+C                | 
  	=========================================================
  	''')

    channel.start_consuming()

main()