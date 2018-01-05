#! /usr/bin/env python

import psutil
import time
import httplib
import json

from Crypto.Cipher import AES
import base64













def send():

    cpu = psutil.cpu_percent(interval=1, percpu = True)
    memory = psutil.virtual_memory()[2] #percentage!
    boot_time = psutil.boot_time()
    time_now = float(time.time())
    uptime = time_now - boot_time
    print cpu
    print memory
    print uptime

    secret_key = '4569803458932015' # create new & store somewhere safe
    cipher = AES.new(secret_key,AES.MODE_ECB) # never use ECB in strong systems obviously
    cpu_enc = base64.b64encode(cipher.encrypt(str(cpu).rjust(32)))
    memory_enc= base64.b64encode(cipher.encrypt(str(memory).rjust(32)))
    uptime_enc=base64.b64encode(cipher.encrypt(str(uptime).rjust(32)))

    data_to_update = json.dumps({ "cpu" : cpu_enc,
                                  "memory": memory_enc,
                                  "uptime":uptime_enc
                                })
    try:
        conn = httplib.HTTPConnection("127.0.0.1", 8080)
        conn.request("PUT", "/1", data_to_update)
        response = conn.getresponse()
        print response.status, response.reason
        if "OK" in response.reason:
            return send()
        else:
            print response.reason

    except:
        return send()



if __name__ == '__main__':

    while True :
        send()


