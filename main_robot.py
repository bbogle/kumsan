from MotorModule import Motor
from LaneModule import getLaneCurve
import WebcamModule as webcam
import utils
import cv2

##################################################
motor = Motor(2,3,4,17,22,27)
##################################################

def main():
    img = webcam.getImg()
    curveVal = getLaneCurve(img,display=1)
    #print(curveVal)

    sen = 1.3   # SENSITIVITY
    maxVAl= 0.3 # MAX SPEED
    if curveVal>maxVAl:curveVal = maxVAl
    if curveVal<-maxVAl: curveVal =-maxVAl
    if curveVal>0:
        sen =1.7
        if curveVal<0.05: curveVal=0
    else:
        if curveVal>-0.08: curveVal=0
    motor.move(0.35,-curveVal*sen,0.05)
    #cv2.waitKey(1)

if __name__ == '__main__':
    initialTrackBarVals = [102, 80, 20, 214]
    utils.initializeTrackbars(initialTrackBarVals)
    frameCounter = 0
    while True:
        frameCounter +=1
        main()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
