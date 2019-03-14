from huey import RedisHuey, crontab
import cv2

huey = RedisHuey('timelapseapp')

@huey.periodic_task(crontab(minute='*5'))
def cam_capture():
    video_capture = cv2.VideoCapture(0)
    if not video_capture.isOpened():
        raise Exception("Could not open video device")

    ret, frame = video_capture.read()
    video_capture.release()