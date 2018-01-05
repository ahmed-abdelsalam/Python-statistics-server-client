import paramiko
import socket
import time

class Ssh_connect:


    def __init__(self,ips,ports,usernames,passwords):

        for x in range(0, len(ips)):
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(ips[x], int(ports[x]), username=usernames[x], password=passwords[x], timeout=2)
                stdin, stdout, stderr=ssh.exec_command('uname')
                sftp = ssh.open_sftp()
                sftp.put('monitor.py', '/tmp/monitor.py')
                print "Client script is transferred to client number :" + str(x + 1)
                sftp.close()
                channel = ssh.invoke_shell()
                time.sleep(2)
                if stdout.read():
                    stdin, stdout, stderr = ssh.exec_command('python /tmp/monitor.py')
                else:
                    channel.send('cd ../\n')
                    channel.send('cd ../\n')
                    channel.send('python tmp/monitor.py\n')

                # time.sleep(3)
                # output = channel.recv(2024)
                # print(output)
                ssh.close()

            except paramiko.ssh_exception.AuthenticationException:
                print "the username or  password is incorrect for client number :" + str(x + 1)
            except socket.timeout:
                print "the client number :" + str(x + 1) + " is not responding ... check IP or port"
            except paramiko.ssh_exception.NoValidConnectionsError:
                print "the client number : "  + str(x + 1) + " refused connection ... check SSH "
            except:
                print "there is error in communication with client number" + str(x)










