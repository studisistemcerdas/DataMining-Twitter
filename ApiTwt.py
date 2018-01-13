from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

ckey = 'wPBMzy98ezjd9QVxfRDl5B3Z3'
csecret = 'nYGws9MB7JQRuCRerunkTqiSd7WvAHQxzeaOy2rgllpQzwmgJ5'
atoken = '946267247583956992-DnAJuifCijevbFQBFhusG1aC0SCCfeD'
asecret = 'K5ZBaY0GhLSfK92uyG9z58QfEjiXRKtUEheVHbDuyfefL'

class listener(StreamListener):
	"""docstring for listener"""
	def on_data(self, data):
		try :
			twitter = data.split(',"text":"')[1].split('","source')[0]
			print twitter
			saveThis = str(time.time())+ '::' + twitter
			saveFile = open('twitDB.csv','a')
			saveFile.write(saveThis)
			saveFile.write('\n')
			saveFile.close()
			return True
		except BaseException, e:
			print 'failed ondata,',str (e)
			time.sleep(5)

	def on_error(self, status):
		print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["jakarta"])