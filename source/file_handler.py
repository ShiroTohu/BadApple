import json

__author__ = "ShiroTohu"

class FileHandler():
    # Takes in frames and outputs it in JSON format, the file is saved in the output folder with the given name as an argument.
    # usually you want this to be the name of the mp4.
    def save_frames(frames: list, name: str, output = "saves/") -> None: # TODO: FIX THIS GOD FORSAKEN CODE
        with open(f"{output}{name}.json", "w") as file:
            json.dump(frames, file)

    def load_frames(file: str) -> list:
        with open(file, "r") as file:
            return json.load(file)