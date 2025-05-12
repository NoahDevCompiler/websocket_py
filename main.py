import asyncio
import websockets
import os
import subprocess
import platform
import ssl

def exec_command(command):
    if command == 'open_calc':
        if platform.system() == "Windows":
            subprocess.Popen('calc.exe')
    elif command == 'shutdown':
        if platform.system() == "Windows":
            os.system("shutdown /s /t 1")
        elif platform.system() == "Linux" or platform.system() == "Darwin":
            os.system("shutdown -h now")

async def handler(websocket, path):
    async for message in websocket:
        print(f"Empfangene Nachricht: {message}")
        exec_command(message)

async def main():
    ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ssl_context.load_cert_chain(certfile="server.crt", keyfile="private.pem")

    server = await websockets.serve(handler, "0.0.0.0", 10000, ssl=ssl_context)
    print("Server läuft auf wss://localhost:10000")
    await server.wait_closed()

if __name__ == '__main__':
    asyncio.run(main())
