import os
import psutil
import json

# Lade die Konfiguration aus einer JSON-Datei
def load_config(config_path):
    with open(config_path, 'r') as file:
        return json.load(file)

def stop_processes_in_folder(folder_paths, exclude_process_names):
    for folder_path in folder_paths:
        for proc in psutil.process_iter(['pid', 'name', 'exe']):
            if proc.info['exe'] is None:
                continue
            if any(folder_path in proc.info['exe'] for folder_path in folder_paths) and proc.info['name'] not in exclude_process_names:
                proc.kill()

# Konfigurationsdatei laden
config = load_config("config.json")

# Daten aus der Konfiguration verwenden
folder_paths = config["folder_paths"]
exclude_process_names = config["exclude_process_names"]

stop_processes_in_folder(folder_paths, exclude_process_names)
