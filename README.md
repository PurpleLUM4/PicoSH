# PicoSH

![pico_img](https://de.farnell.com/productimages/large/en_GB/3643332-40.jpg)

PicoSH is a basic shell designed to give you more control about your device

## Featurs
- Browse through FS using 'cd' and 'ls'.
- Delete files using 'rm'.
- Move files using 'mv'.
- Copy files using 'cp'.
- Execute other python scripts using 'micropython' or 'circuitpython' depending what you are running PicoSH on.
- A .PicoSH cfg in the root of your pico that executes on startup. (like .bashrc)

## Installation
Put the main.py on your raspberry pi pico, it automaticly creates a .PicoSH cfg in the same directory.
