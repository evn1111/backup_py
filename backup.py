import os
import shutil
from datetime import datetime

def backup_files(source, destination):
    if not os.path.exists(destination):
        os.makedirs(destination)

    backup_name = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    backup_path = os.path.join(destination, backup_name)
    shutil.copytree(source, backup_path)
    print(f"Резервная копия создана: {backup_path}")

source_dir = "/path/to/source"
destination_dir = "/path/to/destination"
backup_files(source_dir, destination_dir)
