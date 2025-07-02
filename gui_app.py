import tkinter as tk
from tkinter import messagebox
from contact_utils import get_label, generate_number_list, export_vcard

def on_generate_click():
    prefix = entry.get()
    if not prefix.isdigit():
        messagebox.showerror("Please enter digits only. No dashes, spaces, or other characters.\n")
        return

    number = int(prefix)
    if number < 1000:
        print()
        print("Due to performance concerns, maximum numbers per request is 1,000,000.")
        print("Most mobile devices will not be capable of processing contacts of this size.")
        print("Proceed with caution.")
        print()
        print("Please set prefix to at least 4 digits.\n")
        return

    label = get_label(number)
    numbers = generate_number_list(number)
    export_vcard(numbers, label)
    # messagebox.showinfo(f"Contact '{label}.vcf' exported successfully!")
    messagebox.showinfo("Success", f"Contact '{label}.vcf' exported successfully!")

root = tk.Tk()
root.title("Welcome to Hart's phone number range contact generator!")
root.geometry("400x180")

tk.Label(root, text = "Partial phone number:").pack(pady=10)
entry = tk.Entry(root, font = ("Helvetica", 14))
entry.pack(pady=5)

generate_button = tk.Button(root, text = "Generate Contact", command = on_generate_click)
generate_button.pack(pady=15)

root.mainloop()
