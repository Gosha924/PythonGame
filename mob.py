import pygame
import random, math


class Mob(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Mob, self).__init__()
        self.image = pygame.image.load('image/person_left.png')
        self.screen = screen
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)
        self.speed = 150 / 60
        self.life = True

    def update_qwerty(self):
        n = random.randint(0, 3)
        if n == 0:
            if self.rect.left > 0:
                self.center_x -= self.speed
        elif n == 1:
            if self.rect.right < self.screen_rect.right:
                self.center_x += self.speed
        elif n == 2:
            if self.rect.top > 0:
                self.center_y -= self.speed
        else:
            if self.rect.bottom < self.screen_rect.bottom:
                self.center_y += self.speed
        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y

    def draw_mob(self):
        self.screen.blit(self.image, self.rect)

    def update(self, person_pos):
        player_x = person_pos[0]
        player_y = person_pos[1]
        if abs(self.rect.centerx - player_x) > 5 or abs(self.rect.centery - player_y) > 5:
            dx = player_x - self.center_x
            dy = player_y - self.center_y
            distance = math.sqrt(dx ** 2 + dy ** 2)
            dx = dx / distance
            dy = dy / distance
            self.center_x += dx * self.speed
            self.center_y += dy * self.speed
            self.rect.centerx = self.center_x
            self.rect.centery = self.center_y


