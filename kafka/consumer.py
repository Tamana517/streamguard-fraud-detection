from kafka import KafkaConsumer
import json
import joblib
import pandas as pd
import logging

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("FraudDetection")

# Load model + scaler
model = joblib.load('model/fraud_model.pkl')
scaler = joblib.load('model/scaler.pkl')

# Kafka Consumer
consumer = KafkaConsumer(
    'transactions',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

logger.info("🚀 Fraud Detection Consumer started...")

THRESHOLD = 0.7

for message in consumer:
    try:
        data = message.value

        # Convert to DataFrame
        df = pd.DataFrame([data])

        # Remove target if present
        df = df.drop(columns=['Class'], errors='ignore')

        # 🔥 SCALE INPUT
        df_scaled = scaler.transform(df)

        # 🔥 PREDICT PROBABILITY
        prob = model.predict_proba(df_scaled)[0][1]

        # 🔥 DECISION
        if prob > THRESHOLD:
            logger.warning(f"🚨 FRAUD DETECTED | Prob: {prob:.2f}")
        else:
            logger.info(f"✅ Normal Transaction | Prob: {prob:.2f}")

    except Exception as e:
        logger.error(f"Error processing message: {e}")