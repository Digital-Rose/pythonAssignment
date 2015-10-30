import twitter,datetime,time,schedule
import sqlite3
from os import system
creds = []
tweets = []
user = 78169161
timehms = time.strftime("%H:%M:%S")

# Read in and print out the data in the data file
file = open("res/twitcred.txt",'r')
creds = file.readline().strip().split(",")

# Store secret codes
api = twitter.Api(creds[0],creds[1],creds[2],creds[3])
statuses = api.GetUserTimeline(user)
print (statuses[0].text)
saythis = statuses[0].text
system('say ' + saythis)

#Database Code
def getHistory():
	rows = []
	try:
		console = sqlite3.connect("/Users/admin/Library/Application Support/Google/Chrome/Default/History")
		cursor = console.cursor()
		cursor.execute("SELECT title FROM urls ORDER BY ROWID DESC LIMIT 1")
		rows = cursor.fetchall()
	except sqlite3.OperationalError:
		rows.append(["Chrome in use", " "])
	return rows[0]
	
def tweeter():
	row = getHistory()
	if row[0] == "Chrome in use" :
		print " Can not get current page - please quit Google Chrome"
	elif row[0] not in tweets:
		if len(row[0]) != 0:
			tweets.append(row[0])
			print "I'm currently looking at " + row[0]
			response = api.PostUpdate(" I'm currently looking at " + row[0] + " at " + str(timehms))
			system('say "tweet tweet"')
	else:
		print "I've already looked at " + row[0]

schedule.every(10).seconds.do(tweeter)
# uncomment below to tweet every hour
#schedule.every(1).hour.do(tweeter)

while True:
	schedule.run_pending()
console.close()