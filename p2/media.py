# -*- coding: utf-8 -*-
# 导入模块
import webbrowser
# 定义类
class Movie():
	"""
	创建电影类，包含电影的基本信息
	Attributes:
		title: 电影的标题名称
		storyline: 电影简介信息
		postor_image: 电影图片海报
		trailer_youtube: 电影播放地址的URL
	Output: 
		title
		storyline
		postor_image
		trailer_youtube
	"""
	def __init__(self, title, storyline, poster_image, trailer_youtube):
		self.title = title
		self.storyline = storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	"""
	打开电影播放地址
	"""
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)