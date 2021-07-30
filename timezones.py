from datetime import datetime, timezone
from zoneinfo import ZoneInfo

now_Portland = datetime.now(ZoneInfo('America/Los_Angeles'))
hour_Portland = now_Portland.hour
if hour_Portland > 9 and hour_Portland < 17:
    open_Portland = "open"
else:
    open_Portland = "closed"
try:
	time_Portland = now_Portland.strftime('%#I:%M %p')
except:
	try:
		time_Portland = now_Portland.strftime('%-I:%M %p')
	except:
		time_Portland = now_Portland.strftime('%I:%M %p')

now_NYC = datetime.now(ZoneInfo('America/New_York'))
hour_NYC = now_NYC.hour
if hour_NYC > 9 and hour_NYC < 17:
    open_NYC = "open"
else:
    open_NYC = "closed"
try:
	time_NYC = now_NYC.strftime('%#I:%M %p')
except:
	try:
		time_NYC = now_NYC.strftime('%-I:%M %p')
	except:
		time_NYC = now_NYC.strftime('%I:%M %p')

now_London = datetime.now(ZoneInfo('Europe/London'))
hour_London = now_London.hour
if hour_London > 9 and hour_London < 17:
    open_London = "open"
else:
    open_London = "closed"
try:
	time_London = now_London.strftime('%#I:%M %p')
except:
	try:
		time_London = now_London.strftime('%-I:%M %p')
	except:
		time_London = now_London.strftime('%I:%M %p')

print("The time in Portland is {} and the branch there is {}.".format(time_Portland, open_Portland))
print("The time in New York is {} and the branch there is {}.".format(time_NYC, open_NYC))
print("The time in London is {} and the branch there is {}.".format(time_London, open_London))