![image](https://user-images.githubusercontent.com/55643200/135366675-29992b6d-20e8-4aff-be42-5a8c49ae3a1c.png)
### McMaster Engieering Cyber Security Curriculum Development

note: this page is under construction, feedbacks are always welcomed! Have question? send us a message: guany27@mcmaster.ca

mission statement: There are a lot of amazing cyber security learning resources, my goal is NOT to re-invent the wheels, but to share those resources and my learning journey with you. 

Suggestions: I think there are 3 learning phases: 
- phase 1: foster interest by exploring the technology, read books, coffee-chatting with professionals
- phase 2: getting more serious: join a security bounty program, 
- phase 3: job/co-op

# resources:
![image](https://user-images.githubusercontent.com/55643200/133610953-34969014-68dc-4e5e-89ee-72f626e53e74.png)

https://www.nist.gov/cyberframework 

OWASP most common attacks
https://owasp.org/www-project-top-ten/


Elastic Search:
https://www.elastic.co/security


# Microsoft Security courses:
free courses with certificates!

https://docs.microsoft.com/en-us/learn/modules/security-in-m365/ 

https://docs.microsoft.com/en-ca/learn/modules/explore-security-dashboard/ 

https://docs.microsoft.com/en-ca/learn/modules/network-fundamentals-2/ 


# Recommended Youtube Channel:
https://www.youtube.com/user/NetworkChuck


# Microsoft security products:
https://security.microsoft.com/securityreports 

https://compliance.microsoft.com/homepage 

https://usernmae.portal.cloudappsecurity.com/#/dashboard 

----------------------------------------------

My learning log

# Honey pot | Sept 27th
https://github.com/cowrie/cowrie
What is Cowrie

https://www.youtube.com/watch?v=VoyS0euqHsw
deploying honey pot with T-pot; T-Pot is developed by german IT giant Deutsche Telekom

Cowrie is a medium to high interaction SSH and Telnet honeypot designed to log brute force attacks and the shell interaction performed by the attacker. In medium interaction mode (shell) it emulates a UNIX system in Python, in high interaction mode (proxy) it functions as an SSH and telnet proxy to observe attacker behavior to another system.

![Udacity](https://user-images.githubusercontent.com/55643200/134197106-d078a537-6ab1-465c-8d7a-51fbd01f3a93.png)
What is a DMZ in networking?

In computer networks, a DMZ, or demilitarized zone, is a physical or logical subnet that separates a local area network (LAN) from other untrusted networks -- usually, the public internet. DMZs are also known as perimeter networks or screened subnetworks.

https://www.virustotal.com/gui/home/upload
Analyze suspicious files and URLs to detect types of malware, automatically share them with the security community

https://www.chappell-university.com/post/geoip-mapping-in-wireshark
https://www.wireshark.org/lists/wireshark-dev/200902/msg00154.html

# Chat with Alex

key points:

- Certification matters: A good example is: PCI-DSS Payment Card Industry Data Security Standard 
- Legacy weakness: old telnet, old email protacals can bypass security rules
- Cyber security itself is preventative, always anticipating something bad, not a lot of details. By contrast, developers work on creating more "interesting" tools and complicated Python scripts.

# Sniffing and packet capturing | Sept 20th
https://www.youtube.com/watch?v=4t4kBkMsDbQ
https://www.youtube.com/watch?v=-rSqbgI7oZM
tools used: Ettercap, WireShark, NMap, Linux Shell.

Use nmap to scan your local router
nmap -sn 192.168.0.1/24

Ettercap is a man in the attack tool. The below command will sniff ( collect packet) from the local ip address 192.168.0.81
sudo ettercap -T -S -i wlp0s20f3 -M arp:remote /192.168.0.1// /192.168.0.81//

(new ternmial)
Use Wireshark to furthure capture and analyze packets
sudo wireshark


# Security interview | Sept 8th
If you are new to security and want to land your 1st job in security (just like me) I would highly recommend you to get started with preparing for interview questions. I just did my 1st cyber security interview  and the interviewer asked me 3 questions:
- how to secure a database
- what's the difference between symmetrical encryption and asymmetrical encryption
- how would you design a security system
I was absolutely destroyed... Check out this YouTube channel:
https://www.youtube.com/watch?v=sFIbPS2pCzk


------


### IoT Security - Node Red

- Enabling HTTPS on Node Red: https://www.youtube.com/watch?v=z9a_ztJqaII&t=681s

Step 1. Go to your Node-Red location

cd / home / yuxiang (your username) / .node-red

Step 2. Generate 1024 bytes certificate

openssl genrsa -out privkey.pem 1024

Step 3. use private key to create Certificate Signing Request

openssl req -new -key privkey.pem -out private-csr.pem

Step 4. use Certificate Signing Request to generate Certificate

openssl x509 -req -days 365 -in private-csr.pem -signkey privkey.pem -out cert.pem

Step 5. modify the settings.js file

nano / home / yuxiang (your username) / .node-red

Step 6. add this line before any code:

var fs = require("fs");

Step 7. uncomment the following:

https: { key: require("fs").readFileSync('/home/yuxiang/.node-red/privkey.pem'), cert: require("fs").readFileSync('/home/yuxiang/.node-red/cert.pem') },

Step 8. Control S to save and Control X to exit

Step 9. re-Launch your node-red

node-red

you should see: Server now running at https://127.0.0.1:1880/ in the command prompt
