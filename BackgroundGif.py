import ctypes, time, os, sys
os.system("cls")
os.system("color 1A")
print("""
*******************************************************************************
***************** WELCOME TO JAMES' GIF-TO-BACKGROUND-PROGRAM *****************
*******************************************************************************
""")

def changeBackground(background):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, background.lower() , 0)

def main():
    gifNo = int(input("Gif number: "))
    dir_path = os.path.dirname(os.path.realpath(__file__))
    pathToGif = dir_path+"//output//"+str(gifNo)

    files = []
    for (dirpath, dirnames, filenames) in os.walk(pathToGif):
        files.extend(filenames)
        break

    files.sort()
    print(files)
    
    while True:
        for file in files:
            changeBackground(pathToGif+"\\"+str(file))
            time.sleep(0.02)

def run():
   while True:
       try:
            main()
            
       except KeyboardInterrupt:
            print("Interrupted...\nPress CTL+C again to close")
            try:
                for i in range(1):
                    time.sleep(1)
                    print("waiting "+str(i)+"...")
                    
            except KeyboardInterrupt:
                print("Exiting...")
                return
            
if __name__ == '__main__':
    run()
