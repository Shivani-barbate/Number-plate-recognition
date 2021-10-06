import cv2
from matplotlib import pyplot as plt
import numpy as np
import imutils
import os 
os.environ['KMP_DUPLICATE_LIB_OK']='True'
def plate_no(image):
    img = cv2.imread(image , cv2.IMREAD_COLOR)
    # img = imutils.resize(img, width=500)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))



    bfilter = cv2.bilateralFilter(gray, 11, 17, 17) #smoothening images and reducing noise
    edged = cv2.Canny(bfilter, 30, 200) #Edge detection
    # plt.imshow(cv2.cvtColor(edged, cv2.COLOR_BGR2RGB))


    keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #contour:useful tool for shape analysis & object detection
    contours = imutils.grab_contours(keypoints)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]


    location = None
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 10, True)
        if len(approx) == 4:
            location = approx
            break
#mask: allow us to focus only on the portion of the image 
    mask = np.zeros(gray.shape, np.uint8)
    new_image = cv2.drawContours(mask, [location], 0,255, -1)
    new_image = cv2.bitwise_and(img, img, mask=mask)


    # plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))


    (x,y) = np.where(mask==255)
    (x1, y1) = (np.min(x), np.min(y))
    (x2, y2) = (np.max(x), np.max(y))
    cropped_image = gray[x1:x2+1, y1:y2+1]

    # plt.imshow(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))



    import easyocr
#EasyOCR is a python package that allows the image to be converted to text
    reader = easyocr.Reader(['en'])
    result = reader.readtext(cropped_image)
    # result

    plate_number = result[0][-2]
    plate_number = plate_number.replace( ' ', '')
    plate_number = plate_number.replace('.','')

    return plate_number

# plate_no('car2.jpeg')