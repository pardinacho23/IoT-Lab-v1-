# IoT/OT Security Home Lab

A hands-on IoT/OT security research lab built on a Raspberry Pi 4, focused on industrial protocol analysis, Zigbee traffic capture, and network segmentation. Designed to simulate real-world OT environments for security research and protocol analysis.

---

## Hardware

| Device | Role | Status |
|--------|------|--------|
| Raspberry Pi 4 | Central gateway — MQTT broker, packet capture, protocol simulation | ✅ Active |
| Texas Instruments CC2531 | Zigbee sniffer — passive traffic capture | ✅ Connected |
| CH340 UART converter | Modbus RTU serial interface | ✅ Connected |
| Sonoff Zigbee 3.0 USB Dongle Plus (CC2652P) | Zigbee coordinator | 🔜 Pending |
| IKEA TRÅDFRI smart plug | Zigbee end device for traffic analysis | 🔜 Pending |
| MikroTik hAP ac | Managed router — VLAN segmentation, port mirroring | 🔜 Pending |

---

## Network Topology

```
Internet
    │
Router ISP (192.168.1.1)
    │
Raspberry Pi 4 — Gateway IoT (10.0.1.10)
    ├── VLAN 10 — IoT devices      (10.0.10.0/24)  MQTT · Zigbee · Modbus
    ├── VLAN 20 — Analysis         (10.0.20.0/24)  Ubuntu · Kali · UTM
    └── VLAN 30 — Management       (10.0.30.0/24)  Windows 11 · SSH · RDP
```

Port mirroring: VLAN 10 → Kali Linux for passive traffic analysis.

---

## Software Stack

### Raspberry Pi 4 (Raspberry Pi OS Lite 64-bit)

| Tool | Purpose |
|------|---------|
| Mosquitto | MQTT broker |
| tcpdump / tshark | Packet capture |
| nmap | Network discovery |
| paho-mqtt | Python MQTT client |
| pymodbus 3.6.9 | Modbus TCP/RTU via Python |
| Zigbee2MQTT | Zigbee coordinator management (pending Sonoff) |

### Analysis machines

| Machine | Tools |
|---------|-------|
| Ubuntu | Wireshark, Grafana, InfluxDB |
| Kali Linux | Attack/testing platform |
| macOS (Apple Silicon) | UTM virtualization, SSH client |
| Windows 11 | RDP, management tools |

---

## Protocols Covered

- **MQTT** — IoT messaging protocol. Broker running on RPi, devices publish/subscribe to topics.
- **Modbus TCP/RTU** — Industrial protocol used in PLCs and SCADA systems. Simulated via pymodbus.
- **Zigbee** — Low-power mesh protocol for IoT devices. CC2531 as sniffer, Sonoff CC2652P as coordinator (pending).

---

## Setup

### 1. Flash Raspberry Pi OS

Use Raspberry Pi Imager (v2.0.7+):
- Device: Raspberry Pi 4
- OS: Raspberry Pi OS Lite (64-bit)
- Enable SSH, set hostname `rpi-iot`, configure Wi-Fi

### 2. Initial configuration

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y tcpdump tshark net-tools nmap iptables
```

### 3. MQTT broker

```bash
sudo apt install -y mosquitto mosquitto-clients
sudo systemctl enable mosquitto
sudo systemctl start mosquitto
```

### 4. Python environment

```bash
sudo apt install -y python3-pip python3-venv
python3 -m venv ~/lab-env
source ~/lab-env/bin/activate
pip install paho-mqtt pymodbus==3.6.9 pyserial
```

### 5. Verify adapters

```bash
lsusb
ls /dev/ttyUSB* /dev/ttyACM*
```

Expected output:
```
/dev/ttyACM0  → CC2531 Zigbee sniffer
/dev/ttyUSB0  → CH340 UART converter (Modbus RTU)
```

---

## Modbus TCP Simulation

Simulates a PLC with 4 sensor registers over TCP.

**Server** (`modbus_server.py`) — runs on RPi, exposes holding registers:

```python
# Registers: Temperatura=35, Presion=42, Humedad=18, Nivel=27
hr=ModbusSequentialDataBlock(0, [0, 35, 42, 18, 27])
```

**Client** (`modbus_client.py`) — reads sensor values:

```
Temperatura sala: 35
Presion linea: 42
Humedad: 18
Nivel deposito: 27
```

Run server:
```bash
python3 ~/lab-env/modbus_server.py
```

Run client (separate session):
```bash
python3 ~/lab-env/modbus_client.py
```

---

## Roadmap

- [x] RPi base setup (OS, SSH, networking tools)
- [x] Mosquitto MQTT broker
- [x] Modbus TCP simulation (server + client)
- [x] CH340 UART adapter — Modbus RTU ready
- [x] CC2531 connected — Zigbee sniffer mode
- [ ] Sonoff CC2652P — Zigbee coordinator
- [ ] Zigbee2MQTT installation and configuration
- [ ] IKEA TRÅDFRI device pairing
- [ ] CC2531 Zigbee traffic sniffing via Wireshark
- [ ] MikroTik VLAN segmentation
- [ ] Port mirroring → Kali passive capture
- [ ] Grafana + InfluxDB dashboard for MQTT/Modbus data
- [ ] Zigbee security analysis (key extraction, replay attacks)

---

## References

- [Zigbee2MQTT documentation](https://www.zigbee2mqtt.io)
- [pymodbus documentation](https://pymodbus.readthedocs.io)
- [Mosquitto documentation](https://mosquitto.org/documentation)
- [MikroTik RouterOS VLAN guide](https://help.mikrotik.com)
