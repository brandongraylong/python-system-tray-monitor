# Python System Tray Monitor (PSTM) v1.0.0

## About
Adds clickable icon in system tray which shows cpu, memory, storage, and network statistics

## Attributions
- assets/logo.png modified from: [Font Awesome](https://fontawesome.com/download)
- Great resource on the system tray and Qt5: [Martin Fitzpatrick](https://www.learnpyqt.com/courses/adanced-ui-features/system-tray-mac-menu-bar-applications-pyqt/)

## Python Version
Tested with Python 3.7

## How to Run
### Linux
- Create Python 3.7 virtual environment
- ```source venv/bin/activate```
- ```pip install -r requirements.txt```
- ```python main.py```

## Creating an Executable
After installing dependencies through pip, run `pyinstaller main.py` and then `./dist/main/main` to run.

## Ideal Setup
Add to startup, and you'll have a system tray icon with helpful stats all the time.
