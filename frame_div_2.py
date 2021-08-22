import cv2
import time
import os

def video_to_frames(input_loc, output_loc):
    try:
        os.mkdir(output_loc)
    except OSError:
        pass

    time_start = time.time()
    cap = cv2.VideoCapture(input_loc)

    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    print ("Number of frames: ", video_length)

    frame = 298300
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame - 1)

    count = 0
    print ("Converting video..\n")
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            continue
        cv2.imwrite(output_loc + "/%#05d.jpg" % (count+1), frame)
        count = count + 1
        if (count > (video_length-1)):
            time_end = time.time()
            cap.release()
            print ("Done extracting frames.\n%d frames extracted" % count)
            print ("It took %d seconds forconversion." % (time_end-time_start))
            break
if __name__=="__main__":
    input_loc = 'input/base.mp4'
    output_loc = 'output/'
    video_to_frames(input_loc, output_loc)
