import os
import shutil

# Source directories containing logs
source_dirs = [
    "projectA/logs",
    "projectB/logs",
    "projectC/logs"
]

# Destination folder
dest_dir = "all_logs"

# Create destination folder if not exists
os.makedirs(dest_dir, exist_ok=True)

for src in source_dirs:
    if os.path.exists(src):
        for file in os.listdir(src):
            if file.endswith(".log") or file.endswith(".txt"):
                src_path = os.path.join(src, file)
                dest_path = os.path.join(dest_dir, file)
                shutil.copy(src_path, dest_path)
                print(f"Copied {src_path} → {dest_path}")
    else:
        print(f"Source folder not found: {src}")
