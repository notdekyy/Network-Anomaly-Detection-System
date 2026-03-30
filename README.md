# V-SHIELD: AI/ML Network Anomaly Detection System

**AI/ML Project Submission**  
**VIT Bhopal University**  
**Professor: Dr. Rakesh Srivastava**  
**Student: Chirag Bhatia**  
**Registration Number: 25BAI10766**  
**Date: March 31, 2026**

## Project Overview

V-SHIELD is an **AI-powered Network Intrusion Detection System (NIDS)** that uses **statistical anomaly detection** with Z-Score analysis to identify malicious network traffic patterns in real-time. The system simulates packet capture, performs unsupervised anomaly detection, and provides interactive visualizations for cybersecurity monitoring.

**Core Technology Stack:**
- **Python 3.x** | **NumPy** | **Pandas** | **Matplotlib**
- **Statistical ML**: Z-Score Anomaly Detection
- **Real-time Dashboard** & **Interactive Visual Analytics**

##  Technical Architecture
┌─────────────────┐ ┌──────────────────┐ ┌──────────────────┐
│ Packet Input │───▶│ Statistical │───▶│ Anomaly │
│ (Manual Sim) │ │ Engine (Z-Score)│ │ Classification │
└─────────────────┘ └──────────────────┘ └──────────────────┘
│ │ │
▼ ▼ ▼
┌─────────────────┐ ┌──────────────────┐ ┌──────────────────┐
│ Network Hub │◀───│ Real-time │───▶│ Visual Analytics │
│ (Buffer) │ │ Dashboard │ │ (Matplotlib) │
└─────────────────┘ └──────────────────┘ └──────────────────┘

## Pseudo Code

```python
# MAIN ALGORITHM: Z-SCORE ANOMALY DETECTION
ALGORITHM ZScoreAnomalyDetection():
1. INITIALIZE network_buffer[MAX_SIZE]
2. WHILE user_active:
   3.   CHOOSE operation:
         CASE "ADD_PACKET":
            4.   packet ← CREATE_NEW_PACKET()
            5.   packet.source_ip ← INPUT()
            6.   packet.bytes ← INPUT()
            7.   ADD_TO_BUFFER(packet)
         CASE "ANALYZE":
            8.   data ← EXTRACT_BYTES_FROM_BUFFER()
            9.   mean ← CALCULATE_MEAN(data)
           10.   std ← CALCULATE_STD(data)
           11.   FOR each_packet IN buffer:
               12.      z_score ← (packet.bytes - mean) / std
               13.      IF z_score > THRESHOLD (3.0):
                      14.         MARK_ANOMALY(packet, z_score)
           15.   DISPLAY_RESULTS()
         CASE "VISUALIZE":
            16.  GENERATE_SCATTER_PLOT()
            17.  GENERATE_HISTOGRAM()
```

## Workflow Flowchart
START
│ ▼ [SYSTEM INIT] ──► [Buffer Ready: 500 slots]
│ ▼ [MAIN MENU LOOP]
├─► 1. Add Packet ──► [Input: IP, Bytes, Protocol] ──► [Store in Buffer]
│ │
│ ▼
└─► 2. Run Analysis ──► [Calculate Z-Scores] ◄────────┘
│
▼
[Z > 3.0?] ─── NO ──► [NORMAL]
│
YES
▼
[Z > 5.0?] ─── NO ──► [WARNING]
│
YES
▼
[CRITICAL]
│
▼
[Display Results] ──► [Dashboard/Table] ──► [Graphs: Scatter + Histogram]
│ ▼ [Continue?]
│ YES
└─ NO ──► END

## Features

### Core Detection Engine
- **Z-Score Statistical Analysis**: \( Z = \frac{x - \mu}{\sigma} \)
- **Multi-tier Alert System**: NORMAL | WARNING | CRITICAL
- **Real-time Buffer Management**: 500 packet capacity

### Interactive Dashboard
ID | SOURCE IP | BYTES | Z-SCORE | STATUS
1 | 192.168.1.10 | 25.5 | 1.23 | CLEAN
45 | 10.0.0.255 | 450.2 | 4.87 | [CRITICAL]

### Advanced Visualizations
- **Scatter Plot**: Traffic volume vs packet sequence (Red=Anomaly, Green=Normal)
- **Histogram**: Traffic distribution frequency analysis

## System Configuration

```python
MAX_TRAFFIC_LOGS = 500      # Buffer capacity
THRESHOLD_Z = 3.0           # Anomaly detection threshold
SYSTEM_NAME = "V-SHIELD"    # Branding
```

**Threshold Logic:**
- \( |Z| \leq 3.0 \): **NORMAL** (99.7% confidence)
- \( 3.0 < |Z| \leq 5.0 \): **WARNING**
- \( |Z| > 5.0 \): **CRITICAL**

## Mathematical Foundation

The system implements **Unsupervised Anomaly Detection** using Z-Score:

\[
Z = \frac{x - \mu}{\sigma}
\]

Where:
- \( x \): Observed traffic volume (KB)
- \( \mu \): Mean traffic volume
- \( \sigma \): Standard deviation

**Detection Rule**: \( |Z| > 3.0 \) indicates statistical outlier (anomaly)

## Installation & Usage

```bash
# 1. Clone/Setup
git clone <your-repo>
cd v-shield

# 2. Install Dependencies
pip install numpy pandas matplotlib

# 3. Run System
python vshield.py
```

**Demo Usage:**
**1.** Add 10-15 normal packets (10-50 KB each)

**2.** Add 2-3 anomalous packets (300+ KB each)

**3.** Run Analysis → Observe CRITICAL alerts

**4.** View Graphs → Red dots = Threats

## Learning Outcomes

1. **Statistical ML**: Z-Score anomaly detection implementation
2. **Data Visualization**: Matplotlib for cybersecurity analytics
3. **Real-time Systems**: Buffer management & dashboard design
4. **OOP Design**: Class-based packet modeling
5. **Interactive CLI**: Menu-driven cybersecurity tool

## Sample Output
--- Analysis Results (N=12) ---
Network Mean Traffic: 45.23 KB
Standard Deviation: 12.45

ID | SOURCE IP | BYTES | Z-SCORE | STATUS
8 | 172.16.1.100 | 289.5 | 4.87 | [CRITICAL]

## Future Enhancements

- [ ] **Machine Learning**: Isolation Forest, Autoencoders
- [ ] **Real Packet Capture**: Scapy integration
- [ ] **Web Dashboard**: Flask/Dash frontend
- [ ] **Database**: SQLite for persistent storage
- [ ] **Multi-protocol**: Deep packet inspection

## References

1. **Z-Score Anomaly Detection**: NIST SP 800-53
2. **Network IDS**: "Computer Networking: Top-Down Approach" - Kurose
3. **Python ML**: "Hands-On ML with Scikit-Learn" - Géron

---

**Submitted by: Chirag Bhatia (25BAI10766)**  
**VIT Bhopal | AI/ML Department**  
**Professor: Dr. Rakesh Srivastava**

