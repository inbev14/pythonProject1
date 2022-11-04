import tkinter as tk

from cross_game_myself.settings.game_settings import FONT


class EnterNameWin(tk.Tk):
    def __init__(self):
        super(EnterNameWin, self).__init__()
        self.login = 'New Player'
        self.title('Player name')
        self.geometry('460x200+700+290')
        self.attributes('-topmost', True)

        self.login_label = tk.Label(self, font=FONT, text='Enter your login')
        self.login_entry = tk.Entry(self, font=FONT, width=20, justify=tk.CENTER)
        self.login_button = tk.Button(self, font=FONT, text='Ok', command=self.set_login)
   
        self.login_label.grid(row=0, column=1, padx=15)
        self.login_entry.grid(row=1, column=1, padx=70, pady=20)
        self.login_button.grid(row=2, column=1, padx=15)
        
        self.mainloop()
        
    def set_login(self):
        self.login = self.login_entry.get()
        self.destroy()
        