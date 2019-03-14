from huey import RedisHuey, crontab
import cv2, time

huey = RedisHuey('timelapseapp')

@huey.periodic_task(crontab(minute='*'))
def cam_capture():
    video_capture = cv2.VideoCapture(0)
    if not video_capture.isOpened():
        raise Exception("Could not open video device")

    ret, frame = video_capture.read()
    video_capture.release()
    cv2.imwrite("captures/{}.jpg".format(time.time()), frame)