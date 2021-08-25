import cv2
import numpy as np

PATH = 'snapshots/'
file_list_name = 'snapshot_file_list.txt'
click_list = 'click_list.txt'

logo = cv2.imread('logo.png')

LOGO_WIDTH = 42
LOGO_HEIGHT = 42

fo = open(file_list_name, "r")
clk_cmd = open(click_list, "a")

while True:
    file_name = fo.readline().rstrip()
    if file_name != '':
        print(file_name)
        clk_cmd.write(file_name + '\n')
        clk_cmd.flush()
        snapshot = cv2.imread(file_name)
        result_group_logo = cv2.matchTemplate(snapshot, logo, cv2.TM_SQDIFF_NORMED)
        
        threshold = 0.06
        loc = np.where(result_group_logo <= threshold)

        is_first = True

        for pt in zip(*loc[::-1]):
            if is_first:
                is_first = False
                mid_pos = (pt[0] + LOGO_WIDTH/2, pt[1] + LOGO_HEIGHT/2)
                clk_cmd.write(str(mid_pos[0])+','+str(mid_pos[1])+'\n')
                clk_cmd.flush()
            else:
                if pt[0] - mid_pos[0] < 5 and pt[1] - mid_pos[1] < 5:
                    pass
                else:
                    mid_pos = (pt[0] + LOGO_WIDTH/2, pt[1] + LOGO_HEIGHT/2)
                    clk_cmd.write(str(mid_pos[0])+','+str(mid_pos[1])+'\n')
                    clk_cmd.flush()
