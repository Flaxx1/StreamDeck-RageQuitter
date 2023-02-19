import os
import psutil

def stop_processes_in_folder(folder_paths, exclude_process_names):
    for folder_path in folder_paths:
       for proc in psutil.process_iter(['pid', 'name', 'exe']):
            if proc.info['exe'] is None:
                continue
            if any(folder_path in proc.info['exe'] for folder_path in folder_paths) and proc.info['name'] not in exclude_process_names:
                proc.kill()

## Paths where the Games.exe is located
folder_paths = [r'D:\Steam\steamapps', r'D:\Epic Games'] 
## Which .exe should be ignored
exclude_process_names = ['wallpaperservice32_c.exe', 'wallpaper32.exe', 'EpicGamesLauncher.exe', 'EpicWebHelper.exe']

stop_processes_in_folder(folder_paths, exclude_process_names)