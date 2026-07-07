print('Програмування. Частина 2. Лаботаротна робота №8, Коломоєць Ольги ФБ-44 Варіант 9')
import tkinter as tk

class NumberApp:
    def __init__(self, master):
        self.master = master
        self.value = 0

        self.label = tk.Label(master, text=str(self.value), font=("Arial", 20))
        self.label.pack()

        self.inc_button = tk.Button(master, text="Inc", command=self.increment)
        self.inc_button.pack()

        self.dec_button = tk.Button(master, text="Dec", command=self.decrement)
        self.dec_button.pack()

        self.clear_button = tk.Button(master, text="Clear", command=self.clear)
        self.clear_button.pack()

        self.goodbye_button = tk.Button(master, text="Goodbye", command=master.destroy)
        self.goodbye_button.pack()

    def increment(self):
        if self.value < 100:
            self.value += 1
            self.label.config(text=str(self.value))

    def decrement(self):
        if self.value > -100:
            self.value -= 1
            self.label.config(text=str(self.value))

    def clear(self):
        self.value = 0
        self.label.config(text=str(self.value))

class DNAApp:
    def __init__(self, master):
        self.master = master

        self.text = tk.Text(master, height=10, width=50)
        self.text.pack()

        self.count_button = tk.Button(master, text="Count", command=self.count_dna)
        self.count_button.pack()

        self.clear_button = tk.Button(master, text="Clear", command=self.clear)
        self.clear_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.goodbye_button = tk.Button(master, text="Goodbye", command=master.destroy)
        self.goodbye_button.pack()

    def count_dna(self):
        sequence = self.text.get("1.0", tk.END).upper()
        a_count = sequence.count("A")
        t_count = sequence.count("T")
        c_count = sequence.count("C")
        g_count = sequence.count("G")

        self.result_label.config(text=f"Num As: {a_count} Num Ts: {t_count} Num Cs: {c_count} Num Gs: {g_count}")

    def clear(self):
        self.text.delete("1.0", tk.END)
        self.result_label.config(text="")

class MainApp:
    def __init__(self, master):
        self.master = master
        master.title("Number and DNA Counter")

        self.number_app = NumberApp(master)
        self.separator = tk.Label(master, text="---------------------------")
        self.separator.pack()
        self.dna_app = DNAApp(master)

root = tk.Tk()
app = MainApp(root)
root.mainloop()
