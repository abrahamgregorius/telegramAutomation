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
    os.system(f'adb -s '+ device_id +' shell am start -a android.intent.action.VIEW -d https://t.me/+'+ targetnumber +' org.telegram.messenger')

def sendVideo(targetnumber):
    os.system(f'adb -s '+ device_id +' push '+ filename +' /storage/emulated/0/DCIM/')
    os.system(f'adb -s '+ device_id +' shell am start -a android.intent.action.SEND -t  text/plain -e jid "'+ targetnumber +'" --eu android.intent.extra.STREAM file:///storage/emulated/0/DCIM/'+ filename +' -p '+ packagename+'')

# getChatroom("6285811403649")62859141490060
# sleep(2)
# sendMessage("Hello world")0858 1140 3517

sendMessage("hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world")