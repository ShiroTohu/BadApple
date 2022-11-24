# ASCII Player
An ASCII video player for the windows terminal. Currently unable to take in an mp4, instead the video frames and audio need to be manually extracted.
To make a video compatable use ffmpeg and type the following:

1. ```ffmpeg -i video.mp4 out%d.png```
2. ```ffmpeg -i video.mp4 audio.mp3```

Keep in mind that the program takes in audio.mp3 and out*number*.png, any other names will not work
unless specified changed in the code. As you can see there are alot of manual labour needed to produce
the required outcome therefore:

- [x] output video as ASCII text
- [ ] autoconversion to ASCII text
- [ ] mp4 input program arguments
- [ ] JSON save feature (to reduce loading times)
- [ ] settings

## Package Requirements
To install the packages required to run the program you'll need to install the dependencies needed to run the program which can be installed with:

```pip install -r REQUIREMENTS.txt```

## Sample Images
<img src="images/image1.JPG" alt="example image 1" width="700"/>
<img src="images/image2.JPG" alt="example image 2" width="700"/>