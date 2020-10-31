import marton

servers_login = marton.login('192.168.100.1', 22, 'martins', 'cisco')
server_shell = marton.platform_shell(servers_login)
marton.enter_command(server_shell, 'enable')
marton.enter_command(server_shell, 'cisco')
marton.enter_command(server_shell, 'terminal length 0')
result1 = marton.enter_command(server_shell, 'show run')
print(result1.decode())
marton.close(servers_login)

