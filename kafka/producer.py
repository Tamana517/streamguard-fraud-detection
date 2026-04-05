from kafka import KafkaProducer
import pandas as pd
import json
import time
import logging

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Producer")

# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda x: json.dumps(x).encode('utf-8'),
    retries=5
)

def load_data(path):
    try:
        data = pd.read_csv(path)
        logger.info("Dataset loaded successfully")
        return data
    except Exception as e:
        logger.error(f"Error loading dataset: {e}")
        return None

def send_transactions(data):
    for i, row in data.iterrows():
        try:
            message = row.to_dict()

            # ❗ remove label column
            message.pop('Class', None)

            producer.send('transactions', value=message)

            if i % 1000 == 0:
                logger.info(f"Sent {i} records")

            time.sleep(0.01)  # simulate streaming

        except Exception as e:
            logger.error(f"Error sending data: {e}")

    producer.flush()
    logger.info("All data sent successfully")

if __name__ == "__main__":
    logger.info("🚀 Starting Producer...")
    
    df = load_data('data/raw/creditcard.csv')
    
    if df is not None:
        send_transactions(df)