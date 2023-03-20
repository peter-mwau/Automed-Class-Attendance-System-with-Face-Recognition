import cv2
from django.db import connection
import numpy as np
import face_recognition_models
import os
import face_recognition
from datetime import datetime
import sqlite3
import pathlib
from staff.models import Lecturer_detail


def method_1(dp_path: str) -> sqlite3.Connection:
    connection = sqlite3.Connection(dp_path)
    return connection

if __name__ == "_main_":
    local_dp_path = './project.sqlite3'

    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM attendance_stud_attendance""")
    result = cursor.fetchall()

path = 'images/images'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for lis in myList:
    curImg = cv2.imread(f'{path}/{lis}')
    images.append(curImg)
    classNames.append(os.path.splitext(lis)[0])
print(classNames)

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def markAttendance(name):
        with open('attendance.csv','r+') as f:
            myDataList = f.readlines()
            nameList = []
            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])
            else:
                lec_details = Lecturer_detail.objects.all().values()
                now = datetime.now()
                dtstring = now.strftime("%Y-%m-%d %H:%M:%S")
                for item in lec_details:
                    dict = [
                        {'Full_Name': item['fname']+item['lname']},
                        {'Lecturer_ID': item['lecturer_id']},
                        { 'Department': item['department']},
                        {'Unit': item['units_teaching']},
                        {'Faculty': item['faculty']},
                        {'Date': dtstring}
                    ]
                    f.writelines((f'\n{dict}'))

                #     if user_exist==0: #  user not found, add user
                # try:
                #     lec_details = Lecturer_detail.getLecturer(name_[0], name_[1])
                #     stud_detail = Student_detail.getStudent(name_[0],name_[1])
                #     # items = lec_details 
                #     now = datetime.now()
                #     dtstring = now.strftime("%Y-%m-%d %H:%M:%S")
                #     # dtstring = now.strftime("%Y-%m-%d")

                    
                #     dict = [
                #         {'Full_Name': lec_details.fname+' '+lec_details.lname,
                #         'Category': lec_details.category,
                #         'Date': dtstring,
                #         'Department': lec_details.department,
                #         'Faculty': lec_details.faculty,
                #         'Unit': lec_details.units_teaching,
                #         'Lecturer_ID': lec_details.lecturer_id
                #         }]
                #     with open(csv_name, 'a') as csvfile:
                #         writer = csv.DictWriter(csvfile, fieldnames= csv_columns)
                #         for data in dict:
                #             writer.writerow(data)
                #             read_csv(csv_name)
                #             #reset user_exist to 0
                #             user_exist = 0
                #             f.truncate(0)
                #             # clear
                #     dict1 = [
                #         {'Full_Name': stud_detail.fname+' '+stud_detail.lname,
                #         'Reg_no': stud_detail.reg_no,
                #         'Course': stud_detail.course,
                #         'Cohort': stud_detail.cohort,
                #         'Category': stud_detail.category,
                #         'Unit': stud_detail.units,
                #         # 'Faculty': stud_detail.faculty,
                #         'Date': dtstring
                #         }]
                #     # category = lec_details.category or stud_detail.category
                #     with open(csv_name2, 'a') as csvfile:
                #         writer = csv.DictWriter(csvfile, fieldnames=csv_columns2)
                #         # for data in dict1:
                #         print(dict1)
                #         for data in dict1:
                #             writer.writerow(data)  
                #             read_csv2(csv_name2)
                #             #reset user_exist to 0
                #             user_exist = 0
                #             # clear csv file
                #             f.truncate(0)
                            



encodeListKnown = findEncodings(images)
print("Encoding Complete")

capture = cv2.VideoCapture(0)
cv2.waitKey(0)

while True:
    success, img = capture.read()
    # cv2.imshow("Video", img)
    imgS = cv2.resize(img,(0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)

    for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDistance = face_recognition.face_distance(encodeListKnown,encodeFace)
        print(faceDistance)
        matchIndex = np.argmin(faceDistance)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            print(name)
            y1,x2,y2,x1 = faceLoc
            y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),2)
            markAttendance(name)
        else:
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, "UNKNOWN", (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)

    cv2.imshow('Webcam', img)
    cv2.waitKey(1)