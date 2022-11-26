import pika

def main():
    conexao_parametros = pika.ConnectionParameters("localhost")

    conexao = pika.BlockingConnection(conexao_parametros)

    channel = conexao.channel()

    channel.exchange_declare(exchange="messagens_matriz", exchange_type="fanout")

    lavanderia01 = channel.queue_declare(queue="fila_lavanderia_filial01")
    lavanderia02 = channel.queue_declare(queue="fila_lavanderia_filial02")
    lavanderia03 = channel.queue_declare(queue="fila_lavanderia_filial03")
    lavanderia04 = channel.queue_declare(queue="fila_lavanderia_filial04")
    lavanderia05 = channel.queue_declare(queue="fila_lavanderia_filial05")
    lavanderia06 = channel.queue_declare(queue="fila_lavanderia_filial06")

    channel.queue_bind(exchange="messagens_matriz", queue=lavanderia01.method.queue)
    channel.queue_bind(exchange="messagens_matriz", queue=lavanderia02.method.queue)
    channel.queue_bind(exchange="messagens_matriz", queue=lavanderia03.method.queue)
    channel.queue_bind(exchange="messagens_matriz", queue=lavanderia04.method.queue)
    channel.queue_bind(exchange="messagens_matriz", queue=lavanderia05.method.queue)
    channel.queue_bind(exchange="messagens_matriz", queue=lavanderia06.method.queue)

main()