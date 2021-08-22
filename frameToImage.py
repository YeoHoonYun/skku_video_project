import cv2
import time
import os
import glob

def video_to_frames(input_loc, output_loc, frame_div):
    try:
        os.mkdir(output_loc+str(i))
    except OSError:
        pass
    time_start = time.time()
    cap = cv2.VideoCapture(input_loc)
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    print ("Number of frames: ", video_length)

    count = 0
    print ("Converting video..\n")
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            continue
        if (int(cap.get(1)) % frame_div == 0):
            print(output_loc+str(i)+"/%#08d.jpg" % (count+1))
            cv2.imwrite(output_loc+str(i)+"/%#08d.jpg" % (count+1), frame)
        count = count + 1

        if (count > (video_length-1)):
            # Log the time again
            time_end = time.time()
            # Release the feed
            cap.release()
            # Print stats
            print ("Done extracting frames.\n%d frames extracted" % count)
            print ("It took %d seconds forconversion." % (time_end-time_start))
            break

if __name__=="__main__":
    print(glob.glob("input/*"))
    output_loc = 'output/'
    frame_div = 10000  # 줄이고 싶은 비율

    for i, input_nm in enumerate(glob.glob("input/*")):
        print(input_nm)
        video_to_frames(input_nm, output_loc, frame_div)
