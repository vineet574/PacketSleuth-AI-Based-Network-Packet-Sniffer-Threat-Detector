import joblib

model = joblib.load("model/rf_model.pkl")  # Load pre-trained model

def analyze_packet(data):
    # For now, only protocol as feature (expandable)
    features = [data["proto"]]
    prediction = model.predict([features])
    if prediction[0] == 1:
        print(f"[!] ALERT: Suspicious activity from {data['src']} to {data['dst']}")
