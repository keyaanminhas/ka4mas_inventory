from twilio.rest import Client



class Dialer :
	def __init__(self):
		self.client = None
		self.call = None
  
	def connect(self) :
		self.client = Client(self.account_sid, self.auth_token)

	def initDial(self, from_, account_sid, auth_token) :
		self.auth_token = auth_token
		self.account_sid = account_sid
		self.from_ =from_
		self.url = "https://twilo-customer-proj.ka4malearner.repl.co/answer"

	def dialNumbers(self, numbers_list):
		self.can_call = True
		for num in numbers_list:
			if not self.can_call :
				break
			self.client.calls.create(to=num, from_=self.from_, url = self.url )