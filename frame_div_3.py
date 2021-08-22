import cv2
import time
import os

def video_to_frames(input_loc, output_loc, frame_div):
    try:
        os.mkdir(output_loc)
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
            cv2.imwrite(output_loc + "/%#05d.jpg" % (count+1), frame)
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
    input_loc = 'input/여러분들의 침대 밑에는 무엇이 있습니까_ (공포게임).mp4'
    output_loc = 'output/'
    frame_div = 1000 # 줄이고 싶은 비율
    video_to_frames(input_loc, output_loc, frame_div)
