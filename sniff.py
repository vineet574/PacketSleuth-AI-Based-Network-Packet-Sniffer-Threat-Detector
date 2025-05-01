from scapy.all import sniff, IP
from analyze import analyze_packet

def packet_callback(packet):
    if IP in packet:
        pkt_data = {
            "src": packet[IP].src,
            "dst": packet[IP].dst,
            "proto": packet[IP].proto
        }
        analyze_packet(pkt_data)

def start_sniffing():
    print("[*] Starting Packet Capture...")
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    start_sniffing()
