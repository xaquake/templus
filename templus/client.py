from random import choice, choices
from string import ascii_lowercase
from requests import get

from .objects import *


DOMAINS = [
	"mailto.plus",
	"fexpost.com",
	"fexbox.org",
	"mailbox.in.ua",
	"rover.info",
	"inpwa.com",
	"intopwa.com",
	"tofeat.com",
	"chitthi.in"]

class Client:
	
	def __init__(self, mail: str = None):
		self._mail = mail
		self.api = "https://tempmail.plus/api/mails"
		self.headers = {
			"Host": "tempmail.plus",
			"Content-Type": "application/json; charset=utf-8"
		}
	
	def __check_is_valid(self, mail):
		if self._mail is None and mail is None:
			raise Exception("Mail not found")
		return mail.split("@") if mail is not None else self._mail.split("@")
	
	def get_messages(self, mail: str = None) -> Messages:
		logdata = Client(self._mail).__check_is_valid(mail)
		req = get("%s/?email=%s%%40%s&first_id=0&epin=" % (self.api, logdata[0], logdata[1]), headers=self.headers)
		return Messages(req.json()).update
	
	def read_message(self, id: int, mail: str = None) -> Message:
		logdata = Client(self._mail).__check_is_valid(mail)
		req = get("%s/%s?email=%s%%40%s&epin=" % (self.api, id, logdata[0], logdata[1]), headers=self.headers)
		return Message(req.json())
	
	@staticmethod
	def generate_mails(count: int = 1) -> [str, tuple] :
		generated = tuple("".join(choices(ascii_lowercase, k=5)) + "@%s" % choice(DOMAINS) for x in range(count))
		return generated[0] if count == 1 else generated
