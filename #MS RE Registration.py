print("Hi programmers !")
print("Let's start Microsoft software engineering registration")

name = input("Enter your name:")
print("Hi" , name + "!")

age = input("Enter your age:")
print(age , "years old" )

country = input("Enter your country name:")
print(country)

number = input("Enter your phonenumber:")
print(number)

gmail = input("Enter your Gmail Address:")
print("Your gmail address is" , gmail )

password = input("Enter your passwrd:")
print("******")

print(name)
print(age)
print(country)
print(number)
print(gmail)
print("*****")

print("Correct all detail.")

import time

print("Please go to this side and verify your registration")
print("Please wait some seconds....")

#for card processing
time.sleep(5)

import webbrowser
webbrowser.open('file:///F:/HTML/%23Regis.html', new=10)
