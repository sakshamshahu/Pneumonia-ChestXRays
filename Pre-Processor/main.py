import cv2
import pickle
import os
size = 300
def preprocessing(img):
    img_array = cv2.imread( img,cv2.IMREAD_GRAYSCALE) #convert image to grayscale
    
    new_array = cv2.resize(img_array, (size, size))  #resize image

    # returns the image 
    return new_array/256
folders = ['test','train']
type = ['NORMAL','PNEUMONIA']

X = []
Y = []
for f in folders:
    p1 = os.path.join(f,type[0])
    for i in os.listdir(p1):
        p = os.path.join(p1,i)
        Y.append(0)
        X.append(preprocessing(p))

    p2 = os.path.join(f,type[1])
    for i in os.listdir(p2):
        p = os.path.join(p2,i)
        Y.append(1)
        X.append(preprocessing(p))    

print("done")
print(len(X))
print(len(Y))
f1 = open('X.pickle', 'wb')
pickle.dump(X, f1)
f1.close()

f2 = open('Y.pickle', 'wb')
pickle.dump(Y, f2)
f2.close()
# print(preprocessing('test/NORMAL/IM-0001-0001.jpeg'))