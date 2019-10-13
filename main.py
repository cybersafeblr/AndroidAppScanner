#Created by Gagan Jain @ CyberSafe Bangalore
import os
import time
from loaders import TextLoader

# checking for connected devices
device = os.popen("adb devices").read().split("device")[0].strip()
print("CyberSafe Android Scanner")
loader = TextLoader(duration=10)
loader.run()
connect = os.popen("adb connect " + device ).read()
print(connect)
scan = os.system("adb shell pm list packages -3 > out.txt")
print("Scan results exported")
