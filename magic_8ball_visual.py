import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import random

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class Magic8Ball:
    def __init__(self):
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
        self.root = ctk.CTk()
        self.root.title("🎱 Magic 8-Ball")
        self.root.geometry("500x650")
        
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Title
        self.title_label = ctk.CTkLabel(
            self.main_frame,
            text="🎱 Magic 8-Ball",
            font=ctk.CTkFont(size=28, weight="bold")
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
            height=70,
            font=ctk.CTkFont(size=12)
        )
        self.question_entry.pack(pady=5, padx=30, fill="x")
        
        # 8-Ball visual
        self.create_8ball_visual()
        
        # Shake button
        self.shake_button = ctk.CTkButton(
            self.main_frame,
            text="🎱 Shake the 8-Ball!",
            font=ctk.CTkFont(size=16, weight="bold"),
            height=50,
            command=self.shake_ball
        )
        self.shake_button.pack(pady=20)
    
    def create_8ball_visual(self):
        # Ball frame
        self.ball_frame = ctk.CTkFrame(
            self.main_frame, 
            fg_color="black", 
            corner_radius=125
        )
        self.ball_frame.pack(pady=20)
        
        # Canvas for drawing
        self.ball_canvas = tk.Canvas(
            self.ball_frame,
            width=250,
            height=250,
            bg="black",
            highlightthickness=0
        )
        self.ball_canvas.pack(padx=10, pady=10)
        
        # Draw the 8-ball
        self.draw_8ball()
        
        # Answer overlay
        self.answer_frame = ctk.CTkFrame(
            self.ball_frame, 
            fg_color="navy", 
            corner_radius=60
        )
        self.answer_frame.place(x=60, y=80)
        
        self.answer_label = ctk.CTkLabel(
            self.answer_frame,
            text="Shake me!",
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color="white",
            wraplength=120
        )
        self.answer_label.pack(padx=15, pady=30)
    
    def draw_8ball(self):
        # Main black circle
        self.ball_canvas.create_oval(
            10, 10, 240, 240, 
            fill="black", 
            outline="gray", 
            width=2
        )
        
        # Highlight
        self.ball_canvas.create_oval(
            40, 40, 90, 90, 
            fill="gray30", 
            outline=""
        )
        
        # Number circle
        self.ball_canvas.create_oval(
            100, 30, 140, 70, 
            fill="white", 
            outline="black", 
            width=2
        )
        
        # Number 8
        self.ball_canvas.create_text(
            120, 50, 
            text="8", 
            font=("Arial", 18, "bold"), 
            fill="black"
        )
    
    def shake_ball(self):
        question = self.question_entry.get("1.0", "end-1c").strip()
        
        if not question:
            messagebox.showwarning("No Question", "Please ask a question first!")
            return
        
        # Show loading
        self.answer_label.configure(text="...")
        self.root.update()
        self.root.after(1000)  # 1 second delay
        
        # Get and show answer
        answer = random.choice(self.responses)
        self.answer_label.configure(text=answer)
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = Magic8Ball()
    game.run()