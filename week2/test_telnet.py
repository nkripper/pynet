#!/usr/bin/env python

import telnetlib
import time
import socket
import sys

TELNET_PORT = 23
TELNET_TIMEOUT = 6

#pynet-rtr1 (Cisco 881)
#    ip_addr = 184.105.247.70
#    snmp_port = 161
#    ssh_port = 22
#    username = pyclass
#    password = 88newclass
# =~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
def main():
# =~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
    ip_addr = '184.105.247.70'
    username = 'pyclass'
    password = '88newclass'

    # Open connection to device
    remote_conn = telnetConnect(ip_addr)

    # Login to device
    login(remote_conn,username,password)

    # Disables paging on cisco
    sendCommand(remote_conn,'terminal length 0')

    # Run a specific command and retrieve the output
    output = sendCommand(remote_conn,'show version')
    print output

    # Close connection to device
    remote_conn.close()

# =~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
def login(remote_conn,username,password):
# =~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
    # Look for username
    output = remote_conn.read_until("sername:", TELNET_TIMEOUT)
    remote_conn.write(username + '\n')

    # Look for password
    output += remote_conn.read_until("assword:", TELNET_TIMEOUT)
    remote_conn.write(password + '\n')

    # Sleep for 1 second to allow login to finish and get prompt
    time.sleep(1)
    output += remote_conn.read_very_eager()

    # Return output
    return output

# =~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
def sendCommand(remote_conn, cmd):
# =~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
    # Strip off whitespace and newline on right side to normalize data
    cmd = cmd.rstrip()

    # Write command with single newline
    remote_conn.write(cmd + '\n')

    # Sleep for 1 second
    time.sleep(1)

    # Store output of command
    output = remote_conn.read_very_eager()

    # Return output
    return output

# =~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
def telnetConnect(ip_addr,telnet_port=TELNET_PORT,telnet_timeout=TELNET_TIMEOUT):
# =~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
    # Try to open connection to device, if successful, return connection
    try:
        return telnetlib.Telnet(ip_addr, telnet_port, telnet_timeout)
    # If attempt times out, exit with appropriate error message
    except socket.timeout:
        sys.exit("Connection timed out");

if __name__ == "__main__":
    main()
