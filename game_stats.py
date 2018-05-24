import json

class GameStats():
	'''跟踪游戏统计信息'''

	def __init__(self, ai_settings):
		'''初始化统计信息'''
		self.ai_settings = ai_settings
		self.reset_stats()
		#游戏刚启动时处于活动状态
		self.game_active = False

		#在任何情况下都不应该重置最高得分，所以放在这里而不是reset_stats中
		self.high_score = self.get_record()

	def reset_stats(self):
		'''初始化在游戏运行期间可能变化的统计信息'''
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
		self.level = 1

	def get_record(self):
		'''从文件读取最高纪录'''
		filename = 'record.json'
		try:
			with open(filename) as record_obj:
				record = json.load(record_obj)
		except FileNotFoundError:
			return 0
		else:
			return record
		
		