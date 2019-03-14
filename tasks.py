from huey import RedisHuey, crontab
import cv2, time, os

huey = RedisHuey('timelapseapp')
def get_cameras():
    dev = os.listdir('/dev/')
    out_cams = list()
    for device in dev:
        if "video" in device:
            print(device[:-1])

get_cameras()

@huey.periodic_task(crontab(minute='*'))
def cam_capture():
    video_capture = cv2.VideoCapture(0)
    if not video_capture.isOpened():
        raise Exception("Could not open video device")

    ret, frame = video_capture.read()
    video_capture.release()
    cv2.imwrite("captures/{}.jpg".format(time.time()), frame)