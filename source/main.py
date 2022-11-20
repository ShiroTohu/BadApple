from PIL import Image
from tqdm import tqdm
from colorama import just_fix_windows_console
from file_handler import FileHandler

import argparse
import numpy as np
import pygame
import os
import sys

__author__ = "ShiroTohu"

class Video():
    # initiates the Files class with file variables
    def __init__(self, directory = "output/", prefix = "out", filetype = ".png", music_path = "output/audio.mp3", fps = 30):
        # Information about the Music Video.
        self.music_path = music_path
        self.directory = directory
        self.prefix = prefix
        self.filetype = filetype
        self.fps = fps

        self.images_to_render = self.images_to_render()
        self.amount_of_frames = len(self.images_to_render)
        self.time_between_frames = (1000 / self.fps) # records it in miliseconds
        self.song_length_miliseconds = len(self.images_to_render) / self.fps * 1000

    def play_music(self):
        pygame.mixer.music.load(self.music_path)
        pygame.mixer.music.set_volume(0.05)
        pygame.mixer.music.play()

    def audio_position(self):
        return pygame.mixer.music.get_pos()

    # returns a list of images to render in directory form, that is why it is in the Files class
    def images_to_render(self) -> list:
        number_of_frames = len(os.listdir(self.directory))
        to_render = []
        for number in range(number_of_frames - 2): # TODO please fix!
            to_render.append(f"{self.directory}{self.prefix}{number + 1}{self.filetype}")
        return to_render

# renders the entire video
class PreRender():
    # starts the PreRender process
    def __init__(self, video : Video, coloums = 80, scale = 0.43): # ! to change resolution, change the amount of coloums not the scale!
        self.frames = [] # where the video frames are stored
        self.amount_of_frames = len(self.frames)
        self.coloums = coloums
        self.scale = scale # The scale is used to find out the how many rows there should be in terms of height
        self.video = video

        for image in tqdm(self.video.images_to_render):
            self.frames.append(self.render_image(image))

        FileHandler.save_frames(self.frames, )

    # renders image as ASCII, copy and pasted from geeks for geeks because too hard to read
    def render_image(self, image_path):
        gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
        image = Image.open(image_path).convert('L')
        # store dimensions
        W, H = image.size[0], image.size[1]
    
        # compute width of tile
        w = W/self.coloums
    
        # compute tile height based on aspect ratio and scale
        h = w/self.scale
    
        # compute number of rows
        rows = int(H/h)
    
        # check if image size is too small
        if self.coloums > W or rows > H:
            print("Image too small for specified cols!")
            exit(0)

        aimg = []
        for j in range(rows):
            y1 = int(j*h)
            y2 = int((j+1)*h)
    
            # correct last tile
            if j == rows-1:
                y2 = H
    
            # append an empty string
            aimg.append("")
    
            for i in range(self.coloums):
    
                # crop image to tile
                x1 = int(i*w)
                x2 = int((i+1)*w)
    
                # correct last tile
                if i == self.coloums-1:
                    x2 = W
    
                # crop image to extract tile
                img = image.crop((x1, y1, x2, y2))
    
                # get average luminance
                avg = int(PreRender.get_average_light(img))
                gsval = gscale1[int((avg*69)/255)]
    
                # append ascii char to string
                aimg[j] += gsval

        string = ""
        for row in aimg:
            string += f"{row}\n"

        return string

    @staticmethod
    def get_average_light(image):
        # get image as numpy array
        im = np.array(image)
    
        # get shape
        w,h = im.shape
    
        # get average
        return np.average(im.reshape(w*h))

class Renderer(PreRender):
    def __init__(self, video : Video):
        super().__init__(video)
        self.video = video
        self.main()

    # main render loop YEPCOCK
    def main(self):
        while True:
            input("play: ")
            os.system('cls')
            self.video.play_music()
            next_frame = self.video.time_between_frames
            for frame in self.frames:
                while self.video.audio_position() < next_frame:
                    self.print_frame(frame)
                next_frame += self.video.time_between_frames

    def print_frame(self, frame):
        sys.stdout.write(f"\033[1;1f{frame}")
        sys.stdout.flush()

def main(): # I hope this works...
    # Argparse
    parser = argparse.ArgumentParser(description = "Takes a Video and outputs it as ASCII text supports file reading and writing.")
    # parser.add_argument('video', help='either a JSON save file or a video that is a mp4, mov etc... (include video extension or .json)')
    parser.add_argument('--fps', type=int, help = 'the fps of the video')
    parser.add_argument("-v", "--verbosity", action="count", default=0, help="increase output verbosity, goes up to 2, default set to 0")

    parser.add_argument('--audio', help='the name of the audio file')
    parser.add_argument('--image_prefix', help='the prefix before the image frame, default is set to "out", generally doesn\'t really need to be changed')
    parser.add_argument('--image_filetype', help='filetype of the images that are rendered')
    parser.add_argument('-o', '--output', help = 'Where the picture files and audio are outputted to')

    parser.add_argument('--clear_render_chache', help='program stores the JSON files of already rendered videos so that they can tone down render times.')

    args = parser.parse_args()

    just_fix_windows_console()
    pygame.init()

    video = Video(directory = "output/", prefix = "out", filetype = ".png", music_path = "output/audio.mp3", fps = 30) # ! change video settings here
    Renderer(video)

# for debugging purposes
if __name__ == "__main__":
    pass