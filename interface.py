import tkinter as tk
import pickle

# Load the array from the file
with open('words.pkl', 'rb') as file:
    words = pickle.load(file)

print(words)

class WordDisplayApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Display")
        
        self.index = 0
        # Text Display for the current idex
        self.word_label = tk.Label(root, text=words[self.index], font=('Helvetica', 20))
        self.word_label.pack(pady=20)
        
        # Text Editor widget in case there is need for correcting the questions before sending
        self.word_text = tk.Text(root, font=('Helvetica', 20), width=60, height=7)
        self.word_text.pack(pady=10)
        self.word_text.insert(tk.END, words[self.index])
        
        # Update button to save the modified word
        self.update_button = tk.Button(root, text="Update", font=('Helvetica', 17), command=self.update_word)
        self.update_button.pack(pady=10)
        
        # Next button
        self.next_button = tk.Button(root, text="Next", font=('Helvetica', 17), command=self.show_next_word)
        self.next_button.pack(pady=10)
        
        # Copy to Clipboard button
        self.copy_button = tk.Button(root, text="Copy to Clipboard", font=('Helvetica', 17), command=self.copy_to_clipboard)
        self.copy_button.pack(pady=10)
        
    def show_next_word(self):
        # Save the current text before moving to the next word
        self.update_word()
        
        self.index += 1
        
        if self.index < len(words):
            self.word_label.config(text=words[self.index])
            self.word_text.delete(1.0, tk.END)  # Clear the text widget
            self.word_text.insert(tk.END, words[self.index])
        else:
            self.word_label.config(text="End of list")
            self.next_button.config(state=tk.DISABLED)
            self.copy_button.config(state=tk.DISABLED)
            self.update_button.config(state=tk.DISABLED)
            self.word_text.config(state=tk.DISABLED)
    
    def update_word(self):
        # Update the current word in the array with the value in the text widget
        words[self.index] = self.word_text.get(1.0, tk.END).strip()
        self.word_label.config(text=words[self.index])
    
    def copy_to_clipboard(self):
        current_word = self.word_text.get(1.0, tk.END).strip()
        self.root.clipboard_clear()  # Clear the clipboard
        self.root.clipboard_append(current_word)  # Append the current word to the clipboard
        self.root.update()  # This is necessary to make sure the clipboard is updated


root = tk.Tk()


app = WordDisplayApp(root)

root.mainloop()
