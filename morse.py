import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog

# Словники для кодування букв в азбуку Морзе
morse_code_dict_en = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.'
}

morse_code_dict_uk = {
    'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.', 'Ґ': '--.-',
    'Д': '-..', 'Е': '.', 'Є': '.-..-', 'Ж': '...-', 'З': '--..',
    'И': '..', 'І': '..', 'Ї': '.-..', 'Й': '.---', 'К': '-.-',
    'Л': '.-..', 'М': '--', 'Н': '-.', 'О': '---', 'П': '.--.',
    'Р': '.-.', 'С': '...', 'Т': '-', 'У': '..-', 'Ф': '..-.',
    'Х': '....', 'Ц': '-..-', 'Ч': '---.', 'Ш': '--', 'Щ': '--..-',
    'Ь': '-..-', 'Ю': '..--', 'Я': '.-.-'
}

morse_code_dict_ru = {
    'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.', 'Д': '-..',
    'Е': '.', 'Ё': '.', 'Ж': '...-', 'З': '--..', 'И': '..',
    'Й': '.---', 'К': '-.-', 'Л': '.-..', 'М': '--', 'Н': '-.',
    'О': '---', 'П': '.--.', 'Р': '.-.', 'С': '...', 'Т': '-',
    'У': '..-', 'Ф': '..-.', 'Х': '....', 'Ц': '-..-', 'Ч': '---.',
    'Ш': '--', 'Щ': '--..-', 'Ъ': '--.--', 'Ы': '-.--', 'Ь': '-..-',
    'Э': '..-..', 'Ю': '..--', 'Я': '.-.-'
}

# Зворотні словники для декодування
reverse_morse_code_dict_en = {value: key for key, value in morse_code_dict_en.items()}
reverse_morse_code_dict_uk = {value: key for key, value in morse_code_dict_uk.items()}
reverse_morse_code_dict_ru = {value: key for key, value in morse_code_dict_ru.items()}

class MorseCodeApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Morse Code Converter")
        self.master.configure(bg="#f0f0f0")

        # Показує повідомлення про бета-тест
        messagebox.showinfo("Бета-тест", "ЦЯ ПРОГРАМА, ЯКУ ВИ ВИКОРИСТОВУЄТЕ, ЗНАХОДИТЬСЯ В БЕТА-ТЕСТІ")

        # Labels
        self.label = tk.Label(master, text="Виберіть опцію:", font=("Comic Sans MS", 18, 'bold'), bg="#f0f0f0")
        self.label.pack(pady=10)

        # Frame for buttons
        self.button_frame = tk.Frame(master, bg="#f0f0f0")
        self.button_frame.pack(pady=20)

        # Buttons
        self.encode_button = tk.Button(self.button_frame, text="Кодувати", command=self.encode, bg="#4CAF50", fg="white", font=("Comic Sans MS", 14), padx=10, pady=5)
        self.encode_button.grid(row=0, column=0, padx=10, pady=5)

        self.decode_button = tk.Button(self.button_frame, text="Декодувати", command=self.decode, bg="#2196F3", fg="white", font=("Comic Sans MS", 14), padx=10, pady=5)
        self.decode_button.grid(row=0, column=1, padx=10, pady=5)

        self.load_button = tk.Button(self.button_frame, text="Завантажити з файлу", command=self.load_file, bg="#FFC107", fg="white", font=("Comic Sans MS", 14), padx=10, pady=5)
        self.load_button.grid(row=1, column=0, padx=10, pady=5)

        self.save_button = tk.Button(self.button_frame, text="Зберегти в файл", command=self.save_file, bg="#FF5722", fg="white", font=("Comic Sans MS", 14), padx=10, pady=5)
        self.save_button.grid(row=1, column=1, padx=10, pady=5)

        self.view_dict_button = tk.Button(self.button_frame, text="Переглянути кодування", command=self.view_dict, bg="#3F51B5", fg="white", font=("Comic Sans MS", 14), padx=10, pady=5)
        self.view_dict_button.grid(row=2, column=0, padx=10, pady=5)

        self.show_stats_button = tk.Button(self.button_frame, text="Статистика", command=self.show_statistics, bg="#673AB7", fg="white", font=("Comic Sans MS", 14), padx=10, pady=5)
        self.show_stats_button.grid(row=2, column=1, padx=10, pady=5)

        self.show_extra_button = tk.Button(self.button_frame, text="Додаткові функції", command=self.show_extra, bg="#009688", fg="white", font=("Comic Sans MS", 14), padx=10, pady=5)
        self.show_extra_button.grid(row=3, column=0, padx=10, pady=5)

        self.support_button = tk.Button(self.button_frame, text="Підтримка", command=self.show_support, bg="#FF9800", fg="white", font=("Comic Sans MS", 14), padx=10, pady=5)
        self.support_button.grid(row=3, column=1, padx=10, pady=5)

        self.about_button = tk.Button(self.button_frame, text="Про нас", command=self.show_about, bg="#9E9E9E", fg="white", font=("Comic Sans MS", 14), padx=10, pady=5)
        self.about_button.grid(row=4, column=0, padx=10, pady=5)

        self.quit_button = tk.Button(self.button_frame, text="Вихід", command=self.master.quit, bg="#F44336", fg="white", font=("Comic Sans MS", 14), padx=10, pady=5)
        self.quit_button.grid(row=4, column=1, pady=10)

        self.copy_button = tk.Button(self.button_frame, text="Копіювати закодований текст", command=self.copy_to_clipboard, bg="#9E9E9E", fg="white", font=("Comic Sans MS", 14), padx=10, pady=5)
        self.copy_button.grid(row=5, columnspan=2, pady=10)

        self.paste_button = tk.Button(self.button_frame, text="Вставити з буферу обміну", command=self.paste_from_clipboard, bg="#9E9E9E", fg="white", font=("Comic Sans MS", 14), padx=10, pady=5)
        self.paste_button.grid(row=6, columnspan=2, pady=10)

        self.copied_text = ""  # Змінна для зберігання закодованого тексту

        # Оновлюємо розміри вікна
        self.master.update_idletasks()
        self.master.geometry(f"{self.master.winfo_width() + 50}x{self.master.winfo_height()}")

    def encode(self):
        lang = simpledialog.askstring("Вибір мови", "Введіть '1' для англійської, '2' для української або '3' для російської:")
        if lang not in ['1', '2', '3']:
            messagebox.showerror("Помилка", "Неправильний вибір мови.")
            return

        text = simpledialog.askstring("Введіть текст", "Введіть текст для кодування:")
        if not text:
            messagebox.showerror("Помилка", "Введіть текст для кодування.")
            return

        if lang == '1':
            morse_code = ' '.join(morse_code_dict_en.get(char.upper(), '') for char in text)
        elif lang == '2':
            morse_code = ' '.join(morse_code_dict_uk.get(char.upper(), '') for char in text)
        else:
            morse_code = ' '.join(morse_code_dict_ru.get(char.upper(), '') for char in text)

        self.copied_text = morse_code
        messagebox.showinfo("Закодований текст", morse_code)

    def decode(self):
        lang = simpledialog.askstring("Вибір мови", "Введіть '1' для англійської, '2' для української або '3' для російської:")
        if lang not in ['1', '2', '3']:
            messagebox.showerror("Помилка", "Неправильний вибір мови.")
            return

        morse_code = simpledialog.askstring("Введіть код Морзе", "Введіть текст для декодування:")
        if not morse_code:
            messagebox.showerror("Помилка", "Введіть текст для декодування.")
            return

        if lang == '1':
            decoded_text = ''.join(reverse_morse_code_dict_en.get(code, '') for code in morse_code.split())
        elif lang == '2':
            decoded_text = ''.join(reverse_morse_code_dict_uk.get(code, '') for code in morse_code.split())
        else:
            decoded_text = ''.join(reverse_morse_code_dict_ru.get(code, '') for code in morse_code.split())

        messagebox.showinfo("Декодований текст", decoded_text)

    def load_file(self):
        file_path = filedialog.askopenfilename(title="Виберіть файл", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
        if not file_path:
            return

        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        messagebox.showinfo("Завантажено текст", content)
        self.copied_text = content  # Зберігаємо в закодованому тексті

    def save_file(self):
        if not self.copied_text:
            messagebox.showerror("Помилка", "Немає закодованого тексту для збереження.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
        if not file_path:
            return

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(self.copied_text)

        messagebox.showinfo("Збережено", f"Текст збережено в {file_path}")

    def view_dict(self):
        lang = simpledialog.askstring("Вибір мови", "Введіть '1' для англійської, '2' для української або '3' для російської:")
        if lang not in ['1', '2', '3']:
            messagebox.showerror("Помилка", "Неправильний вибір мови.")
            return

        if lang == '1':
            dict_view = "\n".join(f"{key}: {value}" for key, value in morse_code_dict_en.items())
        elif lang == '2':
            dict_view = "\n".join(f"{key}: {value}" for key, value in morse_code_dict_uk.items())
        else:
            dict_view = "\n".join(f"{key}: {value}" for key, value in morse_code_dict_ru.items())

        messagebox.showinfo("Кодування", dict_view)

    def show_statistics(self):
        # Тут можна додати код для статистики
        messagebox.showinfo("Статистика", "Тут буде статистика.")

    def show_extra(self):
        # Додаткові функції
        messagebox.showinfo("Додаткові функції", "Тут будуть додаткові функції.")

    def show_support(self):
        # Інформація про підтримку
        messagebox.showinfo("Підтримка", "Тут буде інформація про підтримку.")

    def show_about(self):
        # Інформація про програму
        messagebox.showinfo("Про нас", "Це програма для кодування та декодування тексту в азбуку Морзе.")

    def copy_to_clipboard(self):
        self.master.clipboard_clear()
        self.master.clipboard_append(self.copied_text)
        messagebox.showinfo("Успішно", "Закодований текст скопійовано до буфера обміну.")

    def paste_from_clipboard(self):
        pasted_text = self.master.clipboard_get()
        messagebox.showinfo("Вставлений текст", pasted_text)
        # Тепер можемо декодувати вставлений текст
        self.decode_text(pasted_text)

    def decode_text(self, morse_code):
        lang = simpledialog.askstring("Вибір мови", "Введіть '1' для англійської, '2' для української або '3' для російської:")
        if lang not in ['1', '2', '3']:
            messagebox.showerror("Помилка", "Неправильний вибір мови.")
            return

        if lang == '1':
            decoded_text = ''.join(reverse_morse_code_dict_en.get(code, '') for code in morse_code.split())
        elif lang == '2':
            decoded_text = ''.join(reverse_morse_code_dict_uk.get(code, '') for code in morse_code.split())
        else:
            decoded_text = ''.join(reverse_morse_code_dict_ru.get(code, '') for code in morse_code.split())

        messagebox.showinfo("Декодований текст", decoded_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = MorseCodeApp(root)
    root.mainloop()
