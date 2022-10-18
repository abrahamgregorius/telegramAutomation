from time import sleep, time
import uiautomator2 as u2
import os
import main

d = u2.connect('R9CT4007GBM')


device_id = "R9CT4007GBM"
packagename = "org.telegram.messenger"
filename = "videoplayback.mp4"


def startApp():
    os.system(f'adb shell  am start -n org.telegram.messenger/org.telegram.messenger.DefaultIcon')

def sendMessage(message):
    split = [*message.upper()]
    for i in split:
        if i == " ":
            main.pressKey("SPACE")
        main.pressKey(i)
    main.pressSend()

def getChatroom(targetnumber):
    os.system(f'adb -s '+ device_id +' shell am start -a android.intent.action.VIEW -d https://t.me/+'+ targetnumber +' org.telegram.messenger ')

def sendVideo():
    os.system(f'adb -s '+ device_id +' push MEDIA/'+ filename +' /storage/emulated/0/DCIM/')


getChatroom("6285811403649")
sleep(2)
sendMessage("Hello world")