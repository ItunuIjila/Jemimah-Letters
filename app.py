#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 17 15:25:57 2025

@author: ogunjosam
"""

import tkinter as tk
from tkinter import ttk
import random
import string
import time

class RandomDisplayApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Jemimah Letters and Alphabets App")
        self.root.geometry("600x500")
        self.root.configure(bg="#f0f0f0")
        
        # Variables
        self.display_numbers = tk.BooleanVar(value=True)
        self.display_letters = tk.BooleanVar(value=True)
        self.num_min = tk.IntVar(value=0)
        self.num_max = tk.IntVar(value=100)
        self.letter_case = tk.StringVar(value="both")
        self.display_speed = tk.DoubleVar(value=1.0)  # seconds
        self.is_running = False
        self.current_display = tk.StringVar(value="")
        
        # Create UI elements
        self.create_widgets()
        
    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Display frame
        display_frame = ttk.Frame(main_frame, padding="10")
        display_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Display label
        self.display_label = ttk.Label(display_frame, textvariable=self.current_display, 
                                      font=("Arial", 72, "bold"), anchor="center")
        self.display_label.pack(fill=tk.BOTH, expand=True)
        
        # Controls frame
        controls_frame = ttk.LabelFrame(main_frame, text="Settings", padding="10")
        controls_frame.pack(fill=tk.X, pady=10)
        
        # Content type frame
        content_frame = ttk.Frame(controls_frame)
        content_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(content_frame, text="Display Content:").pack(side=tk.LEFT, padx=5)
        ttk.Checkbutton(content_frame, text="Numbers", variable=self.display_numbers).pack(side=tk.LEFT, padx=10)
        ttk.Checkbutton(content_frame, text="Letters", variable=self.display_letters).pack(side=tk.LEFT, padx=10)
        
        # Number range frame
        number_frame = ttk.Frame(controls_frame)
        number_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(number_frame, text="Number Range:").pack(side=tk.LEFT, padx=5)
        ttk.Label(number_frame, text="Min:").pack(side=tk.LEFT, padx=5)
        ttk.Spinbox(number_frame, from_=-1000, to=1000, textvariable=self.num_min, width=5).pack(side=tk.LEFT, padx=5)
        ttk.Label(number_frame, text="Max:").pack(side=tk.LEFT, padx=5)
        ttk.Spinbox(number_frame, from_=-1000, to=1000, textvariable=self.num_max, width=5).pack(side=tk.LEFT, padx=5)
        
        # Letter case frame
        letter_frame = ttk.Frame(controls_frame)
        letter_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(letter_frame, text="Letter Case:").pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(letter_frame, text="Uppercase", variable=self.letter_case, value="upper").pack(side=tk.LEFT, padx=10)
        ttk.Radiobutton(letter_frame, text="Lowercase", variable=self.letter_case, value="lower").pack(side=tk.LEFT, padx=10)
        ttk.Radiobutton(letter_frame, text="Both", variable=self.letter_case, value="both").pack(side=tk.LEFT, padx=10)
        
        # Speed frame
        speed_frame = ttk.Frame(controls_frame)
        speed_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(speed_frame, text="Display Speed (seconds):").pack(side=tk.LEFT, padx=5)
        ttk.Scale(speed_frame, from_=0.1, to=5.0, orient="horizontal", variable=self.display_speed, 
                 length=200).pack(side=tk.LEFT, padx=5, expand=True)
        speed_value = ttk.Label(speed_frame, text="1.0")
        speed_value.pack(side=tk.LEFT, padx=5)
        
        # Update speed label when slider moves
        def update_speed_label(*args):
            speed_value.config(text=f"{self.display_speed.get():.1f}")
        self.display_speed.trace_add("write", update_speed_label)
        
        # Button frame
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=10)
        
        self.start_button = ttk.Button(button_frame, text="Start", command=self.start_display)
        self.start_button.pack(side=tk.LEFT, padx=5)
        
        self.stop_button = ttk.Button(button_frame, text="Stop", command=self.stop_display, state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT, padx=5)
        
        self.manual_button = ttk.Button(button_frame, text="Generate Single", command=self.generate_single)
        self.manual_button.pack(side=tk.LEFT, padx=5)
        
        # Status frame
        status_frame = ttk.Frame(main_frame)
        status_frame.pack(fill=tk.X, pady=5)
        
        self.status_label = ttk.Label(status_frame, text="Ready", anchor="w")
        self.status_label.pack(fill=tk.X)
    
    def generate_random_content(self):
        """Generate random content based on settings"""
        # Check if at least one display option is selected
        if not self.display_numbers.get() and not self.display_letters.get():
            self.current_display.set("⚠️")
            self.status_label.config(text="Error: Select at least one display option")
            return
        
        content_options = []
        
        # Add numbers if selected
        if self.display_numbers.get():
            # Ensure min is less than max
            min_val = min(self.num_min.get(), self.num_max.get())
            max_val = max(self.num_min.get(), self.num_max.get())
            content_options.append(str(random.randint(min_val, max_val)))
        
        # Add letters if selected
        if self.display_letters.get():
            if self.letter_case.get() == "upper":
                content_options.append(random.choice(string.ascii_uppercase))
            elif self.letter_case.get() == "lower":
                content_options.append(random.choice(string.ascii_lowercase))
            else:  # both
                content_options.append(random.choice(string.ascii_letters))
        
        # Choose one from the possible options
        return random.choice(content_options)
    
    def start_display(self):
        """Start automatic display of random content"""
        self.is_running = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.status_label.config(text="Running...")
        self.update_display()
    
    def stop_display(self):
        """Stop automatic display"""
        self.is_running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.status_label.config(text="Stopped")
    
    def update_display(self):
        """Update display with new random content"""
        if not self.is_running:
            return
        
        content = self.generate_random_content()
        self.current_display.set(content)
        
        # Schedule next update
        self.root.after(int(self.display_speed.get() * 1000), self.update_display)
    
    def generate_single(self):
        """Generate a single random item"""
        content = self.generate_random_content()
        self.current_display.set(content)
        self.status_label.config(text="Generated single item")


if __name__ == "__main__":
    root = tk.Tk()
    app = RandomDisplayApp(root)
    root.mainloop()
