#import sys 退出游戏用，这里不用导入

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
#from alien import Alien
import game_functions as gf


def run_game():
	#初始化pygame、设置和屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height)) #游戏窗口尺寸，宽1200像素，高800像素
	pygame.display.set_caption("Alien Invasion")

	#创建一艘飞船、一个子弹编组和一个外星人编组
	ship = Ship(ai_settings, screen)
	#创建一个用于存储子弹的编组
	bullets = Group()
	aliens = Group()

	#创建外星人群
	gf.create_fleet(ai_settings, screen,ship, aliens)


	#设置背景颜色
	#用类的属性就不用这个
	#bg_color = (230,230,230)

	'''#创建一个外星人
	alien = Alien(ai_settings, screen) 不再使用'''


	#开始游戏的主循环
	while True:

		#监视键盘和鼠标事件
		gf.check_events(ai_settings, screen, ship, bullets)
		#更新飞船位置
		ship.update()
		#更新子弹
		gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
		#更新外星人
		gf.update_aliens(ai_settings, aliens)
		#更新屏幕
		gf.update_screen(ai_settings, screen, ship, aliens,bullets)
		
run_game()