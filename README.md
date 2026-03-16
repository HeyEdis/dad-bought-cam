# dad-bought-cam

Python script to concatenate video footage.

## Lore

My dad bought a security camera off wish, so he could catch the people responsible for vandalizing his sign.
One day I walk downstairs and see this man, going through the footage. This camera records 24/7 and it is partinioned into clips of 5 minutes sometimes clips of 10 - 30 seconds. One of these folders had over 800 files lol.

So, I saw this man going through the clips, skipping them one at the time, and I've been studying CS for three years. This felt like a great use case to make something usefull and knowing it will be used.

I rushed to my room, and started up the editor, went through a couple of iterations. To finaly present it that evening. Gave them the full spiel on how to use it, used the existing footage, and ever since that demo, this script hasn't been used even once lol. The vandal did their thing already, now we need to prep a new trap, to catch them in the act.

The hunt is still on!
One day I will see him click that `.exe` file and CONCATENATE some footage!

## The structure

This script opens up a window, where the user can select the SD card. Then it checks if a certain folder exists, and creates a new folder on your system to store the footage on.

Then it does a second check, if a folder exists with a date, it sorts the footage and creates a `.txt` file to holds each file name. Afterwards, it loops through that list and concatenates the footage into one master `.mp4` file using ffmpeg. Once it's done it deletes the `.txt` file and prints a succes message.

Also all printlines are in Bosnian :p Thats what pops understands the most.

## How to use it

To turn it into an `.exe` you need a Windows OS to create the binary for that OS. When I did it on Linux, it created the wrong binaries. If it can be done on Linux you will have to figure that one out. Untill then get the ol' slop out.

### Step -1: Install FFMPEG

Get it through their site, or winget or if you are on Arch use this command:

```bash

sudo pacman -S ffmpeg

```

### Step 0: Set your camera version in the script

### Step 1: Make a Python environment, so that you don't litter your system with packages

Here are some [extend instructions](https://www.w3schools.com/python/python_virtualenv.asp).

```python

python -m venv myfirstproject

```

### Step 2: Install PyInstaller. This tool packages the script into a single executable file

```python

pip intall pyinstaller

```

### Step 3: Run the final command

```python

pyinstaller --onefile dad-bought-cam.py

```
