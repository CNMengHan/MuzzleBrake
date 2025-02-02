# Auto-Recoil Control

## Description

This Python script is designed to simulate automatic recoil control for FPS games by moving the mouse vertically to counteract weapon recoil. When both the left and right mouse buttons are pressed simultaneously, the script activates a thread that repeatedly moves the mouse down at a constant speed, simulating "recoil compensation." Once either button is released, the recoil compensation stops.

This script utilizes the `pynput` library to listen to mouse events and the `ctypes` library to simulate mouse movement on Windows platforms.

## Features

- **Automatic Recoil Compensation**: The script automatically compensates for recoil by moving the mouse down at a fixed rate.
- **Customizable Speed**: The movement speed can be adjusted by changing the value in the `px` function (currently set to 4 pixels per iteration).
- **Easy Start/Stop Mechanism**: The script starts when both the left and right mouse buttons are pressed and stops when either is released.
- **Lightweight**: Runs in the background without requiring any game modifications.

## Requirements

- **Python 3.10** or higher
- **pynput** library for mouse event handling
- Windows 10/11 (because `ctypes.windll.user32` is Windows-specific)

### Install Required Libraries

To install the required library (`pynput`), you can use `pip`:

```bash
pip install pynput
```

## How It Works

1. **Mouse Click Detection**: The script listens for mouse button presses using `pynput.mouse.Listener`.
2. **Recoil Control Activation**: When both the left and right mouse buttons are pressed, a new thread is started that simulates recoil compensation by moving the mouse down at a specified distance.
3. **Recoil Control Deactivation**: The recoil control stops when either the left or right mouse button is released.
4. **Mouse Movement**: The mouse is moved vertically by a small amount (default: 4 pixels every 15ms), simulating the action of controlling recoil.

## Usage

1. **Run the Script**: Execute the script in your terminal or IDE. The script will print "Ready..." to indicate that it's waiting for input.
   
   ```bash
   python MuzzleBrake.py
   ```

2. **Start Recoil Compensation**: Press both the left and right mouse buttons at the same time. The script will automatically start moving the mouse down to counteract recoil.

3. **Stop Recoil Compensation**: Release either the left or right mouse button to stop the recoil compensation.

4. **Adjust Speed**: To adjust the recoil compensation speed, modify the value passed to `px(y_distance)` in the `main()` function. Higher values will move the mouse faster, while smaller values will result in slower compensation.

## Code Walkthrough

- **Mouse Event Simulation**: 
   - `user32.mouse_event(MOUSEEVENTF_MOVE, 0, y_distance, 0, 0)` simulates moving the mouse by `y_distance` pixels.
   
- **Event Listeners**: 
   - The `on_click` function listens for mouse events, updating whether the left and right buttons are pressed and starting or stopping the recoil compensation accordingly.

- **Threading**:
   - The `main()` function runs in a separate thread, continuously moving the mouse until recoil compensation is deactivated.

## Important Notes

- **Platform**: This script is specifically designed for Windows. If you are using another OS, you may need to modify the code to simulate mouse events.
- **Games Compatibility**: This script might not work with all games due to anti-cheat mechanisms, and it should be used in compliance with the game's terms of service.
- **Legal Considerations**: Make sure you are not violating any game rules or terms of service by using automation scripts like this.

## Troubleshooting

- **Error: ModuleNotFoundError: No module named 'pynput'**
   - Solution: Install the `pynput` library using `pip install pynput`.

- **Recoil Compensation Not Working**:
   - Ensure both the left and right mouse buttons are being pressed simultaneously to activate the recoil control.
   - If you're using a non-Windows OS, this script may not work as it relies on Windows-specific APIs (`ctypes.windll.user32`).

---

### Adjustments & Improvements

If you plan to further develop or improve the script, here are some ideas:
1. **Mouse Movement Direction**: Currently, the script moves the mouse down. You could make the direction configurable or add more complex patterns based on the game’s recoil.
2. **Sensitivity Control**: Allow users to modify the sensitivity and movement speed dynamically via command-line arguments or a settings file.
3. **Cross-Platform Compatibility**: For cross-platform compatibility, consider using a different library (like `pyautogui`) to simulate mouse events that work on both Windows and MacOS/Linux.
