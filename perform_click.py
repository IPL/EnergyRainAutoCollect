import time
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage

SPEED = 314 #pixel/second
click_list = 'click_list.txt'

print('Before connected')
device = MonkeyRunner.waitForConnection()
print('After connected')

clk_cmd = open(click_list, "r")

def click():
    click_cnt = 0
    while True:
        cmd = clk_cmd.readline().rstrip()
        if cmd != '':
            a = cmd.split(',')
            if len(a) == 2:
                curr_time = time.time()
                time_diff = curr_time - snap_time
                time_offset = SPEED * time_diff + 1

                pos_x = int(float(a[0]))
                pos_y = int(float(a[1])+time_offset)

                click_cnt = click_cnt + 1
                print('Command: ', str(click_cnt), time.time(), 'device.touch(' + str(pos_x) + ',' + str(pos_y) + ',DOWN_AND_UP)')
                device.touch(pos_x, pos_y, 'DOWN_AND_UP')
                print('Command time cost: ', time.time())
                # MonkeyRunner.sleep(0.017)
            else:
                snap_time = float(cmd.split('/')[1].split('_')[1].split('.png')[0])
                print('File is: ', cmd, snap_time)

click()
