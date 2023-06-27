import tkinter as tk
from tkinter import ttk
import random
import time

window = tk.Tk()
window.title("Zgadnij TĘ liczbę")

is_dark_mode = False

def toggle_dark_mode():
    global is_dark_mode
    is_dark_mode = not is_dark_mode

    if is_dark_mode:
        window.configure(bg="#333333")
        copyright_label.configure(fg="white", bg="#333333")
    else:
        window.configure(bg="#F0F0F0")
        copyright_label.configure(fg="gray", bg="#F0F0F0")

copyright_label = tk.Label(
    window,
    text="© 2023 Szymon Wasik.",
    font=("Montserrat", 10),
)
if is_dark_mode:
    copyright_label.configure(fg="white", bg="#333333")
else:
    copyright_label.configure(fg="gray", bg="#F0F0F0")
    
copyright_label.pack(side="bottom")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_width = int(screen_width * 0.8)
window_height = int(screen_height * 0.8)

position_x = int((screen_width - window_width) / 2)
position_y = int((screen_height - window_height) / 2)

window.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

is_dark_mode = False

def toggle_dark_mode():
    global is_dark_mode
    is_dark_mode = not is_dark_mode

    if is_dark_mode:
        window.configure(bg="#333333")
        game_frame.configure(bg="#333333")
        title_label.configure(fg="white", bg="#333333")
        guess_label.configure(fg="white", bg="#333333")
        attempts_label.configure(fg="white", bg="#333333")
        hint_label.configure(fg="white", bg="#333333")
        result_label.configure(fg="white", bg="#333333")
        timer_label.configure(fg="white", bg="#333333")
        dark_mode_button.configure(text="Tryb jasny", bg="#4CAF50", fg="white")
    else:
        window.configure(bg="#F0F0F0")
        game_frame.configure(bg="#F0F0F0")
        title_label.configure(fg="black", bg="#F0F0F0")
        guess_label.configure(fg="black", bg="#F0F0F0")
        attempts_label.configure(fg="black", bg="#F0F0F0")
        hint_label.configure(fg="black", bg="#F0F0F0")
        result_label.configure(fg="black", bg="#F0F0F0")
        timer_label.configure(fg="black", bg="#F0F0F0")
        dark_mode_button.configure(text="Tryb ciemny", bg="#4CAF50", fg="white")

window.configure(bg="#F0F0F0")

game_frame = tk.Frame(window, bg="#F0F0F0", bd=5)
game_frame.pack(expand=True)

title_label = tk.Label(game_frame, text="Zgadnij TĘ liczbę", font=("Montserrat", 24), fg="black", bg="#F0F0F0")
title_label.pack(pady=(10, 20))

guess_label = tk.Label(game_frame, text="Wybierz liczbę od 1 do 100:", font=("Montserrat", 16), fg="black", bg="#F0F0F0")
guess_label.pack()

guess_input = tk.Entry(game_frame, font=("Montserrat", 16))
guess_input.pack(pady=10)

attempts_label = tk.Label(game_frame, text="Liczba prób: 0", font=("Montserrat", 14), fg="black", bg="#F0F0F0")
attempts_label.pack()

hint_label = tk.Label(game_frame, text="", font=("Montserrat", 14), fg="black", bg="#F0F0F0")
hint_label.pack()

result_label = tk.Label(game_frame, text="", font=("Montserrat", 18), fg="black", bg="#F0F0F0")
result_label.pack(pady=20)

timer_label = tk.Label(game_frame, text="", font=("Montserrat", 14), fg="black", bg="#F0F0F0")
timer_label.pack()

dark_mode_button = tk.Button(game_frame, text="Tryb ciemny", font=("Montserrat", 12), bg="#4CAF50", fg="white", command=toggle_dark_mode)
dark_mode_button.pack(pady=10)

def submit_guess():
    user_input = guess_input.get()

    if not user_input:
        result_label.config(text="Podaj liczbę od 1 do 100!")
        hint_label.config(text="")
        return

    try:
        user_guess = int(user_input)
    except ValueError:
        result_label.config(text="Nieprawidłowy format liczby!")
        hint_label.config(text="")
        return

    if user_guess < 1 or user_guess > 100:
        result_label.config(text="Podaj liczbę od 1 do 100!")
        hint_label.config(text="")
        return

    global attempts
    attempts += 1

    if attempts == 1:
        global start_time
        start_time = time.time()
        update_timer()

    if user_guess == secret_number:
        end_time = time.time()
        total_time_in_seconds = end_time - start_time
        minutes = int(total_time_in_seconds / 60)
        seconds = int(total_time_in_seconds % 60)
        hours = int(minutes / 60)
        minutes = minutes % 60
        result_label.config(text=f"Brawo! Udało Ci się zgadnąć liczbę {secret_number} po {attempts} próbach!")
        result_label.config(text=result_label.cget("text") + f"\nCzas: {hours} godz. {minutes} min. {seconds} sek.")
        submit_button.config(state="disabled")
        guess_input.config(state="disabled")
        hint_label.config(text="")
    elif user_guess < secret_number:
        result_label.config(text="Za niska. Spróbuj ponownie!")
        hint_label.config(text=get_random_hint())
    else:
        result_label.config(text="Za wysoka. Spróbuj ponownie!")
        hint_label.config(text=get_random_hint())

    attempts_label.config(text=f"Liczba prób: {attempts}")

submit_button = tk.Button(game_frame, text="Zgadnij", font=("Montserrat", 16), bg="#4CAF50", fg="white",
                          command=submit_guess)
submit_button.pack()

def get_random_hint():
    hints = [
        f"Podpowiedź: Liczba jest większa niż {guess_input.get()}.",
        f"Podpowiedź: Liczba jest mniejsza niż {guess_input.get()}.",
        "Podpowiedź: Spróbuj wybrać liczbę pomiędzy 1 a 100.",
        f"Podpowiedź: Liczba kończy się na {str(secret_number)[-1]}.",
        f"Podpowiedź: Pierwsza cyfra liczby to {str(secret_number)[0]}.",
        "Podpowiedź: Liczba jest większa niż średnia wartość pomiędzy 1 a 100.",
        "Podpowiedź: Liczba jest mniejsza niż średnia wartość pomiędzy 1 a 100.",
        f"Podpowiedź: Spróbuj wybrać liczbę, która jest bliżej {secret_number} niż poprzednia próba.",
        f"Podpowiedź: Spróbuj wybrać liczbę, która jest dalej od {secret_number} niż poprzednia próba."
    ]
    return random.choice(hints)

def update_timer():
    current_time = time.time()
    elapsed_time_in_seconds = int(current_time - start_time)
    minutes = int(elapsed_time_in_seconds / 60)
    seconds = elapsed_time_in_seconds % 60
    hours = int(minutes / 60)
    minutes = minutes % 60
    timer_label.config(text=f"Czas: {hours} godz. {minutes} min. {seconds} sek.")
    timer_label.after(1000, update_timer)

secret_number = random.randint(1, 100)
attempts = 0
start_time = 0

toggle_dark_mode()
window.mainloop()