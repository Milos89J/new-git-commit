import os
import shutil
import zipfile

def main():
    # Define the base directory (one level up from /scripts)
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    repo_path = os.path.abspath(base_dir)

    # Files to exclude from the repo temporarily while packaging
    files_to_exclude = [
        "pilot/.env",
        "pilot/gpt-pilot"
    ]

    # Step 1: Move excluded files to /tmp
    tmp_excluded_paths = []
    for file in files_to_exclude:import os
import shutil
import zipfile

def main():
    # Define the base directory (one level up from /scripts)
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    repo_path = os.path.abspath(base_dir)

    # Files to exclude from the repo temporarily while packaging
    files_to_exclude = [
        "pilot/.env",
        "pilot/gpt-pilot"
    ]

    # Step 1: Move excluded files to /tmp
    tmp_excluded_paths = []
    for file in files_to_exclude:
        source_path = os.path.join(repo_path, file)
        if os.path.exists(source_path):
            tmp_path = os.path.join("/tmp", os.path.basename(file))
            shutil.move(source_path, tmp_path)
            tmp_excluded_paths.append((tmp_path, source_path))
        source_path = os.path.join(repo_path, file)
        if os.path.exists(source_path):
            tmp_path = os.path.join("/tmp", os.path.basename(file))
            shutil.move(source_path, tmp_path)
            tmp_excluded_paths.append((tmp_path, source_path))