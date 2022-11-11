from time import sleep
import os
import re
import uiautomator2 as u2
import random
import subprocess

class TeleHelper:
    device_id = "R9CT300FQRE"
    numdata = ["81311951704", "85811403517", "85892284244", "895410810690"] 
    d = u2.connect(device_id)

    def __init__(self):
        pass

    def adbs(self, command):
        a = subprocess.run(command, capture_output=True)
        return a.stdout.decode()

    def startApp(self):
        os.system(f'adb -s '+ self.device_id +' shell am start -n org.telegram.messenger/org.telegram.messenger.DefaultIcon')

    def pressKey(self, keycode):
        key = keycode.upper()
        os.system(f'adb -s '+ self.device_id +' shell input keyevent KEYCODE_' + key)

    def pressSend(self):
        os.system(f'adb -s ' + self.device_id + ' shell input tap 985 2230') 

    def generateNumber(self):
        number = random.choice(self.numdata)
        return number
    
    def getChatroom(self, number):
        os.system(f'adb -s '+ self.device_id +' shell am start -a android.intent.action.VIEW -d https://t.me/+62'+ number +' org.telegram.messenger')

    def sendMessage(self, number, message):
        self.getChatroom(number)
        split = [*message.upper()]
        for i in split:
            if i == " ":
                self.pressKey("SPACE")
                sleep(0.3)
            self.pressKey(i)
            sleep(0.3)
        self.pressSend()
        sleep(0.3)

    def sendPhoto(self, number, message):
        self.getChatroom(number)
        sleep(1)

        split = [*message.upper()]
        for i in split:
            if i == " ":
                self.pressKey("SPACE")
                sleep(0.3)
            self.pressKey(i)

        sleep(.5)
        os.system(f'adb -s '+ self.device_id +' push MEDIA/nature.jpg /storage/emulated/0/DCIM/')
        os.system(f'adb -s '+ self.device_id +' shell am start -a android.intent.action.SEND -t  text/plain -e jid "62123" --eu android.intent.extra.STREAM file:///storage/emulated/0/DCIM/nature.jpg -p org.telegram.messenger')
        os.system(f'adb -s '+ self.device_id +' shell input tap 270 570')
        sleep(1)
        os.system(f'adb -s '+ self.device_id +' shell input tap 970 2150')
        sleep(1)
        os.system(f'adb -s '+ self.device_id +' shell input tap 970 2150')
        sleep(1)
        
    def sendVideo(self, number, message):
        self.getChatroom(number)
        sleep(1)
        
        split = [*message.upper()]
        for i in split:
            if i == " ":
                self.pressKey("SPACE")
                sleep(0.3)
            self.pressKey(i)

        sleep(1)
        self.pressSend()
        sleep(.8)
        os.system(f'adb -s '+ self.device_id +' push MEDIA/video.mp4 /storage/emulated/0/DCIM/')
        os.system(f'adb -s '+ self.device_id +' shell am start -a android.intent.action.SEND -t  text/plain -e jid "62123" --eu android.intent.extra.STREAM file:///storage/emulated/0/DCIM/video.mp4 -p org.telegram.messenger')
        sleep(1)
        os.system(f'adb -s '+ self.device_id +' shell input tap 270 570')
        sleep(1)
        os.system(f'adb -s '+ self.device_id +' shell input tap 970 2150')
        sleep(1)
        os.system(f'adb -s '+ self.device_id +' shell input tap 970 2150')

    def checkActivity(self):
        a = self.adbs(f'adb -s '+ self.device_id +' shell dumpsys activity activities | grep -E "mFocusedApp"')
        b = a.split()
        print(b)

    def checkCall(self):
        self.adbs("adb -s "+ self.device_id +" shell uiautomator dump")
        sleep(2)
        self.adbs("adb -s "+ self.device_id +" pull /storage/self/primary/window_dump.xml")
        sleep(2)
        pattern = re.compile("(\+62 ((\d{3}([ -]\d{3,})([- ]\d{4,})?)|(\d+)))|(\(\d+\) \d+)|\d{3}( \d+)+|(\d+[ -]\d+)|\d+")
        

    def makeCall(self, number):
        self.getChatroom(number)
        sleep(3)
        os.system(f'adb -s  '+ self.device_id +' shell input tap 865 200')
        sleep(5)
        try:
            d(text="While using the app").click()
        except:
            print("There is no permission request")
        finally:
            os.system(f'adb -s  '+ self.device_id +' shell input tap 940 2140')
            sleep(1)

    def mainFunc(self, number, message):
        try:
            self.sendMessage(number, "**"+ message)
        except:
            print("The number is not a valid number or it is not registered on Telegram")
        finally:
            print("The program is shutting down...")

    def mainFuncMedia(self, number, message):
        try:
            self.sendVideo(number, message)
        except:
            print("The number is not a valid number or it is not registered on Telegram")
        finally:
            print("The program is shutting down...")

    # def changeAccount(self):
    #     coordinates = {"a":"400 616", "b":"400 750"}
    #     a = random.choice(list(coordinates.values()))
    #     os.system(f'adb -s '+ self.device_id +' shell input tap 90 200')
    #     sleep(1)
    #     os.system(f'adb -s '+ self.device_id +' shell input tap '+ a +'')

helpz = TeleHelper()

while True:
    helpz.makeCall(helpz.generateNumber())
    