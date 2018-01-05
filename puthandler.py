
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import json
from Crypto.Cipher import AES
import base64
from db import DB
from mail import Mail
import numpy as np
from read_xml import Read_xml
class PUTHandler(BaseHTTPRequestHandler ):


    #function to handle PUT REQUESTS
    def do_PUT(self):
        ips = Read_xml.ips
        alerts = Read_xml.alerts
        mails = Read_xml.mails
        ip = str(self.headers).split(" ")[1].split(":")[0]
        length = int(self.headers['Content-Length'])
        content = self.rfile.read(length)


        #Send PUT Respond
        self.send_response(200)


        #Decryption the incoming data from HHTP PUT Request
        secret_key = '4569803458932015'
        cipher = AES.new(secret_key,AES.MODE_ECB)
        cpu = cipher.decrypt(base64.b64decode(json.loads(content)["cpu"]))
        cpu = eval(cpu)
        memory = cipher.decrypt(base64.b64decode(json.loads(content)["memory"]))
        memory = float(memory)
        uptime = cipher.decrypt(base64.b64decode(json.loads(content)["uptime"]))
        uptime=float(uptime)



        #Storing the data to the database
        DB(cpu, memory, uptime, ip)



        #check for Alerts to send mail
        index = 0
        for check in ips:
            if ip == check:
                if alerts[index,0][0] == 'memory':
                    if memory >= float(str(alerts[index,0][1]).split("%")[0]):
                        Mail(index,cpu, memory, mails)
                    else:
                        pass
                elif alerts[index,1][1] == 'cpu':
                    if np.mean(cpu) >= float(str(alerts[index,1][1]).split("%")[0]):
                        Mail(index,cpu, memory, mails)
                    else:
                        pass
            else:
                print " couldn't find the IP of the alerted client"
            index += 1





