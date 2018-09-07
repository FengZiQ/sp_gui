# coding=utf-8
import paramiko
import time
from configuration_file import config_data


def view_log(log_server, cmd):

    # 连接ssh
    ssh = paramiko.SSHClient()
    # 允许连接不在known_hosts文件上的主机
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #
    ssh.connect(
        hostname=config_data['log_server'],
        username=config_data['log_username'],
        password=config_data['log_pwd']
    )
    # 建立一个通道
    c = ssh.invoke_shell()

    # data接收通道返回数据的可变对象; timer：每个while最长运行5s后break
    result = {'data': '', 'timer': 0}

    # 发送go，打开跳板列表
    while True:
        result['data'] += c.recv(9999).decode('utf-8')
        time.sleep(1)
        result['timer'] += 1
        if result['data'].endswith(']$ ') or result['data'].endswith(']# ') or result['timer'] == 5:
            # print(result['data'])
            c.send('go\n')
            result['data'] = ''
            result['timer'] = 0
            break

    # 选择跳板
    while True:
        result['data'] += c.recv(9999).decode('utf-8')
        time.sleep(1)
        result['timer'] += 1
        if result['data'].endswith('enter your choice\r\n') or result['timer'] == 5:
            # print(result['data'])
            c.send(log_server + '\n')
            result['data'] = ''
            result['timer'] = 0
            break

    # 发送查看log命令
    while True:
        result['data'] += c.recv(9999).decode('utf-8')
        time.sleep(1)
        result['timer'] += 1
        if result['data'].endswith(']$ ') or result['data'].endswith(']# ') or result['timer'] == 5:
            # print(result['data'])
            c.send(cmd + '\n')
            result['data'] = ''
            result['timer'] = 0
            break

    # 返回log内容
    while True:
        result['data'] += c.recv(9999).decode('utf-8')
        time.sleep(1)
        result['timer'] += 1
        if result['data'].endswith(']$ ') or result['data'].endswith(']# ') or result['timer'] == 5:
            # print(result['data'])
            break
    # print(result['timer'])
    ssh.close()
    return result['data']


if __name__ == "__main__":
    con = view_log('dm1p', 'tail -n 100 /data/log/inspos-dm-ppcp2.log | grep "name"')
    print(con)
