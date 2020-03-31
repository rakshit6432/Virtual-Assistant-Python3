# This is a Virtual Assistant called "Py Assistant" that is in beta and will be forever.
print("Booting up...")
import datetime # Imports system date and time
print("10%")
import smtplib, ssl # Imports modules needed to send emails
print("20%")
import random # Imports module 'random'
import face_recognition # Imports module to identify faces
print("30%")
from covid import Covid # Imports module to track 'COVID-19' virus live
covid = Covid()
import numpy as np # Imports module numpy
print("40")
import tkinter as tk # Imports module 'Tkinter'
import speech_recognition as sr # Import module to turn speech into text
print("50%")
import os # Imports 'os' module
import duckduckgo # Imports module to search DuckDuckGo
print("60%")
import cv2 # Imports camera module
print("70")
import sys # Imports 'system' module
print("80%")
import logging as log # Imports 'logging' module
print("90%")
from time import sleep # Imports module to pause for a few seconds
print("100%")

# Load a owner's picture and learn how to recognize it.
owner1_image = face_recognition.load_image_file("file1.jpg")
owner1_face_encoding = face_recognition.face_encodings(owner1_image)[0]
# Load a second owner's picture and learn how to recognize it.
owner2_image = face_recognition.load_image_file("file2.jpg")
owner2_face_encoding = face_recognition.face_encodings(owner2_image)[0]

r = sr.Recognizer() # Sets up speech recogniion
mic = sr.Microphone() # Selects default microphone

remembers = [] # Creates list to remember things

