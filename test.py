from MedicalInformation import get_medical_informations
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import smtplib

# 邮件信息
password = "tpymueebnzojchcf"
from_email = ("jaydentang418@qq.com")
to_email = "jaydentang418@qq.com"

def send_email():
    server = smtplib.SMTP("smtp.qq.com:587")
    server.starttls()
    server.login(from_email, password)

    message = MIMEMultipart()
    message["From"] = from_email
    message["To"] = to_email

    # 邮件主题
    message["Subject"] = "警告！"

    # 查找医疗信息
    medical_informations = get_medical_informations()
    medical_information = None
    for info in medical_informations:
        if info.name == "Jayden":
            medical_information = info
            break

    # 消息内容
    message_body = (
        f"jayden跌倒了!\n"
        + "医疗信息卡:\n"
        + "\t姓名: " + medical_information.name + "\n"
        + "\t出生日期: " + medical_information.brithday + "\n"
        + "\t血型: " + medical_information.blood_type + "\n"
        + "\t紧急联系人: " + medical_information.phone_number + "\n"
        + "\t健康状况: " + medical_information.health_conditions + "\n"
        + "\t过敏信息: " + medical_information.allergy_information + "\n"
        + "\t当前用药: " + medical_information.current_medications + "\n"
        + "\t手术史或重大医疗事件: " + medical_information.history_surgeries_N_medical_events + "\n"
        + "时间: 2024-04-22 22:54:08"
        )

    message.attach(MIMEText(message_body, "plain"))
    server.sendmail(from_email, to_email, message.as_string())

    server.quit()

send_email()