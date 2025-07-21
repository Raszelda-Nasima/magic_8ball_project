import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import random

# Configure CustomTkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class Magic8Ball:
    def __init__(self):
        # Traditional 8-ball responses
        self.responses = [
            "It is certain", "Reply hazy, try again", "Don't count on it",
            "It is decidedly so", "Ask again later", "My reply is no",
            "Without a doubt", "Better not tell you now", "My sources say no",
            "Yes definitely", "Cannot predict now", "Outlook not so good",
            "You may rely on it", "Concentrate and ask again", "Very doubtful",
            "As I see it, yes", "Most likely", "Outlook good",
            "Yes", "Signs point to yes"
        ]
        
        self.setup_gui()
    
    def setup_gui(self):
        # Main window
        self.root = ctk.CTk()
        self.root.title("🎱 Magic 8-Ball")
        self.root.geometry("400x500")
        
        # Main frame
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Title
        self.title_label = ctk.CTkLabel(
            self.main_frame,
            text="🎱 Magic 8-Ball",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        self.title_label.pack(pady=20)
        
        # Question input
        self.question_label = ctk.CTkLabel(
            self.main_frame,
            text="Ask your question:",
            font=ctk.CTkFont(size=14)
        )
        self.question_label.pack(pady=(10, 5))
        
        self.question_entry = ctk.CTkTextbox(
            self.main_frame,
            height=60,
            font=ctk.CTkFont(size=12)
        )
        self.question_entry.pack(pady=5, padx=20, fill="x")
        
        # Answer display
        self.answer_label = ctk.CTkLabel(
            self.main_frame,
            text="Ask me anything!",
            font=ctk.CTkFont(size=14),
            wraplength=300
        )
        self.answer_label.pack(pady=30)
        
        # Shake button
        self.shake_button = ctk.CTkButton(
            self.main_frame,
            text="🎱 Shake!",
            font=ctk.CTkFont(size=16, weight="bold"),
            height=40,
            command=self.shake_ball
        )
        self.shake_button.pack(pady=20)
    
    def shake_ball(self):
        question = self.question_entry.get("1.0", "end-1c").strip()
        
        if not question:
            messagebox.showwarning("No Question", "Please ask a question first!")
            return
        
        # Get random response
        answer = random.choice(self.responses)
        self.answer_label.configure(text=answer)
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = Magic8Ball()
    game.run()