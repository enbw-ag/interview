export $(cat .env)
pytest -v -s message_queue/test