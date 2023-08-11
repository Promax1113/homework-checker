# Homework Checker
#### The program that will solve all the hassle of going to Cosmos and checking your homework.

### Backstory
I have been using the Cosmos app, every Monday they put the homework there, and the app is such an inconvenience. I have to log in then click a few things, also have to go to every page to see the due date. It's truly a waste of time. So I decided to create this program, to help me reduce the time I spent checking it.

### How does it work?
It uses Selenium in harmony with a bunch of other libraries to log in to YOUR Colegia user and check the homework for you. It provides two modes, the email, and the console mode.

#### Email
It is currently disabled. You also need a SendGrid account with a verified email, and it's a hassle. SendGrid does not permit the API key to go public, they just delete it, and I can't do anything about it. I want to keep my code open source, so I can't keep this mode available.

#### Console-based
This is the primary mode of this project. It prints your homework with its due date and a link to its corresponding page.

### How does it login into YOUR account?
It will ask you about your login details, they are saved using encryption and hashes, so the password you use to log in to this program isn't stored as plaintext, after that Selenium's Webdriver will open a hidden Chrome tab and will fetch your homework for you.

#### Don't trust me?
It's ok, you can check the code. If you happen to notice any security flaws, kindly send me a direct message on Twitter at [@promax1113](https://twitter.com/promax1113).
Your data is encrypted using symmetric encryption and the key is your username and password. These are saved in a hash after encrypting your Colegia details so when you login into the program a hash of the entered username and password is compared with the one saved, therefore no sensitive information is displayed as plaintext. Encrypting and decrypting are only available after you have entered your username and password, which makes this program secure. I cannot guarantee that the encryption is unbreakable.

## Let's get to the big stuff, how do I run it?
Download the whole repo as a zip or using ```git clone https://github.com/Promax1113/homework-checker.git```. After that you will need to install the libraries using ```pip install -r requirements.txt``` and that will be all regarding configuration.
Now you should run the main.py and enter the needed details. The first username and password are used to encrypt your Colegia details! 
# **MAKE SURE YOU USE A SAFE PASSWORD**
The rest is pretty straightforward, you will need to answer any other input fields and it will automatically run after all that.

