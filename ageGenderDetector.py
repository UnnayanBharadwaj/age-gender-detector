from cv2 import cv2
import random

face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def face_extractor(img):    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.1, 5)
    only_face = []

    if faces is ():
        return only_face

    for (x, y, w, h) in faces:
        only_face.append([x, y, x+w, y+h])
    return only_face

def getAge(range):
    return random.randint(range[0], range[-1])

def startDetection():

    #ageProto="age_deploy.prototxt"
    #ageModel="age_net.caffemodel"
    genderProto="gender_deploy.prototxt"
    genderModel="gender_net.caffemodel"
    
    MODEL_MEAN_VALUES=(78.4263377603, 87.7689143744, 114.895847746)
    #ageList=[(0,2), (4,6), (8,12), (15,20), (25,32), (38,43), (48,53), (60,100)]
    genderList=['Male','Female']
    
    #ageNet=cv2.dnn.readNet(ageModel,ageProto)
    genderNet=cv2.dnn.readNet(genderModel,genderProto)
    
    video=cv2.VideoCapture(0)
    padding=20
    while True:
        ret,frame=video.read()
        faceBoxes = face_extractor(frame)

        if not faceBoxes:
            cv2.destroyAllWindows()
            print("No face detected")
        
        for faceBox in faceBoxes:
            x1,y1,x2,y2 = faceBoxes[0]

            face = frame[y1:y2, x1:x2]
            blob=cv2.dnn.blobFromImage(face, 1.0, (227,227), MODEL_MEAN_VALUES, swapRB=False)

            genderNet.setInput(blob)
            genderPreds=genderNet.forward()
            gender=genderList[genderPreds[0].argmax()]
    
            #ageNet.setInput(blob)
            #agePreds=ageNet.forward()
            #age = getAge(ageList[agePreds[0].argmax()])

            cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)
            cv2.putText(frame, f'{gender}', (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,255), 2, cv2.LINE_AA)
            cv2.imshow("Detecting gender", frame)

        if cv2.waitKey(1) == 13:
            break
    video.release()
    cv2.destroyAllWindows()
    
startDetection()