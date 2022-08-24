from tkinter import *
from tkinter import ttk
from PIL import Image
import PIL.Image
from PIL import ImageTk
from cv2 import cv2
import numpy as np
import face_recognition
import os
from tkinter import messagebox

root = Tk()
root.geometry("1900x1000+0+0")
root.title("detecting face.....")
root.iconbitmap("")


'''# bg image
img = PIL.Image.open(r"D:/college/BCA/Mislaneous/R&D/projects/RUNING/Faculty recoginition/images.jpeg")
img=img.resize((1900,1000),Image.Resampling.LANCZOS)

photoimg=ImageTk.PhotoImage(img)

bg_lbl=Label(root,image=photoimg)
bg_lbl.place(x=0,y=0,width=1900,height=1000)'''

"""#black button to start cam
img_2 = Image.open(r"D:/college/BCA/Mislaneous/R&D/projects/RUNING/Faculty recoginition/images.jpeg")
img_2 = img_2.resize((1900, 1000), Image.Resampling.LANCZOS)

photoimg_2 = ImageTk.PhotoImage(img_2)"""


def open_image(name):
    img = cv2.imread("D:/college/BCA/Mislaneous/R&D/projects/RUNING/Faculty recoginition/Images of Faculties/")
    cv2.imshow("Faculty Details", img)
    cv2.waitKey(0)
    print(name + " THIS Entered IMAGES")

# To open camera
def open_cam():
    path = 'Images of Faculties'
    images = []
    personNames = []
    myList = os.listdir(path)
    word_list = []
    find_max = ""

    with open('Attendance.csv', 'r') as firstfile, open('AttendanceHistory.csv', 'a') as secondfile:
        for line in firstfile:
            secondfile.write(line)
    firstfile = open('Attendance.csv', 'r+')
    firstfile.close()
    firstfile.truncate(0)

    # print(myList)
    for cu_img in myList:
        current_Img = cv2.imread(f'{path}/{cu_img}')
        images.append(current_Img)
        personNames.append(os.path.splitext(cu_img)[0])

    # print(personNames)

    def faceEncodings(images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList

    encodeListKnown = faceEncodings(images)
    print('All Encodings Complete!!!')
    messagebox.showinfo("Ready")


    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        faces = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
        faces = cv2.cvtColor(faces, cv2.COLOR_BGR2RGB)

        facesCurrentFrame = face_recognition.face_locations(faces)
        encodesCurrentFrame = face_recognition.face_encodings(faces, facesCurrentFrame)

        for encodeFace, faceLoc in zip(encodesCurrentFrame, facesCurrentFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            # print(faceDis)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = personNames[matchIndex].upper()
                print(name)
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)  # hided to hide greenbox and frames
                cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

                if len(word_list) < 20:
                    word_list.append(name)
                    print(word_list)

        if len(word_list) == 20:  # if cv2.waitKey(1) == 13:
            break

    cap.release()
    cv2.destroyAllWindows()
    if len(word_list) == 20:
        print("list completed ................."
              "List completed..................."
              "List completed..................")

        word_dictionary = {}

        for word in word_list:
            if word not in word_dictionary:
                word_dictionary[word] = 1
            else:
                word_dictionary[word] = word_dictionary[word] + 1
                print(word_dictionary)

                find_max = max(word_dictionary, key=word_dictionary.get)
                print("maximum value : ", find_max)
                break
        open_image(find_max)

'''bg_button = Button(root,image=photoimg_2,cursor="hand2",command = open_cam)
bg_button.place(x=0,y=0,width=1900,height=1000)


root.mainloop()'''

