import pygame

#custom event
Timer = pygame.USEREVENT + 1

#button class
class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False
		self.is_visible = False

	def draw(self, surface, can_click):
		if not self.is_visible:
			return False
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos) and can_click:
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				pygame.time.set_timer(Timer, 500, 1)
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action 
