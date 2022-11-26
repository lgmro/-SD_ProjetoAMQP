import pika

def main():
    conexao_parametros = pika.ConnectionParameters("localhost")

    conexao = pika.BlockingConnection(conexao_parametros)

    channel = conexao.channel()

    nomeFilaLavanderia04 = "fila_lavanderia_filial04"

    def callback(ch, method, properties, body):
        print(f"MATRIZ ENVIOU A SEGUINTE MENSAGEM:\n {body}\n")

    channel.basic_consume(queue=nomeFilaLavanderia04, auto_ack=True, on_message_callback=callback)


    print('''
  	=========================================================
	|                                                       |
	|                   LAVANDERIA: FILIAL 04               |
	|                                                       | 
	|              ESPERANDO MENSAGENS DA MATRIZ            | 
	|                                                       | 
  	|                 PARA FECHAR USE CTRL+C                | 
  	=========================================================
  	''')

    channel.start_consuming()

main()