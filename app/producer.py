import logging
import time
from config import RABBITMQ_CONN_PARAMS, PARSING_QUEUE_NAME, LOGGING_CONFIG
import pika

logging.basicConfig(**LOGGING_CONFIG)

if __name__ == '__main__':
    with pika.BlockingConnection(RABBITMQ_CONN_PARAMS) as connection:
        channel = connection.channel()
        channel.queue_declare(queue=PARSING_QUEUE_NAME)

        while True:
            message_body = b'hello-world'
            channel.basic_publish(exchange='', routing_key=PARSING_QUEUE_NAME, body=message_body)
            logging.info("Message sent with routing_key=%s and body=%s", PARSING_QUEUE_NAME, message_body)
            time.sleep(30)

