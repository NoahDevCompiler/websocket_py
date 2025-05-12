import asyncio
import websockets
import os
import subprocess
import platform

def exec_command(command):
    if command == 'open_calc':
        if platform.system() == "Windows":
            subprocess.Popen('calc.exe')
    elif command == 'shutdown':
        if platform.system() == "Windows":
            os.system("shutdown /s /t 1")
        elif platform.system() == "Linux" or platform.system() == "Darwin":
            os.system("shutdown -h now")

async def handler(websocket):
    async for message in websocket:
        print(f"Empfangene Nachricht: {message}")
        exec_command(message)

async def main():
    async with websockets.serve(handler, "0.0.0.0", 10000):
        print("Se4ver Runnnig")
        await asyncio.Future()

if __name__ == '__main__':
    asyncio.run(main())

    