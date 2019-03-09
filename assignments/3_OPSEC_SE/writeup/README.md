# Writeup 3 - Operational Security and Social Engineering

Name: Ramsay Farah
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Ramsay Farah

## Assignment Writeup

### Part 1 (40 pts)

Firstly, when I call her, I would pose as her someone who is maintaining her 1337Bank server. In the background I would have office workers to show that I am working in an official environment. I would begin by saying that we need to ask some basic security questions to verify it is her. I would first ask for her mother's maiden name, and after she answers, I would say that she is correct. Then I would ask what city she was born in and then the name of her first pet. After that, I would ask to make sure she is able to login to her site. I would tell her to choose any browser she likes, Chrome, Internet Explorer, or Fire Fox And ask which she chooses. I would then have her login to her site and once she does I would say every is clear over here as well, thank you.

In order to get the ATM pin number, I would first set up an email for the company and learn how they format their emails. After that I send Elizabeth and email from the company saying her pin number is about to expire and say she can use the link below to update it which would go to a dummy website. The dummy website would take what her current and new pin is and store them. Then using her credentials in her own website would change her pin to the new one.

### Part 2 (60 pts)

Vulnerabilities
- using the same username for everything
- weak password
- can use unlimited amount of attempts for password

Elizabeth, firstly I would recommend not having the same password for every account, while this makes things easier for you, it also makes things easier for us. I would also recommend making a stronger password with more than just lower case letters. I would throw in some upper case letters, special characters, numbers, and do not make it similar to an actual word. Webroot.com says the aspects of a strong password are length (the longer the better); a mix of letters (upper and lower case), numbers, and symbols, no ties to your personal information, and no dictionary words. Lastly, I would recommend having a limited number of attempts to access the server or website. I was able to brute force my way in because of the lack of constraints. Computerweekly.com says to implement an account lockout policy. For example, after three failed login attempts, the account is locked out until an administrator unlocks it.
