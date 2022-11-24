# This module is responsible of taking the video and outputting it as images and audio, this will be outputted to the "output" folder
# keep in mind that this folder will be deleted each time a new render process is initiated.
#! output/

import os
import ffmpeg

class VideoToOutput:
    def __init__(self, videopath):
        if not (os.path.exists("../output2")):
            os.mkdir("../output2")

        os.system(f"ffmpeg -i {videopath} ../output2/out%d.png")
        os.system(f"ffmpeg -i {videopath} ../output2/audio.mp3")

    def foo():
        pass

if __name__ == "__main__":
    VideoToOutput("D:\\Mine\\Programming\\BadApple\\RL.mp4")

