# This module is responsible of taking the video and outputting it as images and audio, this will be outputted to the "output" folder
# keep in mind that this folder will be deleted each time a new render process is initiated.
#! output/

import os
import ffmpeg
from pprint import pprint

__author__ = "ShiroTohu"

class File:
    def __init__ (self, full_file_path):
        self.full_file_path = full_file_path
        self.file_name = self.get_file_name(full_file_path)
        self.stripped_file_name = self.get_stripped_name(self.file_name)
        self.filetype = self.get_filetype(self.file_name)

    # TODO: this is not clean code, it's like... terrible code lmao, hard to read
    @staticmethod
    def get_file_name(full_file_path):
        return os.path.basename(full_file_path).split('/')[-1]

    @staticmethod
    def get_stripped_name(file_name):
        return file_name[:file_name.index('.' + file_name.split('.')[-1])]

    @staticmethod
    def get_filetype(file_name):
        return '.' + file_name.split('.')[-1]

class VideoToOutput(File):
    # named argument file instead of video so to not confuse with the Video class
    # takes in the full file path to specified video.
    def __init__(self, full_file_path):
        File.__init__(self, full_file_path)
        self.output_folder = "../output2/"
        self.full_file_path = full_file_path
        self.metadata = self.get_metadata()

        self.frame_rate = self.get_framerate()
        # vairables for full_path, file, file_name

    def convert_video(self):
        if os.path.exists("../output2"):
            os.remove("../output2")
        os.mkdir("../output2")

        #! there might be a better way of doing this, but python-ffmpeg is just a wrapper so this is just as efficient.
        os.system(f"ffmpeg -i {self.videopath} {self.output_folder}out%d.png")
        os.system(f"ffmpeg -i {self.videopath} {self.output_folder}audio.mp3")

    def get_framerate(self) -> int:
        frame_rate = self.metadata["r_frame_rate"]
        return int(frame_rate[:-(len(frame_rate) - frame_rate.index("/"))]) # instead of 30/1 it returns just 30, because we know that most videos that are inputted are in frames per second not frames per 30 minutesloloololoplo

    # strips .mp4 off the end of the str given
    def strip_file_extension(file) -> "str":
        file_name = file[:-(len(file) - file.index("."))]
        return file_name

    # this is here because it has to deal with the actual video itself not the JSON curd the Video class hasn to deal with.
    def get_metadata(self) -> dict:
        video_metadata = ffmpeg.probe(self.full_file_path)["streams"][0] # here for readability
        return video_metadata

if __name__ == "__main__":
    x = VideoToOutput("D:\\Mine\\Programming\\BadApple\\output\\test.mp4")
    metadata = x.get_metadata()
    pprint(metadata)