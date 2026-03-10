import pandas as pd
from model import train_model, detect_anomalies

def generate_sample_data():
    normal = [60, 62, 59, 61, 60, 63, 58, 64]
    attack = [300, 350, 400]

    data = normal + attack
    df = pd.DataFrame(data, columns=["packet_size"])
    return df

def main():
    print("AI Network Anomaly Detection System")

    data = generate_sample_data()

    model = train_model(data)

    results = detect_anomalies(model, data)

    data["anomaly"] = results

    print(data)

if __name__ == "__main__":
    main()
