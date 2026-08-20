import hashlib
import os
import json

def hash_file(filepath):
    with open(filepath, "rb") as f:
        contents = f.read()
    return hashlib.sha256(contents).hexdigest()


def hash_folder(folder_path):
    file_hashes = {}
    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)
        if os.path.isfile(full_path):
            file_hashes[filename] = hash_file(full_path)
    return file_hashes


def save_baseline(file_hashes, output_file= "baseline.json"):
    with open(output_file, "w") as f:
        json.dump(file_hashes, f, indent=4)

folder_result= hash_folder(".")
save_baseline(folder_result)
print("Baseline saved!")