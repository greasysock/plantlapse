import cv2, time, os

output_path = "/home/pi/captures/cam{}"

def get_cameras():
    dev = os.listdir('/dev/')
    out_cams = list()
    for device in dev:
        if "video" in device:
            index = int(device[-1])
            c = (index, cv2.VideoCapture(index))
            out_cams.append(c)
    return out_cams
def check_path(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
def cam_capture():
    cameras = get_cameras()
    for index, camera in cameras:  
        if camera.isOpened():
            camera.set(5,float(1))
            p = output_path.format(index)
            check_path(p)
            ret, frame = camera.read()
            cv2.imwrite("{}/{}.jpg".format(int(p,time.time()), frame)
            camera.release()
            print("Image captured on camera {}".format(index))


if __name__ == "__main__":
    cam_capture()
