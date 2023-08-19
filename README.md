# Homework Checker

#### Here is the program that will eliminate the hassle of going to Cosmos and checking your homework.

### Backstory

I have been using the Cosmos application. Every Monday they post homework there, and the app is extremely inconvenient. To view the due date, I must log in, then click a few things, and then go to each page. It's truly a waste of time. So I decided to create this program to help me reduce the time I spend checking it.

### How does it work?

Using Selenium, the application logs into your Colegia user and checks your homework for you. The program is available in two modes, email and console.

#### Email

Currently, it is disabled. You also need a SendGrid account with a verified email, and it's a hassle.  SendGrid does not permit the API key to go public. They just delete it, and I can't do anything about it. I want to keep my code open source, so I can't keep this mode available.

#### Console-based

This is the primary mode of this project. It prints your homework's due date and a link to its corresponding page.

### How does it login into YOUR account?

It will ask you about your login details, they are saved using encryption and hashes, so the password you use to log in to this program isn't stored as plaintext, after that Selenium's Webdriver will open a hidden Chrome tab and will fetch your homework for you.

## Don't trust me?

It's OK, you can check the code. If you happen to notice any security flaws, kindly send me a direct message on Twitter at [@promax1113](https://twitter.com/promax1113). Your data is encrypted using symmetric encryption and the key is your username and password. These are saved in a hash after encrypting your Colegia details so when you login into the program a hash of the entered username and password is compared with the one saved, therefore no sensitive information is displayed in plaintext. Encrypting and decrypting are only available after you have entered your username and password, which makes this program secure. However, I cannot guarantee that the encryption or hashes are unbreakable. 

### Let's get to the big stuff, how do I run it?

Download the whole repo as a zip or using ```git clone https://github.com/Promax1113/homework-checker.git```. After that, you will need to install the libraries using ```pip install -r requirements.txt``` and that will be all regarding configuration. Now you should run the main.py and enter the needed details. The first username and password are used to encrypt your Colegia details!

# MAKE SURE YOU USE A SAFE PASSWORD

The rest is pretty straightforward. You'll need to answer any other input fields and it will automatically run after all that.