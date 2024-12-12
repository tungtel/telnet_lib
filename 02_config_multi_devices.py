import telnetlib
import time
import getpass

r1 = {
    'host':'10.123.2.1',
    'user':'u1'
}

r4 = {
    'host':'10.123.2.4',
    'user':'u1'
}

r5 = {
    'host':'10.123.2.5',
    'user':'u1'
}

routers = [r1,r4,r5]

password = getpass.getpass('Enter your password:')

for router in routers:
    print(f'connecting to {router["host"]}')
    tn = telnetlib.Telnet(host = router['host'] , port = 23)
    tn.read_until(b'Username: ')
    tn.write(router['user'].encode() + b'\n')

    tn.read_until(b'Password: ')
    tn.write(password.encode() + b'\n')

    tn.write(b'terminal length 0\n')

    tn.write(b'show ip interface brief \n')

    tn.write('show version \n'.encode())

    tn.write(b'enable\n')

    tn.write(b'cisco\n')

    tn.write(b'config t\n')

    tn.write(b'username u10 password 0 cisco\n')

    tn.write(b'end\n')

    tn.write(b'exit\n')

    time.sleep(1)

    output = tn.read_all()

    output = output.decode()

    print(output)

    print('#' *50)
