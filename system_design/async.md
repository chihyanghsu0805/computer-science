# Asynchronism

1.  Doing work in advance and serve with a low request time, dynamic content into static content.
2.  Sends a job to a queue.

-   Message Queues
    -   Redis
    -   RabbitMQ
    -   Amazon SQS

-   Task Queues
    -   Celery

-   Back Pressure: queue may become bigger than memoru, casuing cahe miss. Back pressure limites the queue size.
