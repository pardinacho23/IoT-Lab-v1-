On this Repo I am going to go through all the basics / intermediate / advanced protocols, software, hardware & tricks about OT applied Cybersecurity which is already vital for a country's indepence.

Technologies that I will go through:
• OS: Ubuntu (Analyser), Windows 11 (Victim), Kali Linux (Attacker)
• MQTT · Zigbee · Wireshark / Laboratorio inicial 
• Wazuh · ELK · Zeek /  Detección de amenazas
• IEC 62443 · Modbus · SCADA · NIS2 / Arquitectura de planta solar
• Raspberry Pi / Servidor Local

# IoT/OT Security Lab

Hands-on cybersecurity lab focused on IoT/OT protocols and threat 
detection in critical infrastructure environments, with a focus on 
solar energy architecture.

## Lab Architecture

| Machine | Role | OS |
|---|---|---|
| Ubuntu | Traffic analyzer / SIEM agent | Ubuntu 24 |
| Kali Linux | Attacker simulation | Kali |
| Windows 11 | Victim node | Windows 11 |
| Raspberry Pi 4 | IoT broker / central node | Raspberry Pi OS |

## Hardware
- Zigbee USB dongle CC2531
- USB-UART converter CH340G
- [Router / Tuya plug — incoming]

## Findings

### 01 — MQTT Plaintext Transmission
**Protocol:** MQTT · **Tool:** Wireshark · **Date:** May 2026

Captured MQTT traffic on loopback interface showing solar inverter 
data transmitted in plaintext on port 1883.

- Topic visible: `solar/inversor/01/potencia`  
- Payload visible: `3450W`
- No authentication required to connect or publish

**Impact:** Any attacker with network access can read and inject 
data into solar inverter topics, violating NIS2 requirements for 
critical infrastructure operators.

**Mitigation:** TLS on port 8883 + authentication + ACLs per topic.

[Screenshot](findings/01-mqtt-plaintext/wireshark-capture.png)

## Tools Used
Wireshark · Mosquitto · MQTT · Linux · [Wazuh — in progress]

## Status
🟢 Phase 1 in progress — MQTT analysis complete
⬜ Phase 2 — Wazuh/SIEM setup
⬜ Phase 3 — OT/Modbus/SCADA
⬜ Phase 4 — CompTIA Security+




