"""
Modbus TCP Client — IoT/OT Security Lab
Reads sensor holding registers from the Modbus TCP server.

Usage:
  source ~/lab-env/bin/activate
  python3 modbus_client.py

Expected output:
  Temperatura sala: 35
  Presion linea: 42
  Humedad: 18
  Nivel deposito: 27
"""

import asyncio
from pymodbus.client import AsyncModbusTcpClient


async def main():
    client = AsyncModbusTcpClient("localhost", port=5020)
    await client.connect()
    print("Connected to Modbus TCP server\n")

    labels = ["Temperatura sala", "Presion linea", "Humedad", "Nivel deposito"]

    for i, label in enumerate(labels):
        result = await client.read_holding_registers(i, 1, slave=1)
        if not result.isError():
            print(f"{label}: {result.registers[0]}")
        else:
            print(f"{label}: error — {result}")

    client.close()
    print("\nRead complete.")


if __name__ == "__main__":
    asyncio.run(main())
