import time 
import telnetlib
#define a class telnet_to_deice including host,username,password,etc parameters 
#inside class , define class attribute 

class telnet_to_device:
    def __init__(self,host,username,password,port = 23 ,tn = None):
        self.host = host
        self.username = username
        self.password = password 
        self.port = port 
        self.tn = tn

#define a connec method 
    def connect(self): 
        self.tn = telnetlib.Telnet(self.host,self.port)

#define authenticate to enter username and password 
    def authenticate(self):
        self.tn.read_until(b'Username: ')
        self.tn.write(self.username.encode() + b'\n')
        self.tn.read_until(b'Password: ')
        self.tn.write(self.password.encode() + b'\n')

#define send command method 
#command are read from txt file 
    def send_command_from_file(self,filename,timeout = 1):
        with open(filename,'r') as f:
            commands = f.read().splitlines()
        print(f'sending commands...')
        for cmd in commands: 
            self.tn.write(cmd.encode() + b'\n')
            time.sleep(timeout)

#define functionn o printout entire output 
    def print_output(self):
        output = self.tn.read_all()
        output = output.decode('utf-8')
        print(output)
        self.tn.close()


if __name__ == '__main__':

    r1 = {
    'host':'10.123.2.1',
    'username':'u1',
    'password':'cisco'
    }

    device = telnet_to_device(r1['host'],r1['username'],r1['password'] , port = 23)
    device.connect()
    device.authenticate()
    device.send_command_from_file(filename = 'commands1.txt')
    device.print_output()

