from pathlib import Path
from datetime import datetime
import subprocess
from tkinter import Tk
from tkinter.filedialog import askdirectory
import os

camera = "insert version"

# Hide main Tkinter window
Tk().withdraw()

# Ask dad to select the SD card root
print("Izaberite SD karticu")
SD_ROOT = askdirectory(title="Izaberite SD karticu")
if not SD_ROOT:
    print("Niste izabrali folder. Prekidam.")
    input("Pritisnite Enter za izlaz...")
    exit()

SD_ROOT=Path(SD_ROOT).resolve()
VE_FOLDER = SD_ROOT / camera / "video"

if not VE_FOLDER.exists():
    print(f"Nije pronadzen folder {camera}")
    input("Pritisnite Enter za izlaz...")
    exit()


OUTPUT_ROOT = Path.home() / "Documents" / "Kucica"
os.makedirs(OUTPUT_ROOT, exist_ok = True)
print(f"Output folder je : {OUTPUT_ROOT}")

print("===================================")
print(" Alat za spajanje video snimaka počinje")
print(" Molimo nemojte zatvarati ovaj prozor")
print("===================================\n")



def is_valid_date_folder(folder: Path) -> bool:
    """
    Returns True only if folder name is a valid YYYY-MM-DD date.
    """
    try:
        datetime.strptime(folder.name, "%Y-%m-%d")
        return True
    except ValueError:
        return False


for date_folder in sorted(VE_FOLDER.iterdir()):
    
    if not date_folder.is_dir():
        continue

    if not is_valid_date_folder(date_folder):
        print(f"{date_folder.name}: s1 folder ne postoji, preskačem.")
        continue

    s1_folder = date_folder / "s1"
    if not s1_folder.exists():
        print(f"Skipping er is geen s1 folder in {date_folder.name}")
        continue

    print(f"\nObrađujem snimak za datum: {date_folder.name}")

    videos = sorted(s1_folder.glob("*.mp4"))
    if not videos:
        print("Nema video fajlova, preskačem.")
        continue

    filelist = s1_folder / "filelist.txt"
    with filelist.open("w", encoding="utf-8") as f:
        for v in videos:
            f.write(f"file '{v}'\n")

    output = OUTPUT_ROOT / f"{date_folder.name}.mp4"
    if output.exists():
        print("Izlaz već postoji, preskačem.")
        continue

    print("Spajam video snimke... molimo sačekajte.")
    
    cmd = [
        "ffmpeg",
        "-f", "concat",
        "-safe", "0",
        "-i", str(filelist),
        "-c", "copy",
        str(output)
    ]

    result = subprocess.run(cmd, cwd=s1_folder)

    try:
        filelist.unlink()
        print(f"  🗑 Obrišen privremeni filelist.txt iz {s1_folder}")
    except Exception as e:
        print(f"  ⚠ Ne mogu obrisati filelist.txt: {e}")

    if result.returncode == 0:
        print(f"  ✅ Gotovo: {output.name}")
    else:
        print(f"  ❌ Greška pri obradi {output.name}")

print("\n===================================")
print(" Sve snimke su obrađene")
print(" Sada možete zatvoriti ovaj prozor")
print("===================================")
input("Pritisnite Enter za izlaz...")
