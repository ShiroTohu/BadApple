# This module is responsible of taking the video and outputting it as images and audio, this will be outputted to the "output" folder
# keep in mind that this folder will be deleted each time a new render process is initiated.
#! output/

import os
from shutil import rmtree
import ffmpeg
from pprint import pprint

__author__ = "ShiroTohu"

# contains metadata and directory information from the file parsed
class File:
    def __init__ (self, full_file_path):
        self.full_file_path = full_file_path
        self.file_name = self.get_file_name(full_file_path)
        self.stripped_file_name = self.get_stripped_name(self.file_name)
        self.filetype = self.get_filetype(self.file_name)

        self.metadata = self.get_metadata()
        self.frame_rate = self.get_framerate()
        self.amount_of_frames = self.get_amount_of_frames()

    # this is here because it has to deal with the actual video itself not the JSON curd the Video class hasn to deal with.
    def get_metadata(self) -> dict:
        video_metadata = ffmpeg.probe(self.full_file_path)["streams"][0] # here for readability
        return video_metadata

    def get_framerate(self) -> int:
        frame_rate = self.metadata["r_frame_rate"]
        return int(frame_rate[:-(len(frame_rate) - frame_rate.index("/"))]) # instead of 30/1 it returns just 30, because we know that most videos that are inputted are in frames per second not frames per 30 minutesloloololoplo

    def get_amount_of_frames(self) -> int:
        return int(self.metadata["nb_frames"])

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

# strips the images and audio from the video and outputs it to the "output" folder
class FileToOutput(File):
    # the name of the output images and audio are set here
    def __init__(self, full_file_path):
        File.__init__(self, full_file_path)
        self.output_folder = "../output"
        self.full_file_path = full_file_path

        self.audio_name = "audio.mp3"
        self.audio_path = f"{self.output_folder}/{self.audio_name}"

        self.prefix = "out"
        self.image_name = f"{self.prefix}%d.png"
        self.image_path = f"{self.output_folder}"

        self.convert_video()

# strips the images and audio from the video into the "output" folder
    def convert_video(self):
        if os.path.exists(self.output_folder):
            rmtree(self.output_folder)
        os.mkdir(self.output_folder)

        os.system(f"ffmpeg -i {self.full_file_path} {self.image_path}/{self.image_name}")
        os.system(f"ffmpeg -i {self.full_file_path} {self.audio_path}")

if __name__ == "__main__":
    x = FileToOutput("D:\\Mine\\Programming\\BadApple\\test.mp4")
    metadata = x.get_metadata()
    pprint(metadata)