import sys
import telnetlib
import time

HOST = "{change-this}"
user = "{change-this}"
password = "{change-this}"

# Logs into enable mode with user/pw
tn = telnetlib.Telnet(HOST)
tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
tn.read_until(b"Password: ")
tn.write(password.encode('ascii') + b"\n")
tn.read_until(b">")
tn.write(b"en\n")
tn.read_until(b"Password:")
tn.write(password.encode('ascii') + b"\n")

# Running show cmds
tn.read_until(b"#")
tn.write(b"term len 0\n")
tn.write(b"sh run\n")
tn.read_until(b'#')
tn.write(b"exit\n")
print(tn.read_all().decode('ascii'))

tn.close()