#w4rm15h
#50 Projects
#15. Magic 8 Ball Game
import random
import os

#Responses
responses = [
	"Don't count on it.",
	"My reply is no.",
	"My sources say no.",
	"Outlook not so good.",
	"Very doubtful.",
	"Reply hazy, try again.",
	"Ask again later.",
	"Better not tell you now.",
	"Cannot predict now.",
	"Concentrate and ask again.",
	"As I see it, yes.",
	"Most likely.",
	"Outlook good.",
	"Yes.",
	"Signs point to yes.",
	"It is certain.",
	"It is decidedly so.",
	"Without a doubt.",
	"Yes definitely.",
	"You may rely on it.",
]

def choosingAnswer():
	os.system("clear")
	print("Ask me a question...")
	print("Shake the magic 8 ball")
	con = input("Press enter to shake...")
	randomValue = random.choice(responses)
	print(randomValue)

choosingAnswer()