import socket
import sys
import re
import os
import threading
import errno
import time
import json
import uuid

LOG_FLAG=False
BUFFER_SIZE = 2048

# implement this method that modifies the header as specified in the spec
# TODO: IMPLEMENT THIS METHOD
def modify_headers(client_data):
    ''' modify header as specified in the spec''' 
    return client_data # must return the new data with the updated header

# implement this method that parses server info from client data 
# must return 4 tuples of (server_ip, server_port, hostname, isCONNECT)
# TODO: IMPLEMENT THIS METHOD
def parse_server_info(client_data):
    ''' parse server info from client data and
    returns 4 tuples of (server_ip, server_port, hostname, isCONNECT) '''
    
    #replace below lines with correct values as specified in client_data
    server_ip = ""
    server_port = 0
    hostname = ""
    isCONNECT = False # if it is HTTP CONNECT request then set to True otherwise False
    return (server_ip, server_port, hostname, isCONNECT) 

# Creates a subdirectory for the hostname and a new json file
# Do not change this method
def create_log(hostname, incoming_header, modified_header, server_response):
    pathname = "Log/" + hostname
    if not os.path.exists(pathname):
        os.makedirs(pathname, 0o777, exist_ok=True)
        os.chmod('Log', 0o777)
        os.chmod(pathname, 0o777)
    
    json_dict = {
        'Incoming header': incoming_header,
        'Modified header': modified_header,
        'Server reponse received' : server_response
    }
    #Dir/Subdir/hostnameuuid.json
    with open(pathname + "/" + hostname + str(uuid.uuid1()) + ".json", "w+") as outfile:
        json.dump(json_dict, outfile, indent=4)

# Creates a subdirectory for the hostname and a new json file (Use this for CONNECT requests)
# Do not change this method
def create_log2(hostname, incoming_header, response_sent):
    pathname = "Log/" + hostname
    if not os.path.exists(pathname):
        os.makedirs(pathname, 0o777, exist_ok=True)
        os.chmod('Log', 0o777)
        os.chmod(pathname, 0o777)

    json_dict = {
        'Incoming header': incoming_header,
        'Proxy response sent': response_sent,
    }
    #Dir/Subdir/hostnameuuid.json
    with open(pathname + "/" + hostname + str(uuid.uuid1()) + ".json", "w+") as outfile:
        json.dump(json_dict, outfile, indent=4)
        
# A new thread should call this proxy method when starting
# TODO: IMPLEMENT THIS METHOD 
def proxy(client_socket,client_IP):
    '''
    Modify this comment and add your code here
    '''
    global LOG_FLAG
    pass

# TODO: IMPLEMENT THIS METHOD
def main():
    # check arguments
    if(len(sys.argv)!=2 and len(sys.argv)!=3):
        print("Incorrect number of arguments. \nUsage python3 http_proxy.py PORT")
        print("Incorrect number of arguments. \nUsage python3 http_proxy.py PORT Log")
        sys.exit()

    # enable logging
    if(len(sys.argv)==3 and sys.argv[2]=="Log"):
        global LOG_FLAG
        LOG_FLAG = True
        DIR_NAME = "./Log"
        if not (os.path.isdir(DIR_NAME)):
            os.system("mkdir Log")

    ''' Create proper socket(s) and do proper binding.
        Create a new thread whenever new client's TCP connection request arrives
        and let the new thread call proxy method as the thread starts '''

# DO NOT CHANGE THIS METHOD
if __name__ == "__main__":
    main()
