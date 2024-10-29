import tkinter as tk
from tkinter import ttk

rates = {
    "USD": 1.0,
    "INR": 74.0,
    "EUR": 0.85,
    "GBP": 0.75,
    "JPY": 110.0,
}

def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_var.get()
        to_currency = to_currency_var.get()

        if from_currency != to_currency:
            converted_amount = amount * (rates[to_currency] / rates[from_currency])
            result_label.config(text=f"Converted Amount: {converted_amount:.2f} {to_currency}")
        else:
            result_label.config(text="Converted Amount: Same currency")
    except ValueError:
        result_label.config(text="Please enter a valid amount")

root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x400")
root.configure(bg="black")

frame = tk.Frame(root, bg="black")
frame.pack(pady=20)

font_style = ("Helvetica", 14, "bold")

amount_label = tk.Label(frame, text="Amount:", bg="black", fg="cyan", font=font_style)
amount_label.grid(row=0, column=0, padx=10, pady=10)

amount_entry = tk.Entry(frame, font=font_style, bg="black", fg="cyan", insertbackground='cyan')
amount_entry.grid(row=0, column=1, padx=10, pady=10)

from_currency_var = tk.StringVar(value="USD")
from_currency_label = tk.Label(frame, text="From Currency:", bg="black", fg="cyan", font=font_style)
from_currency_label.grid(row=1, column=0, padx=10, pady=10)

from_currency_dropdown = ttk.Combobox(frame, textvariable=from_currency_var, values=list(rates.keys()), font=font_style)
from_currency_dropdown.grid(row=1, column=1, padx=10, pady=10)

to_currency_var = tk.StringVar(value="INR")
to_currency_label = tk.Label(frame, text="To Currency:", bg="black", fg="cyan", font=font_style)
to_currency_label.grid(row=2, column=0, padx=10, pady=10)

to_currency_dropdown = ttk.Combobox(frame, textvariable=to_currency_var, values=list(rates.keys()), font=font_style)
to_currency_dropdown.grid(row=2, column=1, padx=10, pady=10)

convert_button = tk.Button(frame, text="Convert", command=convert_currency, font=font_style, bg="cyan", fg="black")
convert_button.grid(row=3, columnspan=2, pady=20)

result_label = tk.Label(frame, text="", bg="black", fg="cyan", font=font_style)
result_label.grid(row=4, columnspan=2, pady=10)

root.mainloop()
