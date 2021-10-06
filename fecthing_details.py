# fecthing car details .................
import json
import requests
import xmltodict


def rto(number_plate):
    try:
        vehicle_reg_no = number_plate #NumberPlate deteted
        username = "shivani03" #API_user name
        url = "http://www.regcheck.org.uk/api/reg.asmx/CheckIndia?RegistrationNumber=" + vehicle_reg_no + "&username="+username
        url=url.replace(" ","%20")
        r = requests.get(url)
        #print(r.content)                                 
        n = xmltodict.parse(r.content)#xmltodict. parse() method takes an XML file as input and changes it to Ordered Dictionary. 
        #print(n)
        k = json.dumps(n)
        #print(k)
        df = json.loads(k)
        #print(df)
        l=df["Vehicle"]["vehicleJson"]
        #print(l)
        p=json.loads(l)
        s="\nVehicle Registration Number : "+vehicle_reg_no+"\nOwner name : "+str(p['Owner'])+"\n"+"Car Company : "+str(p['CarMake']['CurrentTextValue'])+"\n"+"Car Model : "+str(p['CarModel']['CurrentTextValue'])+"\n"+"Fuel Type : "+str(p['FuelType']['CurrentTextValue'])+"\n"+"Registration Year : "+str(p['RegistrationYear'])+"\n"+"Insurance : "+str(p['Insurance'])+"\n"+"Vehicle ID : "+str(p['VechileIdentificationNumber'])+"\n"+"Engine No. : "+str(p['EngineNumber'])+"\n"+"Location RTO : "+str(p['Location'])
        return(s)
    except:
        msg="Unable to retrieve vehicle information, plz \nprovide clear image"
        return(msg)





      