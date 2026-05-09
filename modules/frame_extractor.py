import cv2
import os

def extract_frames(video_path, output_folder, interval=30):

    cap = cv2.VideoCapture(video_path)

    count = 0
    saved = 0

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        if count % interval == 0:

            frame_path = os.path.join(
                output_folder,
                f"frame_{saved}.jpg"
            )

            cv2.imwrite(frame_path, frame)

            saved += 1

        count += 1

    cap.release()
