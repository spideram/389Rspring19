OSINT (Open Source Intelligence)
======

## Assignment details

This assignment has two parts. It is due by Friday, February 22 at 11:59 PM.

To submit your homework, please follow the guidelines posted under the grading section of the syllabus.

**There will be a late penalty of 5% off per day late! Submissions received more than 3 days late will receive a 0!**

### Part 1

In class you were given an online usertag: `v0idcache`

NOTE: "briefly describe" = 2-3 sentences (and/or include screenshot(s))

Use OSINT techniques to learn as much as you can about `v0idcache` and answer the following questions:

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

### Part 2

Use the provided python stub code [('stub.py')](stub.py) or write your own program in another language to gain access to `v0idcache`'s server via an open port that you should have found in Part 1.

Once you have gained access to `v0idcache`'s account with the correct login credentials, you will have access to a system shell.

Use your knowledge of Linux and OSINT techniques to locate the flag file and submit its contents for points.

Your response here should briefly document how you approached and solved this part of the assignment. You should also push your bruteforce program to the "week/2/writeup" folder of your GitHub repository.

Note: If you choose to write your own program in another language, please include instructions on how to execute your program, including what version of the language you are using. You will **NOT** receive credit if the TAs cannot run your program.

If you are stuck on this part of the assignment, let us know! The facilitator staff is here to help and teach, and we are open to releasing hints as time goes on!

The way I combatted this problem I broke it into steps. The first step was to be able to access the wordlist and be able to iterate through it. After that was done, I needed to be able to receive the data I was gathering. After getting the data, I needed to send the data to the server. After that, all I had to do is wait for the right password to come appear.


### Format
In the "week/2/writeup" directory of our repository there is a README.md file for you to edit and submit your homework in. Use this as a template and directly edit it with your answers. Complete your bruteforce program in this directory as well. When you've finished the assignment, push it up to your personal GitHub for us to grade.

Your responses to every prompt in this assignment should include answers to any specific questions along with a brief explanation of your thought process and how you obtained the answer.

### Scoring

Part 1 is worth 45 points, and part 2 is worth 55 points.

### Tips

Reference the slides from lecture 2 to help you effectively utilize available OSINT techniques.
