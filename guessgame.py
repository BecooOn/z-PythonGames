import tkinter as tk
import random

def check_guess():
    user_guess = int(entry.get())
    if user_guess == secret_number:
        result_label.config(text="Tebrikler! Doğru Tahmin ettiniz!")
    elif user_guess < secret_number:
        result_label.config(text="Daha büyük bir sayı girin.")
    else:
        result_label.config(text="Daha küçük bir sayı girin.")

def start_game():
    global secret_number
    secret_number = random.randint(1, 100)
    result_label.config(text="")
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Sayı Tahmin Oyunu")

secret_number = 0

guess_label = tk.Label(root, text="Tahmininizi girin (1-100):")
guess_label.pack()

entry = tk.Entry(root)
entry.pack()

check_button = tk.Button(root, text="Tahmin Et", command=check_guess)
check_button.pack()

result_label = tk.Label(root, text="", fg="green")
result_label.pack()

start_button = tk.Button(root, text="Oyunu Başlat", command=start_game)
start_button.pack()

root.mainloop()