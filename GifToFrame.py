import os
from PIL import Image
import string

alphabet = string.ascii_uppercase

def getName(frameN):
    remain, lsl = divmod(frameN, 26) # LeastSigLetter
    msl, mid = divmod(remain, 26) # MostSigLetter, Middle
    name = alphabet[msl]+alphabet[mid]+alphabet[lsl] # Name
    print("Saving frame {}".format(name))
    
    return name

def getGIFLen(inGif):
    gif = Image.open("{}.gif".format(inGif))
    gifLen = 0
    try:
        while True:
            gif.seek(gif.tell()+1)
    except EOFError:
        return gifLen

def createFolder(path):
    folder = 0
    while True:
        newPath = path + str(folder)
        if not os.path.exists(newPath):
            os.makedirs(newPath)
            break
        else:
            folder += 1

    return newPath

def extractFrames(inGif, outFolder):
    frame = Image.open(inGif)
    nframes = 0
    outFolder = createFolder(outFolder)
    while frame:
        frame.convert("RGB").save('{}/{}.jpg'.format(outFolder,getName(nframes)), optimize=True, quality=95) #Convert and output
        nframes += 1
        try:
            frame.seek(nframes)
        except EOFError: # Detect end of GIF
            break

gifs = []
wDir = os.path.dirname(os.path.realpath(__file__)) # Working Dir
for file in os.listdir(".\\gifs"): # Get all files in the /gifs dir
    if file.endswith(".gif"): # Get all GIFs in found files
        gifs.append(wDir+"\\gifs\\"+file) # Add GIF to our output list

if len(gifs) == 0:
    print("Please place at least 1 gif into the './gifs/' folder to continue!")

for g in gifs: # Choose each GIF
    print("Working on: {}".format(g))
    extractFrames(g,'output\\') # Extract the frames
    print("Finished: {}\nNow moving GIF to './gifs/done/'!".format(g))
    # Move our GIF to /done
    tmpH, tmpT = os.path.split(g) # Temp Head and Temp Tail
    os.rename(g, tmpH+"//done//"+tmpT)
