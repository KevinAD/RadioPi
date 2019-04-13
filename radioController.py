import os

PLAYER_STRING = "sox -t mp3 {} -t wav - | sudo /etc/PiFmRds/src/pi_fm_rds -freq {} -audio -"

def getFileContents(dirPath):
    files = []
    for f in os.listdir(dirPath):
            if os.path.isfile(os.path.join(dirPath,f)):
                files.append(os.path.join(dirPath,f))
            else:
                files = files + getFileContents(os.path.join(dirPath,f))
    return files

def playSong(filePath,freq):
    os.system(PLAYER_STRING.format(filePath,freq))


playSong(getFileContents("mp3")[0],'87.5')
