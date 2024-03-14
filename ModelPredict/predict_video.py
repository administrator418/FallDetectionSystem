import cv2
import sys
from ultralytics import YOLO
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

password = "tpymueebnzojchcf"
from_email = "jaydentang895@qq.com"
to_email = "jaydentang895@qq.com"

server = smtplib.SMTP("smtp.qq.com:587")
server.starttls()
server.login(from_email, password)


def send_email(to_email, from_email, wariningtype):
    message = MIMEMultipart()
    message["From"] = from_email
    message["To"] = to_email
    message["Subject"] = "警告！"

    if wariningtype == "send_email":
        message_body = "老人摔倒了！"
    elif wariningtype == "test":
        message_body = "测试！" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    else:
        sys.exit("Error: Invalid warning type!")

    message.attach(MIMEText(message_body, "plain"))
    server.sendmail(from_email, to_email, message.as_string())


# Load the YOLOv8 model
model = YOLO("./ModelPredict/yolov8n_fall.pt")

# Open the video file
video_path = "./ModelPredict/TestData/videos/fall(1).mp4"
cap = cv2.VideoCapture(video_path)

flag = {
    "send_email": False,
    "fall_time": -1,
    "test": False,
}

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 inference on the frame
        results = model(frame)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()
        clss = results[0].boxes.cls.cpu().tolist()

        if 1 in clss:  # Only send email If not sent before
            if not flag["send_email"]:
                if flag["fall_time"] == -1:
                    flag["fall_time"] = time.time()
                elif time.time() - flag["fall_time"] > 10:
                    send_email(to_email, from_email, "send_email")
                    flag["send_email"] = True
        else:
            flag["send_email"] = False
            flag["fall_time"] = -1

        # Display the annotated frame
        cv2.imshow("Fall Detection", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()
