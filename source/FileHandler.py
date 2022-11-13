import json

class FileHandler:
    def save_frames(frames: str, name: str, output = "output/") -> None:
        with open(f"{name}.json", "w") as file:
            json.dump(frames, file)

    def load_frames(file: str) -> list:
        with open(file, "r") as file:
            return json.load(file)