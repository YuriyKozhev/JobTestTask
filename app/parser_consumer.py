import logging
from config import LOGGING_CONFIG, RABBITMQ_CONN_PARAMS, PARSING_QUEUE_NAME, ERRORS_QUEUE_NAME
import pika

logging.basicConfig(**LOGGING_CONFIG)


def callback(ch, method, properties, body):
    logging.info("Message received with body=%s", body)


if __name__ == '__main__':
    with pika.BlockingConnection(RABBITMQ_CONN_PARAMS) as connection:
        channel = connection.channel()
        channel.queue_declare(queue=PARSING_QUEUE_NAME)

        channel.basic_consume(queue=PARSING_QUEUE_NAME, on_message_callback=callback, auto_ack=True)
        channel.start_consuming()
        logging.info("Consumer started listening to queue=%s", PARSING_QUEUE_NAME)
