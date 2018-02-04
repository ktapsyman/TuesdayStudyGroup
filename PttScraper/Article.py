class Article(object):
	def __init__(self, Title="", Meta=None, Push=0, Mark = '', ContentUrl = ""):
		self.Title = Title
		self.Meta = Meta
		self.Content = ""
		self.Push = Push
		if self.Push == '爆':
			self.Push=100
		self.ContentUrl = ContentUrl
		self.TitleVec = None #TODO
		self.Mark = ''
	
	def SetContent(self, Content):
		self.Content = Content
		return self
	
	def SetMeta(self, Meta):
		self.Meta = Meta
		return self
