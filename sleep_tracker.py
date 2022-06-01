import cv2
import cv2.cv2 as cv2
import mediapipe
import numpy as np
import pandas as pd
import time
mp_pose=mediapipe.solutions.pose
mp_drawing=mediapipe.solutions.drawing_utils
mp_drawing_styles=mediapipe.solutions.drawing_styles
mp_drawing_specs=mp_drawing.DrawingSpec(thickness=10,circle_radius=1,color=(255,255,255))
logs=pd.DataFrame(index=['Time','Position'])
def start_tracking():
    global  logs

    cap = cv2.VideoCapture('./test.mp4')
    temp=None
    z=0
    pose=mp_pose.Pose(min_detection_confidence=0.75,min_tracking_confidence=0.75,model_complexity=0)
    lm_pos=dict()
    while cap.isOpened():
        success, image = cap.read()
        if not success:
          print("Ignoring empty camera frame.")
          # If loading a video, use 'break' instead of 'continue'.
          continue
        image_height,image_width,_=image.shape
        if z==0:
            temp=np.zeros(image.shape,np.float32)
            z=1
        image.flags.writeable = False
        results = pose.process(image)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        if not results.pose_landmarks:
            continue
        def getPos(name):
            nx = int(results.pose_landmarks.landmark[name].x * image_width)
            ny = int(results.pose_landmarks.landmark[name].y * image_height)
            return nx,ny
        nx,ny=getPos(mp_pose.PoseLandmark.NOSE)
        srx,sry=getPos(mp_pose.PoseLandmark.RIGHT_SHOULDER)
        slx,sly=getPos(mp_pose.PoseLandmark.LEFT_SHOULDER)
        # print(
        #     f'Nose coordinates: ('
        #     f'{nx}, '
        #     f'{ny})'
        # )
        mx=int(min([results.pose_landmarks.landmark[i].x for i in mp_pose.PoseLandmark])*image_width)
        my=int(min([results.pose_landmarks.landmark[i].y for i in mp_pose.PoseLandmark])*image_height)
        mmx=int(max([results.pose_landmarks.landmark[i].x for i in mp_pose.PoseLandmark])*image_width)
        mmy=int(max([results.pose_landmarks.landmark[i].y for i in mp_pose.PoseLandmark])*image_height)
        image=cv2.rectangle(image,(mx,my),(mmx,mmy),(0,225,255),2)

        # image=cv2.circle(image,(int(nx),int(ny)),5,(255,0,0),5)
        # image=cv2.circle(image,(int(srx),int(sry)),5,(0,255,0),5)
        # image=cv2.circle(image,(int(slx),int(sly)),5,(0,255,0),5)
        # Draw the pose annotation on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        t=np.zeros(image.shape,np.uint8)
        mp_drawing.draw_landmarks(
            t,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,

            None,
            mp_drawing_specs)
        # Flip the image horizontally for a selfie-view display.
        for j in mp_pose.PoseLandmark:
            if results.pose_landmarks.landmark[j]:
                lm_pos[j]=results.pose_landmarks.landmark[j]
        try:
            # cv2.rectangle(t,(getPos(mp_pose.PoseLandmark.LEFT_SHOULDER)),(getPos(mp_pose.PoseLandmark.RIGHT_HIP)),(255,255,255),-1)
            points=np.array([[getPos(mp_pose.PoseLandmark.LEFT_SHOULDER)],[getPos(mp_pose.PoseLandmark.RIGHT_SHOULDER)],
                            [getPos(mp_pose.PoseLandmark.RIGHT_HIP)],[getPos(mp_pose.PoseLandmark.LEFT_HIP)]])
            cv2.fillPoly(t,[points],(255,255,255))
        except Exception as e:
            print(e)
            pass


        temp=((z-1)*temp+t)/z
        # print(z)
        def getDist(name1,name2):
            print(len(np.hypot(np.array(getPos(name1))-np.array(getPos(name2)))))
            return np.hypot(np.array(getPos(name1))-np.array(getPos(name2)))
        # print(np.hypot(xy[0],xy[1]),nx>slx,nx>srx,srx>slx)
        z+=1
        text='front'
        if slx>srx:
            if nx> slx and nx>srx:
                text="right Side"
            elif nx<=slx and nx<=srx:
                text="left Side"


        else:
            text='back'
        print(text)

        logs=logs.append({'Time':time.time(),'Position':text},ignore_index=True)


        cv2.imshow('MediaPipe Pose', cv2.flip(image, 1))
        # cv2.imshow('MediaPipe img', cv2.flip(t, 1))
        cv2.imshow('MediaPipe temp', cv2.flip(np.array(temp,dtype=np.uint8), 1))
        if cv2.waitKey(100) & 0xFF == 27:
            cv2.destroyAllWindows()
            break
    # print(logs)
    logs.dropna(inplace=True)

    logs.reset_index(drop=True,inplace=True)
    import os
    if os.path.exists("Daily_logs.csv"):
        df = pd.read_csv('Daily_logs.csv')
    else:
        df = pd.DataFrame(index=['Date', 'Time of Sleep', 'Quality'])
    import datetime

    t=logs['Time'][len(logs)-1]-logs['Time'][0]
    print(t)

    df=df.append({"Date":datetime.date.today(),"Time of Sleep" :t,'Quality':np.mean(temp.flatten()>0)*3/2*100},ignore_index=True)
    df.to_csv('Daily_logs.csv',index=False)
    logs.to_csv('logs.csv')
    print(np.mean(temp.flatten()>0))

    cv2.imwrite('./temp.png',temp)
    cap.release()
if __name__=='__main__':
    start_tracking()