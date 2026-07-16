from connection import Connect
from ui import UI
from actions import Actions
from droidpad import DroidPad
import json
from pathlib import Path

def main():
   config_add()

def config_add(bg_color: str, text_color: str, btn_color: str, btn_atcive_color: str, btn_size: str, win_width: str, win_height: str, font: str, font_size: str, sidebar_bg: str, sidebar_width_percent: str):
    # Get the user's home directory 
    home = Path.home()

    # Read JSON data
    config_json = home /"AppData"/"Local"/"OpenActionReciever"/"config.json"
    if config_json.exists():
        with config_json.open("r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {}
                home = None
        UI()
    else:  #default values
        UI()

def default_values():
    ...

if __name__ == "__main__":
    main()