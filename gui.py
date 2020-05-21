import tkinter as tk
from main import translate_to_jp


def translate():
    translated.delete('1.0', tk.END)
    if len(entry_field.get()) > 0:
        translated.insert(tk.INSERT, translate_to_jp(entry_field.get()))
    else:
        translated.insert(tk.INSERT, 'There is nothing to translate')


app = tk.Tk()
app.title('Japanese to English translator')

translated_text = 'Nothing has been translated'


entry_field = tk.Entry(app)
entry_field.insert(0, 'こんにちは')
entry_field.pack(side="top")

translate_bt = tk.Button(app)
translate_bt["text"] = "Translate text"
translate_bt["command"] = translate
translate_bt.pack(side="top")

translated = tk.Text(app)
translated.pack(side='bottom')

app.mainloop()
