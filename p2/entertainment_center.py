# -*- coding: utf-8 -*-
# 导入模块
import fresh_tomatoes
from media import Movie
# 定义数据
cat_at_home = Movie('猫咪后院之家', 
					'年纪轻轻获得新人奖，一举成为人气作家的小说家‧佐久本胜（伊藤淳史 饰），现在'
					'却陷入了低潮期。', 
					'https://img1.doubanio.com/view/photo/l/public/p2501119529.jpg', 
					'http://player.youku.com/embed/XMzAzMzUxOTk2OA==')
# print(cat_at_home.poster_image_url)

women_sleeping = Movie('女人沉睡时',
						'位于某海滨的高级酒店，迎来了小有名气作家清水健二（西岛秀俊 饰）和他的妻子'
						'（小山田小百合 饰）。清水凭借处女作享誉文坛，然而第二部作品反响平平，而今'
						'更陷入创作瓶颈。',
						'https://img1.doubanio.com/view/photo/l/public/p2315659149.jpg',
						'http://player.youku.com/embed/XMjUwNzUxNjAzNg==')
firebug = Movie('夏美的萤火虫',
					'影片由森泽明夫同名小说改编：立志成为摄影师的夏美，来到曾与父亲欣赏过萤火虫的森林'
					'寻找萤火虫，在这里夏美结识了经营杂货铺的安奶奶和地藏爷爷。',
					'https://img3.doubanio.com/view/photo/l/public/p2325221431.jpg',
					'http://player.youku.com/embed/XMjgwMTExMzQ5Mg==')
hot_girl = Movie('垫底辣妹',
					'长相甜美的高中女孩工藤沙耶加（有村架纯 饰）在家并不受父亲待见，父亲一心要把弟弟'
					'培养成棒球手，而疏于对女儿们的呵护。',
					'https://img3.doubanio.com/view/photo/l/public/p2327477482.jpg',
					'http://player.youku.com/embed/XMTY2MDUwNzU4MA==')
fish_story = Movie('鱼的故事',
					'四个时间段，四段不同年龄段的人不同的生活片段，四个看似独立的故事，可冥冥之中却'
					'被串联起来，成了改变世界的最强音。',
					'https://img1.doubanio.com/view/photo/l/public/p739307699.jpg',
					'http://player.youku.com/embed/XNjI2OTczNDIw')
good_boy = Movie('你是好孩子',
					'冈野匡（高良健吾 饰）立志成为一名传道授业解惑的教师，在完成了相关学习之后，他进入'
					'了樱丘小学，开始了他的执教生涯。',
					'https://img3.doubanio.com/view/photo/l/public/p2238156625.jpg',
					'http://player.youku.com/embed/XMjY5MDA3MTIxNg==')
# print(cat_at_home.storyline)
# cat_at_home.show_trailer()
# 数据存入list
movies = [cat_at_home, women_sleeping, firebug, hot_girl, fish_story, good_boy]
# 执行打开电影网站
fresh_tomatoes.open_movies_page(movies)
