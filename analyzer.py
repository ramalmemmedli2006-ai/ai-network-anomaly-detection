import pandas as pd

def extract_features(packets):
    data = []

    for pkt in packets:
        length = len(pkt)
        data.append(length)

    df = pd.DataFrame(data, columns=["packet_size"])
    return df
