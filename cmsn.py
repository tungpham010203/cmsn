from time import sleep
import cv2
import shutil
import requests
from PIL import Image
import time
a = 177
b = 219
my_url = 'https://i.imgur.com/Ppm1O0w.jpg'
response = requests.get(my_url, stream=True)
with open('my_image.ipg', 'wb') as file:
    shutil.copyfileobj(response.raw, file)
del response
so_do= cv2.imread("my_image.ipg")
img_resized = cv2.resize(src=so_do, dsize=(720,460))
#img = Image.open('my_image.ipg')

#P = input('myfile.txt')

def loadchay():
    print( "\n\t\t\t\t\t\tLoading...\n\n")
    print("\t\t\t\t\t")

    for i in range(26):
        print( a)

    print("\r")
    print("\t\t\t\t\t")

    for i in range(26):

        print( b)


    print( "\nDa load xong!!!")

print("Nhan phim Enter de bat dau...")

cv2.imshow('anh',img_resized)

f = open('myfile.txt', "r")
for i in range(17):
    with open('myfile.txt', 'r') as f:
        datalist = f.readlines() 
        line2 = datalist[i]
        print(line2)
        time.sleep(0.1)
#for i in range(50):
#    print(f.readline(i))
#    time.sleep(1)

input()
ky=cv2.waitKey()
if ky==27:
    cv2.destroyAllWindows()
    

