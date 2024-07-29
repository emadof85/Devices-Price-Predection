## Test the Application
Run the Flask Application:

Ensure the Flask application is running and accessible at http://localhost:5000.
Run the Spring Boot Application:

Start your Spring Boot application by running the main class annotated with @SpringBootApplication.
Test the Endpoints:

Use tools like Postman or curl to test the Spring Boot API endpoints:
POST /api/devices to create a new device.
GET /api/devices/{id} to retrieve a device by ID.
POST /api/devices/predict/{deviceId} to predict the price for a device.

### API Parameters Example:

```json  
{
    "batteryPower": 1500,
    "blue": 1,
    "clockSpeed": 2.0,
    "dualSim": 1,
    "fc": 5,
    "fourG": 1,
    "intMemory": 16,
    "mDep": 0.5,
    "mobileWt": 150,
    "nCores": 4,
    "pc": 13,
    "pxHeight": 720,
    "pxWidth": 1280,
    "ram": 2048,
    "scH": 14,
    "scW": 7,
    "talkTime": 12,
    "threeG": 1,
    "touchScreen": 1,
    "wifi": 1
}
```
### Predict the Price for the Device:

URL: http://localhost:8080/api/devices/predict/{deviceId}
Method: POST
Replace {deviceId} with for example the ID of the device created in the previous step.
