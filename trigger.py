import requests
from gpiozero import MotionSensor
from picamera import PiCamera
from signal import pause
from filestack import Client

client = Client("ASN9AAfoKTjiAM7hq2I3sz")

camera = PiCamera()
camera.resolution = (1920, 1080)

def send_alert():
    camera.capture("image.jpg")
    new_filelink = client.upload(filepath="image.jpg")
    print(new_filelink.url)
    
    r = requests.post("https://maker.ifttt.com/trigger/trigerr/with/key/dlo9iGzO330FnMV6SxDfoJxwaXqcMINRDZyYcQNpFUX", json={"value1": "https://cdn.filestackcontent.com/theimageurl"})

    if r.status_code == 200:
        print("Aha! Thief Detected")
    else:
        print("Error")

pir = MotionSensor(17)
pir.when_motion = send_alert
pause()
