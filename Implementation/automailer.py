

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
