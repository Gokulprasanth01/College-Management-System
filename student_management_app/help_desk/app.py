from distutils.log import debug
from flask import Flask, render_template, request, url_for, redirect
# from email.mime.text import MIMEText
from email.message import EmailMessage

import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

app = Flask(__name__)

# A decorator used to tell the application
# which URL is associated function
@app.route('/')	
def hello():
	return render_template("home.html")

#app.config["IMAGE_UPLOADS"] = "C:\\Users\\suraj\\Desktop\\flask\\help_desk"

@app.route("/query/", methods=['POST','GET'])
def query():
    print("done 1")
    if request.method == "POST":
        u =""
        print("done 2")
        name = request.form['name']
        contact = request.form['contact']
        address = request.form['address']
        category = request.form['category']
        topic = request.form['topic']
        message = request.form['message']
        image = request.form['image']
        

        print(name, contact, address, category, topic, message, image)

        yourEmail = "surajkumargupta@geeksforgeeks.org"
        yourPassword = u   
        
        msg = MIMEMultipart()

        # storing the senders email address
        msg['From'] = yourEmail
        msg['To'] = yourEmail
        msg['Subject'] = category

        # string to store the body of the mail
        body = "First Name : "+str(name)+"\nContact Number : "+str(contact)+"\nAddress : "+str(address)+ "\nCategory : " + str(category) +"," + str(topic) + "\nMessage : "+str(message)

        # attach the body with the msg instance
        msg.attach(MIMEText(body, 'plain'))

        # open the file to be sent
        filename = image
        attachment = open(filename, "r+")
        #attachment.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
        

        # instance of MIMEBase and named as p
        p = MIMEBase('application', 'octet-stream')

        # To change the payload into encoded form
        p.set_payload((attachment).read())


        # encode into base64
        encoders.encode_base64(p)

        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        # attach the instance 'p' to instance 'msg'
        msg.attach(p)

        # creates SMTP session
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(yourEmail,u)

        # Converts the Multipart msg into a string
        text = msg.as_string()

        # server.send_message(msg)

        # server.quit()




        # Send the message via our own SMTP server.
        try:
            # sending an email
            server.send_message(msg)
            server.quit()
            print("Send")
        except:
            print("Fail to Send")
            pass

    return render_template("Raise_a_query.html")

if __name__ == "__main__":
    app.run(debug=True)
