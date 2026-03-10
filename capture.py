from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

def start_capture():
    print("Starting network capture...")
    sniff(prn=packet_callback, count=50)
