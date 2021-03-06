import cv2

cap = cv2.VideoCapture('input/base.mp4')

# Get the frames per second
fps = cap.get(cv2.CAP_PROP_FPS)

# Get the total numer of frames in the video.
frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)

# Calculate the duration of the video in seconds
duration = frame_count / fps
second = 0
cap.set(cv2.CAP_PROP_POS_MSEC, second * 1000) # optional
success, image = cap.read()

while success and second <= duration:
    # do stuff
    second += 1
    cap.set(cv2.CAP_PROP_POS_MSEC, second * 1000)
    success, image = cap.read()
