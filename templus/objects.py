from dataclasses import dataclass


@dataclass
class Messages:
	
	def __init__(self, data):
		self.json = data
		self.id = []
		self.is_new = []
		self.from_mail = []
		self.from_name = []
		self.title = []
		self.date = []
	
	@property
	def update(self):
		for x in self.json["mail_list"]:
			self.id.append(x["mail_id"])
			self.from_mail.append(x["from_mail"])
			self.from_name.append(x["from_name"])
			self.is_new.append(x["is_new"])
			self.title.append(x["subject"])
			self.date.append(x["time"])
		return self

	
@dataclass
class Message:
	
	def __init__(self, data):
		self.json = data
		self.id = data["mail_id"]
		self.from_mail = data["from_mail"]
		self.from_name = data["from_name"]
		self.title = data["subject"]
		self.text = data["text"]
		self.attachments = data["attachments"]
		self.date = data["date"]
