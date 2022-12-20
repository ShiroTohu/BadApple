import json
import os

__author__ = "ShiroTohu"

#! cache/{filename}/...
#TODO: The cache is creaating a file relative to the file it has run of off
class CacheHandler:
    # creates a json file with the ASCII frames an dother relevant information.
    def save_rendered_information(frames: list, name_of_video: str, coloums: int, scale: int) -> None:
        CacheHandler.create_cache_folder()

        # saves video information to frames.json
        with open(f"../cache/{name_of_video}/frames.json", "w") as file_destination:
            video_information = {
                "name": name_of_video, 
                "audio": "audio.mp3",
                "coloums": coloums,
                "scale": scale,
                "frames": frames}
            json.dump(video_information, file_destination)

    # creates the cache folder if it doesn't exist
    def create_cache_folder(name_of_video: str):
        if not (os.path.exists("../cache")):
                    os.mkdir("../cache")

        if not (os.path.exists(f"../cache/{name_of_video}")):
            os.mkdir(f"../cache/{name_of_video}")

    # returns JSON object as python dictionary.
    def load_file(file_path: str):
        with open(file_path, "w") as file:
            return json.load(file)

    def get_cache_folders():
        return os.listdir("D:\Mine\Programming\BadApple\cache")

if __name__ == "__main__":
    print(CacheHandler.get_cache_folders())