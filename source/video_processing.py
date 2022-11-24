# This module is responsible of taking the video and outputting it as images and audio, this will be outputted to the "output" folder
# keep in mind that this folder will be deleted each time a new render process is initiated.
#! output/

import os
import ffmpeg

__author__ = "ShiroTohu"

class VideoToOutput:
    def __init__(self, video_path):
        self.output = "output2"
        self.video_path = video_path
        self.metadata = self.get_metadata(video_path)

        self.frame_rate = self.get_framerate()

    def convert_video(self):
        if os.path.exists("../output2"):
            os.remove("../output2")
        os.mkdir("../output2")

        #! there might be a better way of doing this, but python-ffmpeg is just a wrapper so this is just as efficient.
        os.system(f"ffmpeg -i {self.videopath} ../{self.output}/out%d.png")
        os.system(f"ffmpeg -i {self.videopath} ../{self.output}/audio.mp3")

    def get_framerate(self) -> int:
        frame_rate = self.metadata["r_frame_rate"]
        return int(frame_rate[:-(len(frame_rate) - frame_rate.index("//"))]) # instead of 30/1 it returns just 30, because we know that most videos that are inputted are in frames per second not frames per 30 minutesloloololoplo

    # this is here because it has to deal with the actual video itself not the JSON curd the Video class hasn to deal with.
    @staticmethod
    def get_metadata(video_path) -> dict:
        video_metadata = ffmpeg.probe(video_path)["streams"][0] # here for readability
        return video_metadata


if __name__ == "__main__":
    x = VideoToOutput("D:\\Mine\\Programming\\BadApple\\output\\test.mp4")
    metadata = x.get_metadata()[0]
    print(metadata["r_frame_rate"][:-2])

