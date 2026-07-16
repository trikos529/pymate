from connection import Connect
from ui import UI
from actions import Actions
from droidpad import DroidPad
import json
from pathlib import Path

def main():
   # Get the user's home directory 
    home = Path.home()

    config_json = home /"AppData"/"Local"/"OpenActionReciever"/"config.json"
    if config_json.exists():
        #read the file for config and call ui constructor
        UI()
    else:  #default values
        UI()

if __name__ == "__main__":
    main()