from time import sleep
import random
import os
import main
import uiautomator2 as u2

device_id = "R9CT300FQRE"
d = u2.connect(device_id)

packagename = "org.telegram.messenger"
filename = "videoplayback.mp4"
namefile = "nature.jpg"

def startApp():
    os.system(f'adb shell am start -n org.telegram.messenger/org.telegram.messenger.DefaultIcon')

