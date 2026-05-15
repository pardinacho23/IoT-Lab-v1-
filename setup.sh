#!/bin/bash
# IoT/OT Security Lab — Raspberry Pi Setup Script
# Run as: bash setup.sh

set -e

echo "=== IoT/OT Lab Setup ==="
echo ""

# System update
echo "[1/5] Updating system..."
sudo apt update && sudo apt upgrade -y

# Network and capture tools
echo "[2/5] Installing network tools..."
sudo apt install -y tcpdump tshark net-tools nmap iptables

# MQTT broker
echo "[3/5] Installing Mosquitto..."
sudo apt install -y mosquitto mosquitto-clients
sudo systemctl enable mosquitto
sudo systemctl start mosquitto

# Python environment
echo "[4/5] Setting up Python environment..."
sudo apt install -y python3-pip python3-venv
python3 -m venv ~/lab-env
source ~/lab-env/bin/activate
pip install paho-mqtt pymodbus==3.6.9 pyserial

# User permissions for serial ports
echo "[5/5] Configuring serial port permissions..."
sudo usermod -a -G dialout "$USER"

echo ""
echo "=== Setup complete ==="
echo ""
echo "Verify adapters:"
echo "  lsusb"
echo "  ls /dev/ttyUSB* /dev/ttyACM*"
echo ""
echo "Activate Python environment:"
echo "  source ~/lab-env/bin/activate"
echo ""
echo "Note: Log out and back in for serial port permissions to take effect."
