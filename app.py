from flask import Flask , render_template , request
from werkzeug.utils import secure_filename
import os 
import fecthing_details
import plate_model
import cv2
from flask.helpers import flash
import easyocr


app = Flask("Car Details")

path = os.getcwd()
dir = os.path.join(path, "uploads")
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = dir


@app.route("/")
def home():
        return render_template( "index.html" )


@app.route("/car-details" , methods = ["POST"] )
def prediction():
        f=request.files["upload"]#it will fetch that image and store it in f
        f.save(f.filename)
        
        
        # img = cv2.imread(filename)
        # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))



        # bfilter = cv2.bilateralFilter(gray, 11, 17, 17) #Noise reduction
        # edged = cv2.Canny(bfilter, 30, 200) #Edge detection
        # plt.imshow(cv2.cvtColor(edged, cv2.COLOR_BGR2RGB))


        # keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # contours = imutils.grab_contours(keypoints)
        # contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]


        # location = None
        # for contour in contours:
        #         approx = cv2.approxPolyDP(contour, 10, True)
        #         if len(approx) == 4:
        #                 location = approx
        #                 break

        # mask = np.zeros(gray.shape, np.uint8)
        # new_image = cv2.drawContours(mask, [location], 0,255, -1)
        # new_image = cv2.bitwise_and(img, img, mask=mask)


        # plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))


        # (x,y) = np.where(mask==255)
        # (x1, y1) = (np.min(x), np.min(y))
        # (x2, y2) = (np.max(x), np.max(y))
        # cropped_image = gray[x1:x2+1, y1:y2+1]

        # plt.imshow(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))


        # import easyocr

        # reader = easyocr.Reader(['en'])
        # result = reader.readtext(cropped_image)
        # # result

        # plate_number = result[0][-2]
        # plate_number = plate_number.replace( ' ', '')
        # plate_number = plate_number.replace('.','')

       
        
        



        plate_number = plate_model.plate_no(f.filename)

        
        # plate_numbers="MH13BN8454"
        vehicle_info =  fecthing_details.rto(plate_number)
        return render_template("index.html", output = vehicle_info)

        
        # return render_template("index.html", output = plate_number)
        # return render_template('output.html' , image=image)
        # return render_template('output.html' , image_path=image_path)

        

app.run(host="localhost" , port=8080, debug=True)

