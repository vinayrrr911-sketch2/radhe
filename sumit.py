import os
import google.generativeai as genai
from gtts import gTTS
import tkinter as tk
from tkinter import scrolledtext

# API Setup
genai.configure(api_key="AIzaSyCZQe1rFLIWdrvgApuqcUGb6ggBy0Nbyyw")
model = genai.GenerativeModel('models/gemini-2.5-flash')

def speak(text):
    # Faltu symbols hatana
    clean_text = text.replace('*', '').replace('#', '').strip()
    try:
        tts = gTTS(text=clean_text, lang='hi')
        tts.save("speech.mp3")
        os.system("mpg123 -q -f 30000 speech.mp3")
    except:
        pass

def get_response():
    user_input = entry.get()
    if user_input.strip() == "": return
    
    chat_history.insert(tk.END, f"Aap: {user_input}\n")
    entry.delete(0, tk.END)
    
    try:
        # Sumit ka dimaag
        response = model.generate_content(f"Tum Sumit ho, ek smart AI. Hindi mein jawab do: {user_input}")
        ans = response.text
        chat_history.insert(tk.END, f"Sumit: {ans}\n\n")
        chat_history.see(tk.END)
        speak(ans)
    except Exception as e:
        chat_history.insert(tk.END, f"Error: {e}\n")
     
# --- Safed Screen (GUI) Ka Setup ---
root = tk.Tk()
root.title("Sumit AI - Gemini 2.5 Flash")
root.geometry("500x600")
root.configure(bg="white")

# Chat Window
chat_history = scrolledtext.ScrolledText(root, width=50, height=20, bg="white", fg="black", font=("Arial", 12))
chat_history.pack(padx=10, pady=10)

# Input Box
entry = tk.Entry(root, width=40, font=("Arial", 14))
entry.pack(padx=10, pady=10)
entry.bind("<Return>", lambda x: get_response()) # Enter dabane par chale

# Send Button
send_btn = tk.Button(root, text="mai Sumit hu", command=get_response, bg="blue", fg="white")
send_btn.pack(pady=5)

root.mainloop()
