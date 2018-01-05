
from read_xml import Read_xml
from ssh_connect import Ssh_connect
from puthandler import PUTHandler
from threading import Thread
from BaseHTTPServer import HTTPServer



# function for starting the Server
def run_on(port):
    print("Starting a server on port %i" % port)
    server_address = ('localhost', port)
    httpd = HTTPServer(server_address, PUTHandler)
    httpd.serve_forever()





#main function
if __name__ == "__main__":
    #connect to the clients and upload script
    Ssh_connect(Read_xml.ips, Read_xml.ports, Read_xml.usernames, Read_xml.passwords)


    #run Server in new thread
    server = Thread(target=run_on, args=[8080])


    # Do not make us wait for you to exit
    server.daemon = True
    server.start()
    while 1:
        pass

