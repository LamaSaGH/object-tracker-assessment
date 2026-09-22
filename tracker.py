import cv2


# open webcam
camera = cv2.VideoCapture(0)

# get the first frame
ret, first_frame = camera.read()


# select the object
box = cv2.selectROI(
    "Select Object",
    first_frame,
    fromCenter=False
)

cv2.destroyWindow("Select Object")


# create CSRT tracker
tracker = cv2.TrackerCSRT_create()

# tell the tracker what object to track
tracker.init(first_frame, box)


# start tracking
while True:

    ret, frame = camera.read()

    # find the object in the new frame
    _, box = tracker.update(frame)

    # get bounding box coordinates
    x, y, w, h = map(int, box)

    # draw the box
    cv2.rectangle(
        frame,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        2
    )

    # show webcam
    cv2.imshow("Object Tracking", frame)

    # press q to stop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


