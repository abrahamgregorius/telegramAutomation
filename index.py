from time import sleep
import os
import main
import uiautomator2 as u2

# UIAutomator init
d = u2.connect("R9CT300FQRE")

device_id = "R9CT300FQRE"

packagename = "org.telegram.messenger"
filename = "videoplayback.mp4"
namefile = "nature.jpg"

def startApp():
    os.system(f'adb shell am start -n org.telegram.messenger/org.telegram.messenger.DefaultIcon')

def sendMessage(message):
    split = [*message.upper()]
    for i in split:
        if i == " ":
            main.pressKey("SPACE")
        main.pressKey(i)
    main.pressSend()

def getChatroom(targetnumber):
    os.system(f'adb -s '+ device_id +' shell am start -a android.intent.action.VIEW -d https://t.me/+'+ targetnumber +' org.telegram.messenger')

def getVideo():
    os.system(f'adb -s '+ device_id +' push '+ filename +' /storage/emulated/0/DCIM/')
    os.system(f'adb -s '+ device_id +' shell am start -a android.intent.action.SEND -t  text/plain -e jid "62123" --eu android.intent.extra.STREAM file:///storage/emulated/0/DCIM/'+ filename +' -p '+ packagename +'')
    os.system(f'adb -s '+ device_id +' shell input tap 270 570')
    os.system(f'adb -s '+ device_id +' shell input tap 970 2160')

def sendVideo(targetnumber):
    getChatroom(targetnumber)
    sleep(2)
    # The message is for putting the chat to be the most recent chat
    sendMessage("x")
    getVideo()
    

def getPhoto():
    os.system(f'adb -s '+ device_id +' push '+ namefile +' /storage/emulated/0/DCIM/')
    os.system(f'adb -s '+ device_id +' shell am start -a android.intent.action.SEND -t  text/plain -e jid "62123" --eu android.intent.extra.STREAM file:///storage/emulated/0/DCIM/'+ namefile +' -p '+ packagename +'')
    os.system(f'adb -s '+ device_id +' shell input tap 270 570')
    for i in range(3):
        os.system(f'adb -s '+ device_id +' shell input tap 970 2160')
    
def sendPhoto(targetnumber):
    getChatroom(targetnumber)
    sleep(2)
    # The message is for putting the chat to be the most recent chat
    sendMessage("x")
    getPhoto()


# def changeAccount():
#    os.system(f'adb -s '+ device_id +' shell input tap 90 200')
#    d(className="android.widget.ImageView").click()
    
    
        
# getChatroom("6285811403649")62859141490060
# sleep(2)
# sendMessage("Hello world")0858 1140 3517

    
changeAccount()