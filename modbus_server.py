"""
Modbus TCP Server — IoT/OT Security Lab
Simulates a PLC with 4 sensor holding registers.

Registers:
  Address 0: Temperatura sala  (35)
  Address 1: Presion linea     (42)
  Address 2: Humedad           (18)
  Address 3: Nivel deposito    (27)

Usage:
  source ~/lab-env/bin/activate
  python3 modbus_server.py
"""

import asyncio
from pymodbus.server import StartAsyncTcpServer
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.datastore import ModbusSequentialDataBlock


async def main():
    store = ModbusSlaveContext(
        hr=ModbusSequentialDataBlock(0, [0, 35, 42, 18, 27])
    )
    context = ModbusServerContext(slaves=store, single=True)

    print("Modbus TCP server started on 0.0.0.0:5020")
    print("Registers: Temperatura=35 | Presion=42 | Humedad=18 | Nivel=27")

    await StartAsyncTcpServer(context=context, address=("0.0.0.0", 5020))


if __name__ == "__main__":
    asyncio.run(main())
