# StreamDeck-RageQuitter
Rage quit from all Steam and Epic Games for Elgato Stream Deck

# Requirements: 

✓	Python310 or above
✓	pip install psutil

# How To:

◉ Edit RageQuit.bat, the first path must lead to the installation path of Python.
◉ The second path must lead to RageQuitter.py

◉ Edit RageQuitter.py, in line 13 the steamapps directory must be specified.

```
folder_paths = [r'D:\Steam\steamapps', r'D:\Epic Games'] 
```

◉ In line 15, apps can be specified that are not allowed to be closed.

```
exclude_process_names = ['wallpaperservice32_c.exe', 'wallpaper32.exe', 'EpicGamesLauncher.exe', 'EpicWebHelper.exe']
```

◉ Open Stream Deck app select "Open" under System and select App/File: RageQuit.bat

# Happy RageQuitting ✓

