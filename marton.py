import paramiko
import time

def login(ip_address, port, username, password):
    cl = paramiko.SSHClient()
    cl.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    cl.connect(ip_address, port=port, username=username, password=password, look_for_keys=False, allow_agent=False)
    return cl

def platform_shell(cl):
    shell = cl.invoke_shell()
    return shell

def enter_command(shell, command):
    shell.send(command + '\n')
    time.sleep(2)
    result = shell.recv(4096)
    return result

def close(cl):
    if cl.get_transport().is_active():
        cl.close()


