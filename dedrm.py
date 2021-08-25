import argparse
import os
import time
import sys

parser = argparse.ArgumentParser(description = 'Strip ascm/epub ebook of drm and add to Calibre')
parser.add_argument('ebookPath', type = str, help = 'Path to ebook to process')

args = parser.parse_args()
ebookPath = args.ebookPath.strip()
ebookName = ebookPath.split("\\")[-1]
ebookExt = ebookName.split(".")[-1]

extSupport = ["acsm", "epub"]

print("Processing " + ebookPath)

if ebookExt in extSupport:
    if ebookExt == "acsm":
        # open acsm in default program (should be Adobe Digital Editions)
        print("Opening " + ebookName + " in Adobe Digital Editions")
    elif ebookExt == "epub":
        # open epub in default program (should be Calibre)
        print("Opening " + ebookName + " in Calibre")
    
    command = 'start "" "' + ebookPath + '"'
    print(command)
    os.system(command)
    #os.system("DigitalEditions.exe " + ebookPath)
    
    # wait 30 seconds to make sure everything worked
    wait_time = 30
    print("Waiting for file to process")
    for i in range(wait_time):
        time.sleep(1)

        j = (i + 1)/wait_time
        sys.stdout.write('\r')
        sys.stdout.write("[%-20s] %d%%" % ('='*int(20*j), 100*j))
        sys.stdout.flush()
    print()

    if ebookExt == "acsm":
        # Close Adobe Digital Editions
        print("Closing Adobe Digital Editions")
        os.system("TASKKILL /F /IM DigitalEditions.exe")
    elif ebookExt == "epub":
        # Close Calibre
        print("Closing Calibre")
        os.system("TASKKILL /F /IM calibre.exe")
else:
    print("I don't know what to do with that file")



