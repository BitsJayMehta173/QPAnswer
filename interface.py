import tkinter as tk

# Sample array of words
words = ["apple", "banana", "cherry", "date", "elderberry"]

class WordDisplayApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Display")
        
        # Make the window full-screen
        # self.root.attributes("-fullscreen", True)
        
        # Exit full-screen on Escape key press
        # self.root.bind("<Escape>", self.exit_fullscreen)
        
        self.index = 0
        
        # Label to display the word
        self.word_label = tk.Label(root, text=words[self.index], font=('Helvetica', 36))
        self.word_label.pack(pady=40)
        
        # Entry to modify the word
        self.word_entry = tk.Entry(root, font=('Helvetica', 36), width=20)
        self.word_entry.pack(pady=20)
        self.word_entry.insert(0, words[self.index])
        
        # Update button to save the modified word
        self.update_button = tk.Button(root, text="Update", font=('Helvetica', 24), command=self.update_word)
        self.update_button.pack(pady=20)
        
        # Next button
        self.next_button = tk.Button(root, text="Next", font=('Helvetica', 24), command=self.show_next_word)
        self.next_button.pack(pady=20)
        
        # Copy to Clipboard button
        self.copy_button = tk.Button(root, text="Copy to Clipboard", font=('Helvetica', 24), command=self.copy_to_clipboard)
        self.copy_button.pack(pady=20)
        
    def show_next_word(self):
        # Save the current entry before moving to the next word
        self.update_word()
        
        self.index += 1
        
        if self.index < len(words):
            self.word_label.config(text=words[self.index])
            self.word_entry.delete(0, tk.END)
            self.word_entry.insert(0, words[self.index])
        else:
            self.word_label.config(text="End of list")
            self.next_button.config(state=tk.DISABLED)
            self.copy_button.config(state=tk.DISABLED)
            self.update_button.config(state=tk.DISABLED)
            self.word_entry.config(state=tk.DISABLED)
    
    def update_word(self):
        # Update the current word in the array with the value in the entry widget
        words[self.index] = self.word_entry.get()
        self.word_label.config(text=words[self.index])
    
    def copy_to_clipboard(self):
        current_word = self.word_label.cget("text")
        self.root.clipboard_clear()  # Clear the clipboard
        self.root.clipboard_append(current_word)  # Append the current word to the clipboard
        self.root.update()  # This is necessary to make sure the clipboard is updated

    # def exit_fullscreen(self, event=None):
    #     # Exit full-screen mode
    #     self.root.attributes("-fullscreen", False)

# Create the main window
root = tk.Tk()

# Create the WordDisplayApp instance
app = WordDisplayApp(root)

# Start the Tkinter event loop
root.mainloop()
