from tkinter import *
from tkinter import messagebox
import time
import random
from functions import load_user_data, save_user_data
from sample_texts import sample_texts


class TypingSpeedApp:
    def __init__(self, root):
        self.root = root
        self.root.title('TYPING SPEED TEST')
        self.user_data = load_user_data()
        self.current_user = None
        self.start_time = None
        self.sample_text = ''
        self.sample_words = []
        self.typed_words = []

        # Widgets
        self.username_label = None
        self.username_entry = None
        self.login_button = None
        self.new_user_button = None
        self.level_label = None
        self.level_var = None
        self.level_menu = None
        self.sample_text_label = None
        self.sample_text_content = None
        self.sample_text = None
        self.typing_area_text = None
        self.start_button = None
        self.stop_button = None
        self.high_score_label = None

        # UI Components
        self.create_widgets()

    def create_widgets(self):
        # User Login / Signup
        self.username_label = Label(self.root, text='Enter Username: ')
        self.username_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        self.username_entry = Entry(self.root)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10, sticky='w')

        self.login_button = Button(self.root, text='Login', command=self.login_user)
        self.login_button.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        self.new_user_button = Button(self.root, text='New User', command=self.new_user)
        self.new_user_button.grid(row=1, column=1, padx=10, pady=10, sticky='w')

        # Level Selection
        self.level_label = Label(self.root, text='Select Level: ')
        self.level_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.level_var = StringVar(value='EASY')
        self.level_menu = OptionMenu(self.root, self.level_var, *sample_texts.keys())
        self.level_menu.grid(row=2, column=1, padx=10, pady=10, sticky='w')

        # Sample Text Display
        self.sample_text_label = Label(self.root, text='Sample Text:')
        self.sample_text_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='w')

        self.sample_text = Label(self.root, text='', wraplength=500, justify='left')
        self.sample_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky='w')

        # Typing Area
        self.typing_area_text = Text(self.root, height=5, width=60, wrap='word')
        self.typing_area_text.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
        self.typing_area_text.bind('<KeyRelease>', self.check_typing)

        # Buttons
        self.start_button = Button(self.root, text='Start', command=self.start_test)
        self.start_button.grid(row=6, column=0, padx=10, pady=10, sticky='w')

        self.stop_button = Button(self.root, text='Stop', state='disabled', command=self.stop_test)
        self.stop_button.grid(row=6, column=1, padx=10, pady=10, sticky='w')

        # High Score
        self.high_score_label = Label(self.root, text='High Score: N/A')
        self.high_score_label.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky='w')

    def login_user(self):
        username = self.username_entry.get().strip()
        if username in self.user_data:
            self.current_user = username
            self.high_score_label.config(text=f'High Score: {self.user_data[username]} WPM')
            messagebox.showinfo('Welcome back!', f'Welcome back, {username}!!')
        else:
            messagebox.showerror('Error', 'User not found, please create a new user!')

    def new_user(self):
        username = self.username_entry.get().strip()
        if username and username not in self.user_data:
            self.user_data[username] = 0
            save_user_data(self.user_data)
            self.current_user = username
            self.high_score_label.config(text='High Score: N/A')
            messagebox.showinfo('Success', f'User {username} created successfully!')
        else:
            messagebox.showerror('Error', 'Invalid username or user already exists!')

    def start_test(self):
        if not self.current_user:
            messagebox.showerror('Error', 'Please login or create a new user first!')
            return
        level = self.level_var.get()
        self.sample_text_content = random.choice(sample_texts[level])
        self.sample_words = self.sample_text_content.split()
        self.sample_text.config(text=self.sample_text_content)
        self.typing_area_text.delete(1.0, END)
        self.typed_words = []
        self.start_time = time.time()
        self.start_button.config(state='disabled')
        self.stop_button.config(state='normal')

    def check_typing(self, event):
        typed_text = self.typing_area_text.get(1.0, END).strip()
        self.typed_words = typed_text.split()
        self.typing_area_text.tag_remove('correct', 1.0, END)
        self.typing_area_text.tag_remove('incorrect', 1.0, END)

        for i, word in enumerate(self.typed_words):
            if i < len(self.sample_words):
                start_index = f"1.0 + {len(' '.join(self.typed_words[:i]))}c"
                end_index = f"1.0 + {len(' '.join(self.typed_words[:i + 1]))}c"

                if word == self.sample_words[i]:
                    self.typing_area_text.tag_add('correct', start_index, end_index)
                else:
                    self.typing_area_text.tag_add('incorrect', start_index, end_index)

        self.typing_area_text.tag_config('correct', foreground='green')
        self.typing_area_text.tag_config('incorrect', foreground='red')

    def stop_test(self):
        if not self.start_time:
            return

        end_time = time.time()
        elapsed_time = end_time - self.start_time
        word_count = len([w for i, w in enumerate(self.typed_words) if i < len(self.sample_words) and w ==
                         self.sample_words[i]])
        wpm = round(word_count / (elapsed_time / 60))

        self.start_time = None
        self.start_button.config(state='normal')
        self.stop_button.config(state='disabled')

        messagebox.showinfo('Typing Speed', f'Your typing speed is {wpm} WPM.')

        # Update High Score
        if self.user_data[self.current_user] < wpm:
            self.user_data[self.current_user] = wpm
            save_user_data(self.user_data)
            self.high_score_label.config(text=f'High Score: {wpm} WPM')
            messagebox.showinfo('New High Score!', 'Congratulations on setting a new high score!')
