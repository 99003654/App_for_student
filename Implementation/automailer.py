import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from pretty_html_table import build_table
from email import encoders
from NEW_RADAR import *

pre_survey=pd.read_excel("pre_survey.xlsx")
post_survey = pd.read_excel("post_survey.xlsx")
pre_test = pd.read_excel("pre_test.xlsx")
post_test = pd.read_excel("post_test.xlsx")

pre_test_list1 = []
pre_test_list2 = []
pos_test_list1 = []
pos_test_list2 = []
pre_survey_list1 = []
pre_survey_list2 = []
pos_survey_list1 = []
pos_survey_list2 = []

for i in range(0, 10):
     sum1 = 0
     sum2 = 0
     sum3 = 0
     sum4 = 0

     pre_survey_list1 = pre_test.iloc[i, 4:10]
     sum1 = sum(pre_survey_list1)
     pre_survey_list2.append(sum1)

     pos_test_list1 = post_test.iloc[i, 4:10]
     sum2 = sum(pos_test_list1)
     pos_test_list2.append(sum2)

     pre_test_list1 = pre_test.iloc[i, 4:10]
     sum3 = sum(pre_test_list1)
     pre_test_list2.append(sum3)

     pos_survey_list1 = post_survey.iloc[i, 4:10]
     sum4 = sum(pos_survey_list1)
     pos_survey_list2.append(sum4)

 arr = np.array(pre_survey_list2)
 pre_survey["pre_survey_total"] = arr

 arr = np.array(pre_test_list2)
 pre_test["pre_test_total"] = arr

 arr = np.array(pos_survey_list2)
 post_survey["post_survey_total"] = arr

 arr = np.array(pos_test_list2)
 post_test["post_test_total"] = arr

def maximum():
    max_pre_survey = pre_survey.nlargest(5, ["pre_survey_total"])
    max_pre_test=pre_test.nlargest(5, ["pre_test_total"]) 
    max_post_survey = post_survey.nlargest(5, ["post_survey_total"])
    max_post_test = post_test.nlargest(5, ["post_test_total"])

    frames = [max_pre_survey, max_pre_test, max_post_survey, max_post_test ]
    
    return (pd.concat(frames))



def minimum():
    min_pre_survey = pre_survey.nsmallest(3, ["pre_survey_total"])
    min_post_survey = post_survey.nsmallest(3, ["post_survey_total"])
    min_pre_test = pre_test.nsmallest(3, ["pre_test_total"])
    min_post_test = post_test.nsmallest(3, ["post_test_total"]) 

    frames = [min_pre_survey, min_pre_test, min_post_survey, min_post_test]
    
    return (pd.concat(frames))


def send_mail(body1, body2):
    faculty_radar_graph()
    
    image1 = 'Consolidated_class.png'

    message = MIMEMultipart()
    message['Subject'] = 'Top 5 Students of class'
    message['From'] = 'learningcorporate7@gmail.com'
    message['To'] = 'pareekashish2196@gmail.com'
    
    body_text = "Top 5 students of your module"
    body_content = body1
    message.attach(MIMEText(body_text))
    message.attach(MIMEText(body_content, "html"))
    
    body_text = "Bottom 3 students of your module"
    body_content = body2
    message.attach(MIMEText(body_text))
    message.attach(MIMEText(body_content, "html"))
    

    with open(image1, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= %s" % image1)
    message.attach(part)

    message.attach(MIMEText(image1))
    msg_body = message.as_string()

    server = SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(message['From'], '99003708')
    server.sendmail(message['From'], message['To'], msg_body)
    server.quit()



def send_data_to_teacher():
    top_data = maximum()
    bottom_data= minimum()
    output1 = build_table(top_data, 'blue_light')
    output2 = build_table( bottom_data, 'blue_light')
    send_mail(output1,output2)

    return "Mail sent successfully."

def send_mail_student():
        '''To send mails'''
        list1 = ['ashish.pareek@ltts.com', 'lalit.bhardwaj@ltts.com', 'ashish.nayak@ltts.com', 'prashantsudhir.bagal@ltts.com', 'aakarsh.mehta@ltts.com', 'yash.jhajharia@ltts.com', 'manzar.hussain@ltts.com', 'digendrakumar.sahu@ltts.com', 'ankitkumar.yadav@ltts.com', 'manu.nadar@ltts.com']
        psnumber = get_PS()
        for i in range(0, 10):
            student_radar_graph(psnumber[i])
            image1 = f'Consolidated_{psnumber[i]}.png'
            sender_email = 'learningcorporate7@gmail.com'
            sender_ePass = '99003708'
            receiver_email = list1[i]
            print(receiver_email)
            message = MIMEMultipart()
            message['From'] = sender_email
            message['To'] = receiver_email
            message['Subject'] = f'Your Test Score :- {psnumber[i]}'
            mail_text = f'''Hello {psnumber[i]},\n\nThis is to inform you about your test result. Attachments file is above.\n\nThank You\n\nThis is an Auto Generated Mail, Please do not reply to this.'''
            message.attach(MIMEText(mail_text, 'plain'))
            with open(image1, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())

            encoders.encode_base64(part)
            part.add_header('Content-Disposition',
                            "attachment; filename= %s" % image1)
            message.attach(part)
            servers = SMTP('smtp.gmail.com', 587)
            servers.starttls()
            servers.login(sender_email, sender_ePass)
            text = message.as_string()
            servers.sendmail(sender_email, receiver_email, text)
            servers.quit()
            print('Mail Sent')
