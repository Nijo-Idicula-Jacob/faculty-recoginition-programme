##import os 
##path = 'D:\college\BCA\Mislaneous\R&D\projects\RUNING\Faculty recoginition\Images of Faculties'
##images = []
##personNames = []
##myList = os.listdir(path)
##word_list = []
##print (word_list)
##find_max = ""
##
##with open('Attendance.csv', 'r') as firstfile, open('AttendanceHistory.csv', 'a') as secondfile:
##    for line in firstfile:
##        secondfile.write(line)
##firstfile = open('Attendance.csv', 'r+')
##firstfile.close()
##firstfile.truncate(0)

##def open_image(name):
##    img = cv2.imread("D:/college/BCA/Mislaneous/R&D/projects/RUNING/Faculty recoginition/Images of Faculties/")
##    cv2.imshow("Faculty Details", img)
##    cv2.waitKey(0)
##    print(name + " THIS Entered IMAGES")

with open('Attendance.csv', 'r') as firstfile, open('AttendanceHistory.csv', 'a') as secondfile:
        for line in firstfile:
            print(firstfile)
            print(secondfile )
            print(line)
