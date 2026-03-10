from sklearn.ensemble import IsolationForest

def train_model(data):
    model = IsolationForest(contamination=0.05)
    model.fit(data)
    return model

def detect_anomalies(model, data):
    prediction = model.predict(data)
    return prediction
