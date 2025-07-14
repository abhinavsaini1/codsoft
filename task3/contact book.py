
# Contact Book by Abhinav
import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

ABHI_CONTACT_FILE = "contacts_abhinav.json"

# Splash screen
def show_splash():
    splash = tk.Toplevel()
    splash.title("Welcome!")
    splash.geometry("300x120")
    tk.Label(splash, text="Abhinav's Unique Contact Book", font=("Arial", 14, "bold"), fg="blue").pack(pady=10)
    tk.Label(splash, text="Created by Abhinav", font=("Arial", 10)).pack()
    splash.after(1500, splash.destroy)

# Load or initialize contacts
def abhi_load_contacts():
    if os.path.exists(ABHI_CONTACT_FILE):
        with open(ABHI_CONTACT_FILE, 'r') as f:
            return json.load(f)
    return {}

def abhi_save_contacts():
    with open(ABHI_CONTACT_FILE, 'w') as f:
        json.dump(abhi_contacts, f, indent=4)

abhi_contacts = abhi_load_contacts()

# Add Contact (dialog)
def abhi_add_contact():
    name = simpledialog.askstring("Name", "Enter Store Name:")
    if name:
        phone = simpledialog.askstring("Phone", "Enter Phone Number:")
        email = simpledialog.askstring("Email", "Enter Email Address:")
        address = simpledialog.askstring("Address", "Enter Store Address:")
        abhi_contacts[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        abhi_save_contacts()
        abhi_refresh_list()


# View All Contacts
def abhi_refresh_list():
    listbox.delete(0, tk.END)
    for name, info in abhi_contacts.items():
        listbox.insert(tk.END, f"{name} - {info['phone']}")


# Search Contact
def abhi_search_contact():
    query = simpledialog.askstring("Search", "Enter Name or Phone:")
    results = []
    for name, info in abhi_contacts.items():
        if query and (query.lower() in name.lower() or query in info["phone"]):
            results.append(f"{name} - {info['phone']}")
    if results:
        messagebox.showinfo("Search Results", "\n".join(results))
    else:
        messagebox.showinfo("Search Results", "No match found.")


# Update Contact
def abhi_update_contact():
    name = simpledialog.askstring("Update", "Enter Store Name to Update:")
    if name in abhi_contacts:
        phone = simpledialog.askstring("Phone", "New Phone:", initialvalue=abhi_contacts[name]["phone"])
        email = simpledialog.askstring("Email", "New Email:", initialvalue=abhi_contacts[name]["email"])
        address = simpledialog.askstring("Address", "New Address:", initialvalue=abhi_contacts[name]["address"])
        abhi_contacts[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        abhi_save_contacts()
        abhi_refresh_list()
    else:
        messagebox.showerror("Error", "Contact not found.")


# Delete Contact
def abhi_delete_contact():
    name = simpledialog.askstring("Delete", "Enter Store Name to Delete:")
    if name in abhi_contacts:
        del abhi_contacts[name]
        abhi_save_contacts()
        abhi_refresh_list()
    else:
        messagebox.showerror("Error", "Contact not found.")


# UI Setup
root = tk.Tk()
root.title("Abhinav's Contact Book")
root.geometry("420x540")

show_splash()


listbox = tk.Listbox(root, width=52)
listbox.pack(pady=10)

# Contacts are saved in 'contacts_abhinav.json' in the same folder as this script


# Entry fields for adding contact (move to top)
entry_frame = tk.Frame(root)
entry_frame.pack(side="top", pady=10)

tk.Label(entry_frame, text="Name:", font=("Arial", 12, "bold"), fg="#1a73e8").grid(row=0, column=0, sticky="e")
name_entry = tk.Entry(entry_frame, width=32)
name_entry.grid(row=0, column=1, ipady=6)

tk.Label(entry_frame, text="Phone:", font=("Arial", 12, "bold"), fg="#1a73e8").grid(row=1, column=0, sticky="e")
phone_entry = tk.Entry(entry_frame, width=32)
phone_entry.grid(row=1, column=1, ipady=6)

tk.Label(entry_frame, text="Email:", font=("Arial", 12, "bold"), fg="#1a73e8").grid(row=2, column=0, sticky="e")
email_entry = tk.Entry(entry_frame, width=32)
email_entry.grid(row=2, column=1, ipady=6)

tk.Label(entry_frame, text="Address:", font=("Arial", 12, "bold"), fg="#1a73e8").grid(row=3, column=0, sticky="e")
address_entry = tk.Entry(entry_frame, width=32)
address_entry.grid(row=3, column=1, ipady=6)

# Add contact from entry boxes
def abhi_add_contact_from_entry():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()
    if not name:
        messagebox.showerror("Error", "Name is required.")
        return
    abhi_contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    abhi_save_contacts()
    abhi_refresh_list()
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Export contacts to TXT (unique feature)
def abhi_export_contacts():
    filename = "contacts_export_abhinav.txt"
    with open(filename, "w") as f:
        for name, info in abhi_contacts.items():
            f.write(f"Name: {name}\nPhone: {info['phone']}\nEmail: {info['email']}\nAddress: {info['address']}\n---\n")
    messagebox.showinfo("Export", f"Contacts exported to {filename}")


# Place buttons at the very bottom, after the footer
footer = tk.Label(root, text="Created by Abhinav", font=("Arial", 10, "italic"), fg="gray")
footer.pack(side="bottom", pady=5)


# Arrange buttons in two columns per row
button_frame = tk.Frame(root)
button_frame.pack(side="bottom", pady=5)

tk.Button(button_frame, text="Add Contact", command=abhi_add_contact_from_entry, width=20).grid(row=0, column=0, padx=2, pady=2)
tk.Button(button_frame, text="Update Contact", command=abhi_update_contact, width=20).grid(row=0, column=1, padx=2, pady=2)
tk.Button(button_frame, text="Delete Contact", command=abhi_delete_contact, width=20).grid(row=1, column=0, padx=2, pady=2)
tk.Button(button_frame, text="Search Contact", command=abhi_search_contact, width=20).grid(row=1, column=1, padx=2, pady=2)
tk.Button(button_frame, text="Refresh List", command=abhi_refresh_list, width=20).grid(row=2, column=0, padx=2, pady=2)
tk.Button(button_frame, text="Export Contacts", command=abhi_export_contacts, bg="#e0e0e0", width=20).grid(row=2, column=1, padx=2, pady=2)

abhi_refresh_list()
root.mainloop()