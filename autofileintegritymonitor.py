import hashlib
import os
import json
import tkinter as tk


def hash_file(filepath):
    with open(filepath, "rb") as f:
        contents = f.read()
    return hashlib.sha256(contents).hexdigest()


def hash_folder(folder_path):
    file_hashes = {}
    for filename in os.listdir(folder_path):
        if filename == "baseline.json": #we are ignoring this json file. we don't actually want it
            continue
        full_path = os.path.join(folder_path, filename)
        if os.path.isfile(full_path):
            file_hashes[filename] = hash_file(full_path)
    return file_hashes


def save_baseline(file_hashes, output_file= "baseline.json"):
    with open(output_file, "w") as f:
        json.dump(file_hashes, f, indent=4)



def load_baseline(baseline_file="baseline.json"):
    with open(baseline_file, "r") as f:
        return json.load(f)

def compare_hashes(old_hashes, new_hashes):
    modified = []
    new_files = []
    deleted_files = []

    for filename in old_hashes:
        if filename not in new_hashes:
            deleted_files.append(filename)
        elif old_hashes[filename] != new_hashes[filename]:
            modified.append(filename)

    for filename in new_hashes:
        if filename not in old_hashes:
            new_files.append(filename)

    return modified, new_files, deleted_files

#creating a basic menu for saving a new baseline or check for changes

def main():
    while True:
        print("\n--- File Integrity Monitor ---")
        print("1. Save new baseline")
        print("2. Check for changes")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            hashes = hash_folder(".")
            save_baseline(hashes)
            print("Baseline saved!")

        elif choice == "2":
            old_hashes = load_baseline()
            new_hashes = hash_folder(".")
            modified, new_files, deleted_files = compare_hashes(old_hashes, new_hashes)
            print("Modified files:", modified)
            print("New files:", new_files)
            print("Deleted files:", deleted_files)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")

#tkinter part(adding original interface here) with the help of AI also


window = tk.Tk()
window.title("File Integrity Monitor")
window.geometry("450x400")
window.configure(bg="#1e1e2e")

title_label = tk.Label(
    window,
    text="🔒 Ahad's File Integrity Monitor",
    font=("Segoe UI", 16, "bold"),
    bg="#1e1e2e",
    fg="#ffffff"
)
title_label.pack(pady=15)

output_box = tk.Text(
    window,
    height=12,
    width=48,
    bg="#2a2a3a",
    fg="#00ff88",
    font=("Consolas", 10),
    insertbackground="white"
)
output_box.pack(pady=10)


def on_save_click():
    hashes = hash_folder(".")
    save_baseline(hashes)
    output_box.insert(tk.END, "✔ Baseline saved!\n")


def on_check_click():
    old_hashes = load_baseline()
    new_hashes = hash_folder(".")
    modified, new_files, deleted_files = compare_hashes(old_hashes, new_hashes)
    output_box.insert(tk.END, f"Modified: {modified}\n")
    output_box.insert(tk.END, f"New: {new_files}\n")
    output_box.insert(tk.END, f"Deleted: {deleted_files}\n")


save_button = tk.Button(
    window,
    text="Save Baseline",
    command=on_save_click,
    bg="#4caf50",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    relief="flat",
    padx=10,
    pady=5
)
save_button.pack(pady=5)

check_button = tk.Button(
    window,
    text="Check for Changes",
    command=on_check_click,
    bg="#2196f3",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    relief="flat",
    padx=10,
    pady=5
)
check_button.pack(pady=5)

window.mainloop()