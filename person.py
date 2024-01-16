import pygame


class Person(pygame.sprite.Sprite):
    def __init__(self, screen, image):
        super().__init__()
        self.screen = screen
        self.image = image
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)
        self.life = True

    def update_skin(self, new_image):
        self.image = new_image

    def output_person(self):
        # рисование персонажа
        self.screen.blit(self.image, self.rect)

    def update_person(self):
        # обновление позиции персонажа
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center_x += 5.5
        if self.move_left and self.rect.left > 0:
            self.center_x -= 5.5
        if self.move_up and self.rect.top > 0:
            self.center_y -= 5.5
        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.center_y += 5.5
        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y

    def person_barrier_right(self):
        self.center_x += 5.5
        self.center_y += 5.5
        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y

    def person_barrier_left(self):
        self.center_x -= 5.5
        self.center_y += 5.5
        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y





