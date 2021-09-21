note: this page is under construction, feedbacks are always welcomed!

mission statement: There are a lot of amazing cyber security learning resources, my goal is NOT to re-invent the wheels, but to share those resources. 

# resources:
![image](https://user-images.githubusercontent.com/55643200/133610953-34969014-68dc-4e5e-89ee-72f626e53e74.png)

https://www.nist.gov/cyberframework 

OWASP most common attacks
https://owasp.org/www-project-top-ten/




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

------

My learning log

# Sniffing and packet capturing | Sept 20th
https://www.youtube.com/watch?v=4t4kBkMsDbQ
https://www.youtube.com/watch?v=-rSqbgI7oZM
tools used: Ettercap, WireShark, NMap, Linux Shell.



# My thoughts Sept- 21st
If you are new to security and want to land your 1st job in security (just like me) I would highly recommend you to get started with preparing for interview questions. I just did my 1st cyber security interview  and the interviewer asked me 3 questions:
- how to secure a database
- what's the difference between symmetrical encryption and asymmetrical encryption
- how would you design a security system
I was absolutely destroyed... Check out this YouTube channel:
https://www.youtube.com/watch?v=sFIbPS2pCzk


------
Original staff

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
