from time import sleep
import os
import uiautomator2 as u2
import random


class TeleHelper:
    device_id = "R9CT300FQRE"
    numdata = ["85811403649", "895410810679", "895410810680", "895410808876"]
    d = u2.connect(device_id)

    def __init__(self):
        pass

    def startApp(self):
        os.system(f'adb -s '+ self.device_id +' shell am start -n org.telegram.messenger/org.telegram.messenger.DefaultIcon')

    def pressKey(self, keycode):
        os.system(f'adb -s '+ self.device_id +' shell input keyevent KEYCODE_' + keycode)

    def pressSend(self):
        os.system(f'adb -s ' + self.device_id + ' shell input tap 985 2230') 

    def generateNumber(self):
        number = random.choice(self.numdata)
        return number
    
    def getChatroom(self, number):
        os.system(f'adb -s '+ self.device_id +' shell am start -a android.intent.action.VIEW -d https://t.me/+'+ number +' org.telegram.messenger')

    def sendMessage(self, number, message):
        self.getChatroom(number)
        split = [*message.upper()]
        for i in split:
            if i == " ":
                self.pressKey("SPACE")
            self.pressKey(i)
        self.pressSend()

    def sendPhoto(self, number):
        self.getChatroom(number)
        self.pressKey("x")
        self.pressSend()
        os.system(f'adb -s '+ self.device_id +' push MEDIA/nature.jpg /storage/emulated/0/DCIM/')
        os.system(f'adb -s '+ self.device_id +' shell am start -a android.intent.action.SEND -t  text/plain -e jid "62123" --eu android.intent.extra.STREAM file:///storage/emulated/0/DCIM/nature.jpg -p org.telegram.messenger')
        os.system(f'adb -s '+ self.device_id +' shell input tap 270 570')
        sleep(.4)
        os.system(f'adb -s '+ self.device_id +' shell input tap 970 2150')
        sleep(.4)
        os.system(f'adb -s '+ self.device_id +' shell input tap 970 2150')
        
    def sendVideo(self, number):
        self.getChatroom(number)
        self.pressKey("x")
        self.pressSend()
        os.system(f'adb -s '+ self.device_id +' push MEDIA/video.mp4 /storage/emulated/0/DCIM/')
        os.system(f'adb -s '+ self.device_id +' shell am start -a android.intent.action.SEND -t  text/plain -e jid "62123" --eu android.intent.extra.STREAM file:///storage/emulated/0/DCIM/video.mp4 -p org.telegram.messenger')
        os.system(f'adb -s '+ self.device_id +' shell input tap 270 570')
        sleep(.4)
        os.system(f'adb -s '+ self.device_id +' shell input tap 970 2150')
        sleep(.4)
        os.system(f'adb -s '+ self.device_id +' shell input tap 970 2150')

    def changeAccount(self):
        coordinates = {"a":"400 616", "b":"400 750"}
        a = random.choice(list(coordinates.values()))
        os.system(f'adb -s '+ self.device_id +' shell input tap 90 200')
        sleep(1)
        os.system(f'adb -s '+ self.device_id +' shell input tap '+ a +'')
        

helpz = TeleHelper()
