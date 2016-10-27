#!/usr/bin/python

import telnetlib

TELNET_PORT = 23
TELNET_TIMEOUT = 6

def main():
    ip_addr = '192.168.253.147'
    username = 'nkeeling'
    password = ''

    remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)

    remote_conn.close()

if __name__ == "__main__":
    main()
