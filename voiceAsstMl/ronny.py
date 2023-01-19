import random
import json
import torch


from brain import NeuralNet
from NeuralNetwork import bag_of_words,tokenize
from task import NonInputFn
from task import InputFn
from speak import Spk
import datetime



device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open('intents.json','r') as json_data:
    intents = json.load(json_data)

FILE = "TrainData.pth"
data = torch.load(FILE)

input_size = data['input_size']
hidden_size = data['hidden_size']
output_size = data['output_size']
all_words = data['all_words']
tags = data['tags']
model_state = data['model_state']

model = NeuralNet(input_size,hidden_size,output_size).to(device)
model.load_state_dict(model_state)
model.eval()

#--------------code for ronny----------
Name = "ronny"
from  listen import takeCommand

sum_has_run = False
def wishme():
    global sum_has_run
    if sum_has_run:
        return
    sum_has_run = True
    ...
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        Spk.say("good morning sir...\n")
    elif hour>=12 and hour<18:
        Spk.say("good afternoon sir...\n")
    else:
        Spk.say("good evening sir...\n")
    ...

    Spk.say("I am ronny, please tell me how may I help you....\n")

def Main():
        wishme()
        sentence = ""
        Spk.say("ask something sir!\n")
        while len(sentence)==0 and sentence=="":
            #Spk.say("ask something sir\n")
            sentence = takeCommand()

        #print("just after take command : "+sentence2)
        sentence2 = sentence
        sentence2 = tokenize(sentence2)
        X = bag_of_words(sentence2,all_words)
        X = X.reshape(1,X.shape[0])
        X = torch.from_numpy(X).to(device)

        output = model(X)
        _, predicted = torch.max(output,dim=1)

        tag = tags[predicted.item()]
        probs = torch.softmax(output,dim=1)
        prob = probs[0][predicted.item()]
        sentence2 = " ".join(sentence2)
        #print("after tockenize"+sentence2)
        if prob.item() > 0.75:
            for intent in intents['intents']:
                if tag==intent["tags"]:
                    reply = random.choice(intent["responses"])

                    if "time" in reply:
                        NonInputFn(reply)

                    elif "date" in reply:
                        NonInputFn(reply)

                    elif "day" in reply:
                        NonInputFn(reply)

                    elif "wikipedia" in reply:
                        Spk.say("please wait sir. searching on wikipedia....\n")
                        InputFn(reply,sentence2)

                    elif "google" in reply:
                        Spk.say("please wait sir. searching on google...\n")
                        InputFn(reply,sentence2)

                    elif "youtube" in reply:
                        Spk.say("ok sir wait, I am opening youtube.....\n")
                        InputFn(reply,sentence2)

                    elif "screenshot" in reply:
                        Spk.say("wait sir. I am taking screenshot...\n")
                        NonInputFn(reply)

                    elif "open app" in reply:
                        Spk.say("wait sir. I am opening app....\n")
                        InputFn(reply,sentence2)

                    elif "music" in reply:
                        Spk.say("wait sir. I am playing music........\n")
                        NonInputFn(reply)

                    elif "whatsapp" in reply:
                        Spk.say("wait sir. I am sending massage.....\n")
                        NonInputFn(reply)

                    elif "classroom" in reply:
                        Spk.say("please wait sir, I am opening classroom.....\n")
                        NonInputFn(reply)

                    elif "gmail" in reply:
                        Spk.say("please wait sir, I am opening your gmail....\n")
                        NonInputFn(reply)

                    elif "make food" in reply:
                        Spk.say("I can't do that sir. , but I can show you how to make...\n")
                        reply2= "youtube"+reply
                        InputFn(reply,sentence2)

                    elif "play on youtube" in reply:
                        Spk.say("wait sir, I am playing song on youtube.......")
                        NonInputFn(reply)

                    elif "bye" in reply:
                        Spk.say(reply)
                        exit()

                    else:
                        Spk.say(reply)

    #return sentence