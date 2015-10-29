# Meg's Python Chess Chatbot! 

#imports
import random
import webbrowser
lostPage = "http://www.chess.com/article/view/5-reasons-losing-a-chess-game-is-good"
practisePage="https://www.chess.com/register"
import wikipedia
import subprocess
import time
from os import system

#lists&arrays
welcome = ['Hi!','Hello!','Hey!', 'Alright my loverrrrr!']
yesAnswers = ['yes','yep','yeh','ye','yeah','Yes','Yep','Yeh','Ye',"yes i am","Yes I am"]
noAnswers = ['no','nope','nah','nein','No','Nope','Nah',"No im not","no i am not","No, I'm not"]
winAnswers = ['won',"I won","i won","I won my game",'win','amazing','great']
drawAnswers = ['draw',"I drew","i drew","I drew my game","i drew my game",'drew','ok']
lostAnswers = ['lost',"i lost", "I lost","I lost my game",'lose','awful']
random_welcome = random.choice(welcome)

def chessQuestion(nameOfChessQuestion):
	storeStopWords=removeStopwords(nameOfChessQuestion)
	wikipedia.search(storeStopWords)
	return wikipedia.summary(storeStopWords, sentences=5)
	
def removeStopwords(str):
	from stop_words import get_stop_words
	stop_words = get_stop_words('english')
	words = str.split(" ")
	withoutStopwords = ""
	for word in words:
		if(not word in stop_words):
			withoutStopwords = withoutStopwords + word + " "
	return withoutStopwords

while True:
	rw = random_welcome
	print(rw + " What's your name?")
	system('say ' + rw + "What is your name?")
	name = raw_input(">>> ")
	name = name.replace(" name "," ")
	name = name.replace(" called "," ")
	name = name.replace(" I'm"," ")
	name = name.replace("im "," ")
	name = name.replace("My "," ")
	name = removeStopwords(name)
	saythis = name + ", ask me about a chess player"
	system('say ' + saythis)
	print("Chatbot: " + name + ",ask me about a chess player...")
	chessAnswer = raw_input(name + ":")
	foo = chessQuestion(chessAnswer) 
	print foo
	time.sleep(5)
	system('say "Are you playing in a tournament at the moment?"')
	print("Chatbot: Are you playing in a tournament at the moment?")
	tourneyAnswer = raw_input(name + ":")
	if((tourneyAnswer in yesAnswers)):
		system('say "How did you do in your game?"')
		print("Chatbot: How did you do in your game?")
		gameAnswer = raw_input(name + ":")
		if ((gameAnswer in lostAnswers)):
			system('say "Did you learn anything from it?"')
			print("Chatbot: Did you learn anything from it?")
			lostReply = raw_input(name + ":")
			if((lostReply in noAnswers)):
				system('say "Maybe look at this page"')
				print("Chatbot: Maybe look at this page:")
				time.sleep(3)
				webbrowser.open(lostPage)
				print("Chatbot: Also you should study Magnus Carlsen")
				system('say "Also you should study Magnus Carlsen. He is the best chess player in the world!"')
				wikipedia.search("Magnus Carlsen")
				print wikipedia.summary("Magnus Carlsen", sentences=3)
				print("Chatbot: Perhaps you should go through the game with a coach? You learn more from when you lose then when you win. Stay strong and good luck.")
			elif((lostReply in yesAnswers)):
				system('say "That is the main thing. Well done."')
				print("Chatbot: That's the main thing. Well done.")
		elif ((gameAnswer in drawAnswers)):
			system('say "Was it a good game?"')
			print("Chatbot: Was it a good game?")
			drawReply = raw_input(name + ":")
			if((drawReply in noAnswers)):
				system('say "Maybe look at this page"')
				print("Chatbot: Maybe look at this page")
				webbrowser.open(lostPage)
		elif ((gameAnswer in winAnswers)):
			system('say "Wooooo , Well Done"')
			print("Chatbot: Woooo!")
	elif ((tourneyAnswer in noAnswers)):
		system('say "I think you should practise. Why not register on chess.com and play."')
		print("Chatbot: I think you should practise. Why not register on chess.com and play.")
		time.sleep(5)
		webbrowser.open(practisePage)
	system('say "Have a nice day"')

while False:
	print("Have a nice day")
	system('say "Have a nice day"')	
