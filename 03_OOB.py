import time

class Device:
    def __init__(self,host,username,password,port, tn = None):
        self.host = host 
        self.username = username
        self.password = password 
        self.port = port
        self.tn = tn
    
    def connect(self):
        import telnetlib
        self.tn = telnetlib.Telnet(self.host, self.port)
    
    def authenticate(self):
        self.tn.read_until(b'Username: ')
        self.tn.write(self.username.encode() + b'\n')

        self.tn.read_until(b'Password: ')
        self.tn.write(self.password.encode() + b'\n')

    def send_commands(self,command,timeout = 0.5):
        print(f'sending command {command}')
        self.tn.write(command.encode() + b'\n')
        time.sleep(timeout)

    def send_from_list(self,commands):
        for cmd in commands:
            self.send_commands(cmd)

    def show(self):
        output = self.tn.read_all().decode('utf-8')
        return output 

r1 = {
    'host':'10.123.2.1',
    'username':'u1',
    'password':'cisco',
    'port':23
}
r4 = {
    'host':'10.123.2.4',
    'username':'u1',
    'password':'cisco',
    'port':23
}
r5 = {
    'host':'10.123.2.5',
    'username':'u1',
    'password':'cisco',
    'port':23
}

routers = [r1,r4,r5]
commands = ['enable','cisco','terminal length 0','show version','show ip interface brief','exit']
for router in routers: 
    device = Device(host = router['host'],username = router['username'],password= router['password'],port = 23)
    device.connect()
    device.authenticate()
    device.send_from_list(commands = commands)
    output = device.show()
    print(output)
    print('#' * 50 )
