# StreamDeck-RageQuitter
"RageQuitter" is an application for the Elgato Stream Deck that allows users to quickly quit out of all running Steam and Epic Games games. With this application, players can quit all open games on the Steam and Epic Games platforms with just one keystroke. This is especially useful when users are frustrated or need to quickly switch between different games. The application provides a simple and efficient way to exit games without having to search through multiple windows or menus.

## Requirements: 

✓	Python310 or above

✓	pip install psutil

## How To:

◉ Edit RageQuit.bat, the first path must lead to the installation path of Python.

```
C:\PATH_TO_YOUR_PYTHON\python.exe
```

◉ The second path must lead to RageQuitter.py

```
C:\PATH_TO_RageQuitter.py\RageQuitter.py
```

◉ Edit RageQuitter.py, in line 13 the steamapps directory must be specified.

```
folder_paths = [r'D:\Steam\steamapps', r'D:\Epic Games'] 
```

◉ In line 15, apps can be specified that are not allowed to be closed.

```
exclude_process_names = ['wallpaperservice32_c.exe', 'wallpaper32.exe', 'EpicGamesLauncher.exe', 'EpicWebHelper.exe']
```

◉ Open Stream Deck app select "Open" under System and select App/File: RageQuit.bat

### Happy RageQuitting ✓
