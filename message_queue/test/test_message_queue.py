from message import StartTransaction, StopTransaction, LoggingMessageQueue


def test_message_queue():
    # Create messages
    start_msg = StartTransaction(1, "user123", 100.0, "2025-03-17T10:00:00Z")
    stop_msg = StopTransaction(1, 1, 150.0, "2025-03-17T11:00:00Z")

    # Create a LoggingMessageQueue
    queue = LoggingMessageQueue()

    # Add messages to the queue
    queue.add_message(start_msg)
    queue.add_message(stop_msg)

    # Get messages from the queue
    msg1 = queue.get_message()
    msg2 = queue.get_message()
    msg3 = queue.get_message()  # This should return None

    assert msg1.connector_id == 1
    assert msg1.id_tag == "user123"
    assert msg1.meter_start == 100.0
    assert msg1.timestamp == "2025-03-17T10:00:00Z"

    assert msg2.connector_id == 1
    assert msg2.transaction_id == 1
    assert msg2.meter_stop == 150.0
    assert msg2.timestamp == "2025-03-17T11:00:00Z"

    assert msg3 is None
