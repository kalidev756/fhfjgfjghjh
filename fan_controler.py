import subprocess
import time
import os
import tkinter as tk
from tkinter import messagebox

ascii_art0="""  ____       _   _   _                 
 / ___|  ___| |_| |_(_)_ __   __ _ ___ 
 \___ \ / _ \ __| __| | '_ \ / _` / __|
  ___) |  __/ |_| |_| | | | | (_| \__ 
 |____/ \___|\__|\__|_|_| |_|\__, |___/
                             |___/     

"""
ascii_art = """
         _nnnn_       ______________               
        dGGGGMMb     /              |
       @p~qp~~qMb    | I'm ready  ! |
       M|@||@) M|   _;..............'
       @,----.JM| -'
      JS^\__/  qKL
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb
   HZM            MMMM
   FqM            MMMM
 __| ".        |\dS"qML
 |    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMM|   .'
     `-'       `--' hjm
     """
ascii_art1 = """
         _nnnn_       ______________               
        dGGGGMMb     /              |
       @p~qp~~qMb    | run: 100%  ! |
       M|@||@) M|   _;..............'
       @,----.JM| -'
      JS^\__/  qKL
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb
   HZM            MMMM
   FqM            MMMM
 __| ".        |\dS"qML
 |    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMM|   .'
     `-'       `--' hjm
     """

stats_ascii="""
 __________________________________________________
|                  STATS                           |
|__________________________________________________|"""

#fan 100%
def fan_controler():
    os.system('clear')

    def run_command():
        subprocess.run(["sudo", "i8kctl", "fan", "2", "2"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    def get_temperature():
        result = subprocess.run(["sensors"], capture_output=True, text=True)
        return result.stdout

    print(ascii_art)
    run = input("Do you want to push the computer's fans to 100%? (y/n) ")

    if run.lower() == "y":
        display_output=input("Would you like to see information about the PC temperature in real time? (not recommended) (y/n)")
        if display_output=="y":
            try:
                os.system('clear')
                subprocess.run(["sudo","echo","v1.0"])
                print(ascii_art1)
                while True:
                    print(ascii_art1)
                    print(stats_ascii)
                    print("Current temperature :")
                    print(get_temperature())  # Afficher la température
                    time.sleep(0.03)  # Pause de 0,5 seconde
                    os.system('clear')  # Effacer l'écran (pour UNIX)
                    run_command()
            except KeyboardInterrupt:
                print("program off.")
        else:
            try:
                os.system('clear')
                subprocess.run(["sudo","echo","v1.0"])
                print(ascii_art1)
                while True:
                    subprocess.run(["sudo","i8kctl", "fan", "2", "2"],stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except KeyboardInterrupt:
                print("program off.")

    else:
        print("Fin du programme")



# temperature monitor

def temperature_monitor():
    print(ascii_art0)
    print("WARNING | can domoged your laptop, we decline all of responsabilities | WARNING")
    print("__________________________________________________________________________________")
    temperature_limit=int(input("Please set the temperature that the tool will consider as overheating:"))
    print("overheating set has",temperature_limit)
    def show_error_popup():
        root = tk.Tk()
        root.withdraw()  # Hide the root window
        messagebox.showerror("WARNING", "system overheating!")
        root.destroy()  # Close the root window

    def get_temperature_monitor():

        result = subprocess.run(["sensors"], capture_output=True, text=True)
        output = result.stdout
        for line in output.split('\n'):
            if "Core 0:" in line: 
                parts = line.split()
                temp_str = parts[2] 
                temp = float(temp_str.strip("+°C"))
                return temp

        return None



    while True:
        temperature = get_temperature_monitor()
        print("Temperature monitor is activated")
        if temperature is not None:
            print(f"Curent température: {temperature}°C")
            if temperature > temperature_limit:
                show_error_popup()
                fan_controler() 
                break
            time.sleep(0.5)
            os.system('clear')
        else:
            print("fail.")
        
        time.sleep(0.001)
    get_temperature_monitor()
temperature_monitor()


