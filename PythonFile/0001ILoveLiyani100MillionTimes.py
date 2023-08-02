from socket import socket


def main():
    # 1.创建套接字对象默认使用IPv4和TCP协议
    client = socket()
    # 2.连接到服务器(需要指定IP地址和端口)
    client.connect(('127.0.0.1', 6789))
    # 3.从服务器接收数据
    print(client.recv(1024).decode('utf-8'))
    client.close()


if __name__ == '__main__':
    main()


# Bitski
# one_leaf_across_the_ocean
# 125423559@qq.com
# wdRd3NPkLFccC2h
# gamemk iff8WDgXZR4GMjw
# wall 0xd0309dec4d9e2b750ea397e1c8a2035cb8fe7e93