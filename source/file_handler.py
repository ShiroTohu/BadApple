import json
import os

__author__ = "ShiroTohu"

# The Save System Will have a folder named "cache" (for the time being as it makes sense in my mind) where videos will be stored
# each video has an allocated folder with the name of the mp4 as the folder name (without the .mp4 part). In said folder will be the JSON file and the audio file
# the audio file is required so that you do not need the mp4 to run the video.
#! cache/{filename}/...

class FileHandler():
    # creates the required folders and files to store the video for later use.
    def save_video(frames: list, name: str, audio: str) -> None:
        # creates and checks cache folder
        #! I'm sure there has to be a better way but this is here for now
        if not (os.path.exists("../cache")):
            os.mkdir("../cache")

        if not (os.path.exists(f"../cache/{name}")):
            os.mkdir(f"../cache/{name}")

        # saves video information to frames.json
        with open(f"../cache/{name}/frames.json", "w") as file_destination: #? consider modularising??!?? :/
            video_information = {
                "name": name, 
                "audio": audio,
                "coloums": coloums,
                "scale": scale,
                "frames": frames}
            json.dump(video_information, file_destination)

    # returns JSON object as python dictionary.
    def load_file(file: str):
        with open(file, "r") as file:
            return json.load(file)

if __name__ == "__main__":
    frames = ["#############\n#############..#######\n"]
    FileHandler.save_video(frames, "girth", "sex.mp4")