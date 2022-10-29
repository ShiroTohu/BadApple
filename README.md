# ASCII player
this is an ASCII video player for the terimal, currently there is no way to import a mp4, you have to run it through ffmpeg twice
where the first time you convert the video into images preferably with out%d.png and then export the audio; as audio.mp3. There is
currently also no way to save video's frames so that you don't have to render them beforehand.
```ffmpeg -i video.mp4 out%d.png```
```ffmpeg -i video.mp4 audio.mp3```

## images
![example image 1](images/image1.jpg)
![example image 2](images/image2.jpg)

## requirements
- pygame
- PIL
- tqdm
- colorama
- numpy