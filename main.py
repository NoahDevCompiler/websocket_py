import asyncio
import websockets
import os
import subprocess
import platform
from PIL import ImageGrab
import pyautogui
import time
import json
import random
import ctypes
import win32gui
import win32con


def exec_command(data):
    command = data.get("action")
    starttime = data.get("time", 0)

    if command == 'fl':
        fl_path = r"C:\Program Files (x86)\Image-Line\FL Studio 20\FL64.exe"
        if platform.system() == "Windows":
            subprocess.run([fl_path], check=True)
    elif command == 'shutdown':
        if platform.system() == "Windows":
            os.system("shutdown /s /t 1")
    elif command == 'chrome':
        chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        if platform.system() == "Windows":
            subprocess.run([chrome_path], check=True)
    elif command == 'screenshot':
        img = ImageGrab.grab()
        img.save("screenshot.png")
    elif command == 'autoclicker':
        start = time.time()
        end = start + starttime
        while time.time() < end:
            pyautogui.moveTo(random.randint(0, 1080), random.randint(0, 600))  
            pyautogui.moveTo(None, random.randint(0, 800)) 
            pyautogui.moveTo(600, None)
            time.sleep(1)
    elif command == 'lock':
        ctypes.windll.user32.LockWorkStation()
    elif command == 'fixate':
        hwnd = win32gui.FindWindow("Notepad", None)
        win32gui.SetWindowPos(
        hwnd,
        win32con.HWND_TOPMOST,
        0, 0, 0, 0,
        win32con.SWP_NOMOVE | win32con.SWP_NOSIZE
)

    

async def handler(websocket):
    print("neue Verbindung")
    async for message in websocket:
        print(f"Empfangene Nachricht: {message}")
        try:
            data = json.loads(message)
            exec_command(data)
        except json.JSONDecodeError:
            print("Ungültiges JSON empfangen.")
        except Exception as e:
            print(f"❌ Fehler beim Verarbeiten der Nachricht: {e}")

async def main():
    server = await websockets.serve(handler, "0.0.0.0", 10000)
    print("Server läuft auf wss://localhost:10000")
    await asyncio.Future()

if __name__ == '__main__':
    asyncio.run(main())