print("Hi! My name is PyAssistant")
while True:
    # Remembers owners' faces
    known_face_encodings = [
        owner1_face_encoding,
        owner2_face_encoding,
    ]
    known_face_names = [
        "Owner1",
        "Owner2"
    ]

    face_locations = [] # Creates list for face location
    face_encodings = [] # Creates list for face encoding
    face_names = [] # Creates list for face names
    process_this_frame = True
    video_capture = cv2.VideoCapture(0) # Starts camera window
    while True:
        # Adjusts camera window
        ret, frame = video_capture.read() 
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        
        if process_this_frame:
            # Finds all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                face_names.append(name)
        process_this_frame = not process_this_frame
        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        cv2.imshow('Video', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            # Break loop if 'q' is pressed
            break
        if not(face_names == []):
            # Break loop if faces are found
            break
    
    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()
    
    if (if "Unkown" in face_names):
        # Introduces itself to the unknown face
        print("Hi! My name is PyAssistant")
        os.system("say 'Hi! My name is PyAssistant'")
        print("You seem to be a guest. Here are a list of things you can ask me:")
        os.system("say 'You seem to be a guest. Here are a list of things you can ask me'")
        print("CLOCK = 'What is the time?'")
        print("CALENDAR = 'What is today's date?'")
        print("ENTERTAINMENT = 'Let's play a game'")
        print("ENTERTAINMENT = 'Tell me a joke'")
        print("MATH = 'Add two numbers'")
        print("MATH = 'Subtract two numbers'")
        print("MATH = 'Multiply two numbers'")
        print("MATH = 'Divide two numbers'")
        print("MATH = 'Find the remainder of two numbers'")
        print("INTERNET = 'Search the web.'")
        print("CORONAVIRUS = 'Track Coronavirus.'")
    else:
        # Says hello to owner
        print("Hello")
        os.system("say 'Hello'")
        
    # Starts Speech Recognition
    with mic as source:
        r.adjust_for_ambient_noise(source) # Adjusts for ambient noise
        audio = r.listen(source) # Starts listening to voice
        question = r.recognize_google(audio) # Saves recognised speech as text in variable
    print(question)

    # Tries to answer question
    if (question == "what is the time"):
        print("Here's the time:")
        os.system("say 'Here is the time.'")
        print(datetime.datetime.now().time()) # Prints system time
        
    elif (question == "do you know python"):
        print("Actually, I am made up of python.")
        os.system("say 'Actually, I am made up of python'")
        
    elif (question == "how are you"):
        print("Oh! I am fine. I Hope you are too")
        os.system("say 'Oh! I am fine. I hope you are too.'")
        
    elif (question =="hello"):
        print("Hello to you too!")
        os.system("say 'Hello to you too!'")
        
    elif (question == "what is today's date"):
        print("Here's today's date:")
        os.system("say 'Here is todays date.'")
        print(datetime.date.today()) # Prints system date
        
    elif (question == "can you remember something"):
        # Deny feature to guest if face is unknown
        if (face_names == ['Unknown']):
            print("You seem to be a guest. You are denied of this feature")
            os.system("say 'You seem to be a guest. You are denied of this feature'")
        else:
            print("Yes, what is it?")
            os.system("say 'yes. what is it'")
            with mic as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            remembe = r.recognize_google(audio)
            remembers.append(remembe) # Add recognised speech to list
        
            print("I'll try and remember that!")
            os.system("say 'I will try and remember that.'")
            
    elif (question == "what did I ask you to remember"):
        if (face_names == ['Unknown']):
            print("You seem to be a guest. You are denied of this feature")
            os.system("say 'You seem to be a guest. You are denied of this feature'")
        else:
            print("Here is what you asked me to remember:")
            os.system("say 'here is what you asked me to remember'")
            print(remembers)
            
    elif (question == "let's play a game"):
        print("Oh! Rock, Paper, Scissors! Game on!")
        os.system("say 'Oh! Rock paper scissors. game on.'")
        window = tk.Tk() # Start Tkinter window
        window.geometry("400x300") # Adjust window size
        window.title("PyAssistant Rock, Paper,Scissors") # Set window title
        # Create variables for choices and scores
        USER_SCORE = 0
        COMP_SCORE = 0
        USER_CHOICE = ""
        COMP_CHOICE = ""
        # Define functions related to the choice and score
        def choice_to_number(choice):
            rps = {'rock':0,'paper':1,'scissor':2}
            return rps[choice]
        def number_to_choice(number):
            rps={0:'rock',1:'paper',2:'scissor'}
            return rps[number]
        def random_computer_choice():
            return random.choice(['rock','paper','scissor'])
        def result(human_choice,comp_choice):
            global USER_SCORE
            global COMP_SCORE
            user=choice_to_number(human_choice)
            comp=choice_to_number(comp_choice)
            if(user==comp):
                print("Tie")
            elif((user-comp)%3==1):
                print("You win")
                USER_SCORE+=1
            else:
                print("Comp wins")
                COMP_SCORE+=1
            text_area = tk.Text(master=window,height=12,width=30,bg="#FFFF99")
            text_area.grid(column=0,row=4)
            answer = "Your Choice: {uc} \nComputer's Choice : {cc} \n Your Score : {u} \n Computer Score : {c} ".format(uc=USER_CHOICE,cc=COMP_CHOICE,u=USER_SCORE,c=COMP_SCORE)    
            text_area.insert(tk.END,answer)
        def rock():
            global USER_CHOICE
            global COMP_CHOICE
            USER_CHOICE='rock'
            COMP_CHOICE=random_computer_choice()
            result(USER_CHOICE,COMP_CHOICE)
        def paper():
            global USER_CHOICE
            global COMP_CHOICE
            USER_CHOICE='paper'
            COMP_CHOICE=random_computer_choice()
            result(USER_CHOICE,COMP_CHOICE)
        def scissor():
            global USER_CHOICE
            global COMP_CHOICE
            USER_CHOICE='scissor'
            COMP_CHOICE=random_computer_choice() 
            result(USER_CHOICE,COMP_CHOICE)
        # Create a button 'Rock'
        button1 = tk.Button(text="       Rock       ",bg="skyblue",command=rock)
        button1.grid(column=2,row=1)
        # Create a button 'Paper'
        button2 = tk.Button(text="       Paper      ",bg="pink",command=paper)
        button2.grid(column=2,row=2)
        # Create a button 'Scissors'
        button3 = tk.Button(text="      Scissor     ",bg="lightgreen",command=scissor)
        button3.grid(column=2,row=3)
        # Open the Tkinter window
        window.mainloop()
        # Check for winner
        if(USER_SCORE < COMP_SCORE):
            print("I win!")
            os.system("say 'I win'")
        elif(USER_SCORE > COMP_SCORE):
            print("Oh no! you win!")
            os.system("say 'oh no. you win'")
        else:
            print("It's a tie!")
            os.system("say 'its a tie'")
    elif (question == "what can you do"):
        if (face_names == ['Unknown']):
            print("You seem to be a guest. Here are a list of things guest can ask:")
            os.system("say 'You seem to be a guest. Here are a list of things guests can ask'")
            print("CLOCK = 'What is the time?'")
            print("CALENDAR = 'What is today's date?'")
            print("ENTERTAINMENT = 'Let's play a game'")
            print("ENTERTAINMENT = 'Tell me a joke'")
            print("MATH = 'Add two numbers'")
            print("MATH = 'Subtract two numbers'")
            print("MATH = 'Multiply two numbers'")
            print("MATH = 'Divide two numbers'")
            print("MATH = 'Find the remainder of two numbers'")
            print("INTERNET = 'Search the web'")
            print("CORONAVIRUS = 'Track Coronavirus.'")
        else:
            print("Here are a list of things you can ask me:")
            os.system("say 'here are a list of things you can ask me'")
            print("CLOCK = 'What is the time?'")
            print("CALENDAR = 'What is today's date?'")
            print("NOTES = 'Can you remember something?'")
            print("NOTES = 'What did I ask you to remember?'")
            print("ENTERTAINMENT = 'Let's play a game'")
            print("ENTERTAINMENT = 'Tell me a joke'")
            print("CAMERA = 'Take a Photo'")
            print("EMAIL = 'Send an Email'")
            print("MATH = 'Add two numbers'")
            print("MATH = 'Subtract two numbers'")
            print("MATH = 'Multiply two numbers'")
            print("MATH = 'Divide two numbers'")
            print("MATH = 'Find the remainder of two numbers'")
            print("INTERNET = 'Search the web'")
            print("CORONAVIRUS = 'Track Coronavirus.'")
    elif (question == "take a picture"):
        if (face_names == ['Unknown']):
            print("You seem to be a guest. You are denied of this feature")
            os.system("say 'You seem to be a guest. You are denied of this feature'")
        else:
            print("What should I save your picture as?")
            os.system("say 'What should I save your picture as?'")
            with mic as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            image_name = r.recognize_google(audio)
            print("Taking a picture")
            os.system("say 'Taking a picture.'")
            # Setup camera window
            key = cv2. waitKey(1)
            webcam = cv2.VideoCapture(0)
            # Takes  picture
            check, frame = webcam.read()
            cv2.imshow("Capturing", frame)
            key = cv2.waitKey(1)
            cv2.imwrite(filename=image_name + '.jpg', img=frame)
            webcam.release()
            img_new = cv2.imread(image_name + '.jpg', cv2.IMREAD_GRAYSCALE)
            img_new = cv2.imshow("Captured Image", img_new)
            cv2.waitKey(1650)
            cv2.destroyAllWindows()
            print("Image saved!")
            
    elif (question == "send an email"):
        if (face_names == ['Unknown']):
            print("You seem to be a guest. You are denied of this feature")
            os.system("say 'You seem to be a guest. You are denied of this feature'")
        else:
            port = 587  # For starttls
            os.system("say 'Please enter your username and password'")
            sender_email = input("Username(Email)")
            if ("@outlook" in sender_email):
                print("Logging into Outlook...")
                os.system("say 'logging into outlook'")
                smtp_server = "smtp.outlook.com"
            elif ("@gmail" in sender_email):
                print("Logging into Gmail...")
                os.system("say 'logging into G mail'")
                smtp_server = "smtp.gmail.com"
            elif ("@icloud" in sender_email):
                print("Logging into Icloud...")
                os.system("say 'logging into I cloud'")
                smtp_server = "smtp.icloud.com"
            elif ("@yahoo" in sender_email):
                print("Logging into Yahoo...")
                os.system("say 'logging into yahoo'")
                smtp_server = "smtp.yahoo.com"
            else:
                print("Can't find Server")
                os.sysem("say 'cannot find server'")
                smtp_server = input("Please enter smtp server smtp.server.com : ")
            password = input("Type your password and press enter: ")
            receiver_email = input("Please enter your recievers email address: ")
            print("What is your Subject?")
            os.system("say 'What is your subject'")
            with mic as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            sub = r.recognize_google(audio)
            print("Subject: " + sub)
            print("What's your content?")
            with mic as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            content = r.recognize_google(audio)
            print("Subject: " + content)
            message = """\
            Subject: """ + sub + " " + content +" -Sent by PyAssistant for Linux."
            choice = "None"
            while not (choice == "yes") or (choice == "no"):
                os.system("say 'Do you want to send this E mail.")
                choice ="Do you want to send this email? (yes / no)"
                with mic as source:
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                choice = r.recognize_google(audio)
            if (choice == "yes"):
                context = ssl.create_default_context()
                with smtplib.SMTP(smtp_server, port) as server:
                    server.ehlo()  # Can be omitted
                    server.starttls(context=context)
                    server.ehlo()  # Can be omitted
                    server.login(sender_email, password) # Login with username and password
                    server.sendmail(sender_email, receiver_email, message) # Send email to receiver
                    print("Email Sent")
                    
    elif(question == "add two numbers"):
        print("What is your first number?")
        os.system("say 'what is your first number'")
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        number1 = r.recognize_google(audio)
        print("What is your second number?")
        os.system("say 'what is your second number'")
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        number2 = r.recognize_google(audio)
        ans = float(number1) + float(number2) # Turn strings into decimals and add them
        sayer = "say 'the sum of " + str(number1) + " and " + str(number2) + " is " + str(ans) + "'"
        print("The sum of " + str(number1) + " and " + str(number2) + " is " + str(ans) + " ") # Print answer by turning decimals into strings
        os.system(sayer)
    elif(question == "subtract two numbers"):
        print("What is your first number?")
        os.system("say 'what is your first number'")
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        number1 = r.recognize_google(audio)
        print("What is your second number?")
        os.system("say 'what is your second number'")
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        number2 = r.recognize_google(audio)
        ans = float(number1) - float(number2)
        sayer = "say 'the subraction of " + str(number1) + " and " + str(number2) + " is " + str(ans) + "'"
        print("The subtraction of " + str(number1) + " and " + str(number2) + " is " + str(ans) + " ")
        os.system(sayer)
    elif(question == "multiply two numbers"):
        print("What is your first number?")
        os.system("say 'what is your first number'")
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        number1 = r.recognize_google(audio)
        print("What is your second number?")
        os.system("say 'what is your second number'")
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        number2 = r.recognize_google(audio)
        ans = float(number1) * float(number2)
        sayer = "say 'the multiplication of " + str(number1) + " and " + str(number2) + " is " + str(ans) + "'"
        print("The multiplication of " + str(number1) + " and " + str(number2) + " is " + str(ans) + " ")
        os.system(sayer)
    elif(question == "divide two numbers"):
        print("What is your first number?")
        os.system("say 'what is your first number'")
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        number1 = r.recognize_google(audio)
        print("What is your second number?")
        os.system("say 'what is your second number'")
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        number2 = r.recognize_google(audio)
        ans = float(number1) / float(number2)
        sayer = "say 'the division of " + str(number1) + " and " + str(number2) + " is " + str(ans) + "'"
        print("The division of " + str(number1) + " and " + str(number2) + " is " + str(ans) + " ")
        os.system(sayer)
    elif(question == "find the remainder of 2 numbers"):
        print("What is your first number?")
        os.system("say 'what is your first number'")
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        number1 = r.recognize_google(audio)
        print("What is your second number?")
        os.system("say 'what is your second number'")
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        number2 = r.recognize_google(audio)
        ans = float(number1) % float(number2)
        sayer = "say 'the remainder of " + str(number1) + " and " + str(number2) + " is " + str(ans) + "'"
        print("The sum of " + str(number1) + " and " + str(number2) + " is " + str(ans) + " ")
        os.system(sayer)
    elif(question == "tell me a joke"):
        # Create list with jokes
        jokes = ["'I asked my friend to meet me at the gym, but he did not show up. I don't think we are going to work out'",
                 "'What do you call a talking dinosaur?. Thesaurus.'",
                 "'When someone tells me to stop acting like a flamingo, I put my foot down'",
                 "'I taught a wolf to meditate. Now he is Aware Wolf'",
                 "'Two silk worms challenged each other to a race. it ended in a tie'"]
        jokeprint = (random.choice(jokes)) # Choose a random joke
        jokesay = "say " + jokeprint
        print(jokeprint)
        os.system(jokesay)
    elif(question == "search the web"):
        print("What should I search for")
        os.system("say 'what should I search for'")
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        searcher = r.recognize_google(audio)
        print(searcher)
        duck = duckduckgo.get_zci(searcher) # Search for text and save result in variable
        print("Here is what I found:")
        os.system("say 'Here is what I found'")
        print(duck)
    elif(question == "track coronavirus"):
        print("Total confirmed: " + str(covid.get_total_confirmed_cases())) # Get total confirmed cases from JHU CSSE
        print("Deaths: " + str(covid.get_total_deaths())) # Get total deaths from JHU CSSE
        print("Recovered: " + str(covid.get_total_recovered())) # Get total recoveries from JHU CSSE
        print("Data from John Hopkins University")
        print(" ")
        print("Which country should I get data for?")
        os.system("say 'which country should I get data for'")
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        country = r.recognize_google(audio)
        print(country)
        print("Here is what I found:")
        os.system("say 'Here is what I found:'")
        cov = covid.get_status_by_country_name(country) # Search for country and save result in variable
        print(cov)
    else:
        print("I don't know the answer to that")
        os.system("say 'I dont know the answer to that'")
    
