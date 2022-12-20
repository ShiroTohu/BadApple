# This module is responsible of taking the video and outputting it as images and audio, this will be outputted to the "output" folder
# keep in mind that this folder will be deleted each time a new render process is initiated.
#! output/

import os
import ffmpeg
import pygame

from shutil import rmtree
from pprint import pprint

__author__ = "ShiroTohu"

class Output:
    output_folder = "output/"
    audio_name = "audio.mp3"
    prefix = "out"
    audio_path = f"{output_folder}/{audio_name}"

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

        self.frames_to_render = self.get_frames_to_render()
        self.amount_of_frames = len(self.frames_to_render)
        self.time_between_frames = (1000 / self.frame_rate) # records it in miliseconds
        self.song_length_miliseconds = len(self.frames_to_render) / self.frame_rate * 1000

    # this is here because it has to deal with the actual video itself not the JSON curd the Video class hasn to deal with.
    def get_metadata(self) -> dict:
        video_metadata = ffmpeg.probe(self.full_file_path)["streams"][0] # here for readability
        return video_metadata

    def get_framerate(self) -> int:
        frame_rate = self.metadata["r_frame_rate"]
        return int(frame_rate[:-(len(frame_rate) - frame_rate.index("/"))]) # instead of 30/1 it returns just 30, because we know that most videos that are inputted are in frames per second not frames per 30 minutesloloololoplo

    def get_amount_of_frames(self) -> int:
        return int(self.metadata["nb_frames"])

    # returns the name of each frame to render
    def get_frames_to_render(self) -> list:
        number_of_frames = self.amount_of_frames
        to_render = []
        for number in range(number_of_frames):
            to_render.append(f"{Output.output_folder}/{Output.prefix}{number + 1}.png")
        return to_render

    # plays the music using the pygame mixer
    def play_music(self):
        pygame.mixer.music.load(Output.audio_path)
        pygame.mixer.music.set_volume(0.05)
        pygame.mixer.music.play()

    # returns the position of the audio in miliseconds
    def audio_position(self):
        return pygame.mixer.music.get_pos()

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
class FileToOutput:
    # the name of the output images and audio are set here
    def __init__(self, file: File):
        self.full_file_path = file.full_file_path
        self.audio_path = f"{Output.output_folder}/{Output.audio_name}"
        self.image_name = f"{Output.prefix}%d.png"
        self.image_path = Output.output_folder
        self.convert_video()

# strips the images and audio from the video into the "output" folder
    def convert_video(self):
        if os.path.exists(Output.output_folder):
            rmtree(Output.output_folder)
        os.mkdir(Output.output_folder)

        os.system(f"ffmpeg -i {self.full_file_path} {self.image_path}/{self.image_name}")
        os.system(f"ffmpeg -i {self.full_file_path} {self.audio_path}")

if __name__ == "__main__":
    x = FileToOutput("D:\\Mine\\Programming\\BadApple\\test.mp4")
    metadata = x.get_metadata()
    pprint(metadata)