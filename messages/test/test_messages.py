from datetime import datetime
from messages import StartTransaction, StopTransaction


def test_start_transaction_message():
    msg = StartTransaction(connector_id=1,
                           id_tag="User1",
                           meter_start=0.0,
                           timestamp=str(datetime.now()))
