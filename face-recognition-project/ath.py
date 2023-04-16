import cv2
import face_recognition
import numpy as np
import os
import cvzone
import sys
import check
import cross


def main():

    path = 'pics'
    images = []
    bg = cv2.imread('images/bg4.png')
    my_list = os.listdir(path)
    pos = 0
    for cls in my_list:
        curImg = cv2.imread(f'{path}/{cls}')
        images.append(curImg)

    def find_encodings(images):
        if len(images) == 0:
            raise ValueError("No images provided")
        
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList

    encodeListKnown = find_encodings(images)
    cap = cv2.VideoCapture(0)
    cap.set(3, 320)
    cap.set(4, 240)

    authentified = 0
    while True:
        sucess, img = cap.read()
        bg[142:142+240, 40:40+320] = img
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(
                encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(
                encodeListKnown, encodeFace)
            matchIndex = np.argmin(faceDis)
            pos += 40
            color = (0, 205, 0)
            cv2.line(bg, (pos, 490), (pos+40, 490), color, 5)
            org = (200, 480)
            cv2.putText(bg, 'LOADING', (135, 440),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

            if faceDis[matchIndex] < 0.50:
                authentified += 1
                top, right, bottom, left = faceLoc
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4
                bbox = 40 + left, 142 + top, right - left, bottom - top
                cvzone.cornerRect(bg, bbox,  rt=0)

            else:
                top, right, bottom, left = faceLoc
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4
                bbox = 40 + left, 142 + top, right - left, bottom - top
                cvzone.cornerRect(bg, bbox,  rt=0)

        cv2.imshow('Webcam', bg)
        cv2.waitKey(1)

        if pos > int(bg.shape[1]) - 50:
            if authentified >= 4:
                cap.release()
                cv2.destroyAllWindows()
                check.main()

            else:
                cap.release()
                cv2.destroyAllWindows()
                cross.main()
            sys.exit()


if __name__ == "__main__":
    main()
