from PIL import Image
from tqdm import tqdm
from colorama import just_fix_windows_console

from source.cache import CacheHandler
from source.file import FileToOutput, File

import argparse
import numpy as np
import pygame
import os
import sys

__author__ = "ShiroTohu"

# converts images from the video into ASCII text and stores it to bve rendered
class PreRender():
    def __init__(self, file : File, coloums = 80, scale = 0.43): # ! to change resolution, change the amount of coloums not the scale!
        self.frames = [] # where the video frames are stored
        self.amount_of_frames = len(self.frames)
        self.coloums = coloums
        self.scale = scale # The scale is used to find out the how many rows there should be in terms of height
        self.file = file

        print(f"{self.file.stripped_file_name} | {CacheHandler.get_cache_folders()}")
        if self.file.stripped_file_name in CacheHandler.get_cache_folders():
            print(f"D:\Mine\Programming\BadApple\cache\{self.file.stripped_file_name}\\frames.json")
            self.frames = CacheHandler.load_file(f"D:\Mine\Programming\BadApple\cache\{self.file.stripped_file_name}\\frames.json")["frames"]
        else:
            for image in tqdm(self.file.frames_to_render):
                self.frames.append(self.render_image(image))
            CacheHandler.save_rendered_information(self.frames, self.file.stripped_file_name, self.coloums, self.scale)

# converts a singular image into ASCII text and returns it as a string
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

# honestly I have no clue so don't touch it.
    @staticmethod
    def get_average_light(image):
        # get image as numpy array
        im = np.array(image)
    
        # get shape
        w,h = im.shape
    
        # get average
        return np.average(im.reshape(w*h))

# This class is what allows the PreRendered frames to be displayed onto the terminal
class Renderer(PreRender):
    def __init__(self, file : File):
        super().__init__(file)
        self.file = file
        self.main()

# main method that allows everything to work properly, and adds usability to the render loop.
    def main(self):
        while True:
            input("play: ")
            os.system('cls')
            self.file.play_music()
            self.render_loop()

# shows the frames in in sync with the music, method added for modularisation
    def render_loop(self):
        next_frame = self.file.time_between_frames
        for frame in self.frames:
            while self.file.audio_position() < next_frame:
                self.print_frame(frame)
            next_frame += self.file.time_between_frames

# prints a singular frame
    def print_frame(self, frame):
        sys.stdout.write(f"\033[1;1f{frame}")
        sys.stdout.flush()

# The program arguments
def program_arguments():
    # Argparse
    parser = argparse.ArgumentParser(description = "Takes a Video and outputs it as ASCII text supports file reading and writing.")
    parser.add_argument('path', help='either a JSON save file or a video that is a mp4, mov etc... (include video extension or .json)')
    parser.add_argument("-v", "--verbosity", action="count", default=0, help="increase output verbosity, goes up to 2, default set to 0")

    return parser.parse_args()

def main():
    just_fix_windows_console()
    pygame.init()

    args = program_arguments()

    file = File(args.path)
    output = FileToOutput(file)
    Renderer(file)

if __name__ == "__main__":
    main()