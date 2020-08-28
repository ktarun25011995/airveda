Steps to run the project
# airveda

Don't delete the databasee sqlite3 as i have created the dummy data inside it will be lost.
 
1. Clone the repository to your local machine
2. create a virtualenv with python>3.6 version 
3. cd into the project 'airveda' and run `pip install -r requirements.txt`
4. Now all the dependencies are installed now run the server `python manage.py runserver`

for authentication token i will mail it you please check the email.

## API for devices 
1. List of all devices 
   Endpoint: GET http://localhost:8000/api/devices/
   get all the devices 
   
2. Create a device
   Endpoint: POST http://localhost:8000/api/devices/
   creates a device return json response 
   
3. Retrieve a device 
   Endpoint: GET http://localhost:8000/api/devices/{device_id}/
   get a single device as correspond to device id
   
4. Delete a device 
   Endpoint: DELETE http://localhost:8000/api/devices/{device_id}/
 
5. Get Humidity or Tempreature Reading on bases of start_on and end_on timestamp the string format is "%Y-%m-%d %H:%M:%S" ie. 2020-08-28 09:22:38 and also on paramerer ie. temperature and humidity
   Endpoint: http://localhost:8000/api/devices/{device_id}/readings/{parameter}/?start_on=2020-08-28 09:22:38&end_on=2020-08-28 09:24:38


If any queries please revert accordingly
