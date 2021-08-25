import time, threading
import os
import datetime

PATH = 'snapshots/'
file_list_name = "snapshot_file_list.txt"
sleeptime = 0
click_list = 'click_list.txt'


def clickByThread():
    t = threading.Thread(target=click)
    t.start()


def androidshot():
    fo = open(file_list_name, "w")
    i=0
    while True:
        time_str = str(time.time())
        short_file_name = str(i) + "_" + time_str + ".png"
        os.system('adb shell screencap -p /sdcard/af/' + short_file_name)
        file_name = PATH + short_file_name
        os.system('adb pull /sdcard/af/' + short_file_name + ' ' + file_name)
        fo.write(file_name + '\n')
        fo.flush()
        i = i + 1
        time.sleep(0.2)
    fo.close()
if __name__ == '__main__':
    os.system('bash clean.sh')
    androidshot()
