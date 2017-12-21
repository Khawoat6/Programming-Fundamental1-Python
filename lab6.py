##def trik(list_ball):
##    changing_style = input(" ")
##    list_ball = [1,0,0]
##    for i in changing_style:
##        if(i == 'A'):
##            list_ball[0],list_ball[1] = list_ball[1],list_ball[0]
##        elif(i == 'B'):
##            list_ball[1],list_ball[2] = list_ball[2],list_ball[1]
##        elif(i == 'C'):
##            list_ball[0],list_ball[2] = list_ball[2],list_ball[0]
##        print(list_ball.index(1)+1)

import cv2

def main():
    cv2.namedWindow("preview")
    vc = cv2.VideoCapture(0)
    if vc.isOpened():
        rval,frame = vc.read()
    else:
        rval = False
    while rval:
        cv2.imshow("preview",frame)
        rval,frame = vc.read()
        key = cv2.waitKey(20)
        if key == 27: #press 'ESC' for exit
            cv2.destroyWindow("preview")
            break
    pass

if __name__ == '__main__':
    main()
