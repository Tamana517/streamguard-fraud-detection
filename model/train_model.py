import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import joblib

# Load data
data = pd.read_csv('data/raw/creditcard.csv').sample(50000, random_state=42)

X = data.drop('Class', axis=1)
y = data['Class']

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("Class distribution:")
print(y_train.value_counts())

# 🔥 SCALE DATA (VERY IMPORTANT)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train model
model = LogisticRegression(max_iter=2000, class_weight='balanced')
model.fit(X_train_scaled, y_train)

# Threshold tuning
thresholds = [0.5, 0.6, 0.7]
probs = model.predict_proba(X_test_scaled)[:, 1]

for t in thresholds:
    print(f"\n🔹 Threshold = {t}")
    y_pred = (probs > t).astype(int)
    print(classification_report(y_test, y_pred))

# Save model + scaler
joblib.dump(model, 'model/fraud_model.pkl')
joblib.dump(scaler, 'model/scaler.pkl')

print("\nModel and scaler saved successfully!")