import pyttsx3
import time
import os

file_path = "input.txt"

while True:
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read().strip()
        if text:
            try:
                engine = pyttsx3.init()
                engine.setProperty('rate', 150)
                engine.setProperty('volume', 1.0)
                voices = engine.getProperty('voices')
                engine.setProperty('voice', voices[1].id)  # Use voices[0] for male
                engine.say(text)
                engine.runAndWait()
                engine.stop()
                del engine
                print(f"🔊 Robot spoke: {text}")
                # Clear file so it's ready for next input
                open(file_path, "w").close()
            except Exception as e:
                print("❌ Error:", e)
    time.sleep(2)
