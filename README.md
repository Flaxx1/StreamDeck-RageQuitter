# RageQuitter

**RageQuitter** is a simple tool to terminate processes from specific folders, with the option to exclude certain programs. Designed to work seamlessly with Stream Deck, RageQuitter allows gamers and power users to instantly clean up running processes without manually opening Task Manager.

---

## 🚀 Features

- Automatically kills processes from specified folders.
- Allows you to exclude specific programs from termination.
- Fully customizable through a configuration file.
- Compatible with Stream Deck for one-button operation.
- No need for Python installation—runs as a standalone `.exe`.

---

## 🛠️ Installation

1. **Download the program**: 
   - Clone this repository or download the latest release from the [Releases](https://github.com/your-repo-link/releases) section.

2. **Prepare the configuration file**: 
   - Edit the `config.json` file to specify the paths to scan and the processes to exclude.

3. **Set up with Stream Deck**:
   - Add a "System" action in your Stream Deck software and point it to the `RageQuitter.exe` file.

---

## 📄 Configuration

The program uses a `config.json` file to determine which folders to scan and which processes to exclude.

### Example `config.json`

```json
{
    "folder_paths": [
        "F:\\Steam\\steamapps",
        "F:\\Epic Games",
        "D:\\SteamLibrary"
    ],
    "exclude_process_names": [
        "wallpaperservice32_c.exe",
        "wallpaper32.exe",
        "EpicGamesLauncher.exe",
        "EpicWebHelper.exe"
    ]
}
```
- folder_paths: Add paths where the target processes are located.
- exclude_process_names: List process names to exclude from termination.

---

## 💡 Usage

1. **Run RageQuitter**:
   - Double-click the `RageQuitter.exe` file to execute the program.
   - Alternatively, trigger it via your Stream Deck button configured with the `.exe`.

2. **Edit the Configuration**:
   - Open the `config.json` file in a text editor (e.g., Notepad, VS Code).
   - Add or remove folder paths under `"folder_paths"` to include or exclude specific directories.
   - Add or remove process names under `"exclude_process_names"` to manage which programs are ignored during termination.

3. **Test it**:
   - Run the program and ensure the desired processes are terminated while excluded processes remain unaffected.

4. **Automate with Stream Deck**:
   - Add the `.exe` file to a Stream Deck button as a "System > Open" action.
   - Press the button to instantly terminate processes based on your configuration.

---

## ⚠️ Important Notes

- **Administrative Privileges**:
   Some processes may require admin rights to terminate. If RageQuitter does not work as expected, try running it as an administrator.

- **Use with Caution**:
   Be careful when adding folder paths to `config.json`. Ensure you only include directories with processes you intend to terminate, as the program will forcefully kill them.

---

## 🖼️ Icon

RageQuitter comes with a custom skull icon for the `.exe` file. If you'd like to use your own icon:
1. Replace the `skull.ico` file with your desired `.ico` file.
2. Rebuild the `.exe` using the following PyInstaller command:
   ```bash
   pyinstaller --onefile --noconsole --icon=your_icon.ico RageQuitter.py

---

## 🔧 Development

If you'd like to contribute or modify the program:

1. Clone the repository:
    ```
   git clone https://github.com/Flaxx1/StreamDeck-RageQuitter.git
    ```
2. Install dependencies (if using Python):
    ```
   pip install psutil
    ```
3. Test the program locally:
   ```
    python RageQuitter.py
   ```
4. Build the .exe with PyInstaller:
   ```
   pyinstaller --onefile --noconsole --icon=skull.ico RageQuitter.py
   ```
---

## 📝 License

This project is licensed under the MIT License.