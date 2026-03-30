import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# GLOBAL CONFIGURATIONS (Metadata)
# ==========================================
MAX_TRAFFIC_LOGS = 500  # Equivalent to your maxseats
SYSTEM_NAME = "V-SHIELD: AI/ML NETWORK MONITOR"
THRESHOLD_Z = 3.0       # Statistical threshold for anomalies

# ==========================================
# CORE DATA CLASS (Mirroring your Booking Class)
# ==========================================
class NetworkPacket:
    def __init__(self):
        self.packet_id = 0          # Equivalent to seatnumber
        self.source_ip = "0.0.0.0"
        self.dest_ip = "0.0.0.0"
        self.bytes_kb = 0.0
        self.packet_count = 0
        self.protocol = "TCP"
        self.is_anomaly = False     # Equivalent to isbooked
        self.z_score = 0.0
        self.severity = "NORMAL"

# Global List to store network logs
network_hub = [NetworkPacket() for _ in range(MAX_TRAFFIC_LOGS)]
active_logs_count = 0

# ==========================================
# SYSTEM INITIALIZATION
# ==========================================
def initialize_system():
    """Sets all logs to default state."""
    global active_logs_count
    active_logs_count = 0
    for i in range(MAX_TRAFFIC_LOGS):
        network_hub[i].is_anomaly = False
        network_hub[i].bytes_kb = 0.0
        network_hub[i].packet_id = i + 1
    print(f"[*] {SYSTEM_NAME} Initialized. Buffer Ready.")

# ==========================================
# DATA ANALYSIS ENGINE (The "ML" Part)
# ==========================================
def run_statistical_engine():
    """
    Calculates Z-Scores for all active logs.
    Formula: Z = (x - mean) / std_dev
    """
    global active_logs_count
    if active_logs_count < 2:
        print("[!] Not enough data to perform statistical analysis.")
        return

    # Extracting data for NumPy calculations
    data_points = [network_hub[i].bytes_kb for i in range(active_logs_count)]
    mean_val = np.mean(data_points)
    std_val = np.std(data_points)

    if std_val == 0: std_val = 1 # Avoid division by zero

    print(f"\n--- Analysis Results (N={active_logs_count}) ---")
    print(f"Network Mean Traffic: {mean_val:.2f} KB")
    print(f"Standard Deviation:   {std_val:.2f}")

    for i in range(active_logs_count):
        log = network_hub[i]
        log.z_score = (log.bytes_kb - mean_val) / std_val
        
        # Detection Logic
        if log.z_score > THRESHOLD_Z:
            log.is_anomaly = True
            log.severity = "CRITICAL" if log.z_score > 5 else "WARNING"
        else:
            log.is_anomaly = False
            log.severity = "NORMAL"

# ==========================================
# USER ACTIONS (Mirroring your book/cancel)
# ==========================================
def add_network_log():
    """Adds a new traffic entry manually (Simulating a packet capture)."""
    global active_logs_count
    if active_logs_count >= MAX_TRAFFIC_LOGS:
        print("[!] Network Buffer Full!")
        return

    print(f"\n--- Entry {active_logs_count + 1} Configuration ---")
    log = network_hub[active_logs_count]
    log.source_ip = input("Enter Source IP (e.g. 192.168.1.1): ").strip()
    log.dest_ip = input("Enter Destination IP: ").strip()
    log.bytes_kb = float(input("Enter Traffic Volume (KB): "))
    log.packet_count = int(input("Enter Packet Count: "))
    log.protocol = input("Enter Protocol (TCP/UDP/ICMP): ").upper()
    
    active_logs_count += 1
    print("[+] Log Registered Successfully.")

def display_security_dashboard():
    """Prints a formatted table of all captured traffic."""
    print(f"\n{'ID':<4} | {'SOURCE IP':<15} | {'BYTES':<8} | {'Z-SCORE':<8} | {'STATUS'}")
    print("-" * 60)
    for i in range(active_logs_count):
        log = network_hub[i]
        status = f"[{log.severity}]" if log.is_anomaly else "CLEAN"
        print(f"{log.packet_id:<4} | {log.source_ip:<15} | {log.bytes_kb:<8.1f} | {log.z_score:<8.2f} | {status}")

def show_visual_graphs():
    """Generates the Matplotlib analytics."""
    if active_logs_count == 0:
        print("[!] No data to plot.")
        return

    bytes_list = [network_hub[i].bytes_kb for i in range(active_logs_count)]
    colors = ['red' if network_hub[i].is_anomaly else 'green' for i in range(active_logs_count)]

    plt.figure(figsize=(10, 6))
    
    # Scatter Plot
    plt.subplot(2, 1, 1)
    plt.scatter(range(active_logs_count), bytes_list, c=colors, s=50, edgecolor='black')
    plt.title("Real-Time Traffic Volumetric Analysis")
    plt.ylabel("KiloBytes (KB)")

    # Histogram
    plt.subplot(2, 1, 2)
    plt.hist(bytes_list, bins=15, color='silver', edgecolor='black')
    plt.title("Traffic Distribution Frequency")
    plt.xlabel("Volume (KB)")

    plt.tight_layout()
    plt.show()

# ==========================================
# MAIN INTERFACE
# ==========================================
def main():
    initialize_system()
    menu_choice = 0
    
    while menu_choice != 6:
        print(f"\n--- {SYSTEM_NAME} ---")
        print("1. Add New Network Log (Packet Capture)")
        print("2. Run Detection Engine (Calculate Z-Scores)")
        print("3. Display All Traffic Logs")
        print("4. Show Security Alerts Only")
        print("5. Generate Visual Analytics (Graphs)")
        print("6. Exit System")
        
        try:
            menu_choice = int(input("Select Option: "))
        except ValueError:
            print("Invalid Input. Use numbers 1-6.")
            continue

        if menu_choice == 1:
            add_network_log()
        elif menu_choice == 2:
            run_statistical_engine()
        elif menu_choice == 3:
            display_security_dashboard()
        elif menu_choice == 4:
            print("\n--- CRITICAL ANOMALIES ---")
            found = False
            for i in range(active_logs_count):
                if network_hub[i].is_anomaly:
                    print(f"LOG #{network_hub[i].packet_id}: Threat from {network_hub[i].source_ip} (Z={network_hub[i].z_score:.2f})")
                    found = True
            if not found: print("Network Status: SECURE")
        elif menu_choice == 5:
            show_visual_graphs()
        elif menu_choice == 6:
            print("System offline.")
        else:
            print("Choice out of range.")

if __name__ == "__main__":
    main()