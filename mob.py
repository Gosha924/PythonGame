import pygame
import time, random
from bullets_mobs import Bullet_mobs
from pygame.sprite import Group


class Mob(pygame.sprite.Sprite):
    def __init__(self, screen, shot):
        super(Mob, self).__init__()
        self.image = pygame.image.load('image/person_left.png')
        self.screen = screen
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.shot = shot
        if self.shot == 1:
            self.rect.centerx = 1100
            self.rect.bottom = 100
        else:
            self.rect.centerx = 100
            self.rect.bottom = 700
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)
        self.speed = 150 / 60
        self.life = True
        self.go_left = False
        self.go_middle_left = False
        self.go_straite = False
        self.go_right = False
        self.go_middle_right = False
        self.go_straite_right = False


        # Время последнего выстрела моба
        self.last_shoot_time = time.time()
        self.bullets_mobs = Group()

    def draw_mob(self):
        self.screen.blit(self.image, self.rect)

    def update(self, person_pos, person):
        lens = [i for i in range(350, 451, 35)]
        lens2 = [i for i in range(1000, 840, -50)]
        player_y = person_pos[1]
        if self.shot == 1:
            if not self.go_left:
                self.rect.centerx += self.speed
                if self.rect.centerx >= 1165:
                    self.go_left = True
            elif not self.go_middle_left and self.go_left:
                self.rect.centery += self.speed
                if self.rect.y >= random.choice(lens):
                    self.go_middle_left = True
            elif not self.go_straite and self.go_left and self.go_middle_left:
                self.rect.centerx -= self.speed
                if self.rect.x <= random.choice(lens2):
                    self.go_straite = True
            if abs(self.rect.centery - player_y) > 1 and self.go_straite:
                if self.rect.centery > player_y:
                    self.rect.centery -= self.speed
                else:
                    self.rect.centery += self.speed
            if time.time() - self.last_shoot_time > 0.8:
                    # Выполнить выстрел
                new_bullet = Bullet_mobs(self.screen, self)
                self.bullets_mobs.add(new_bullet)
                self.last_shoot_time = time.time()
        else:
            if not self.go_right:
                self.rect.centerx -= self.speed
                if self.rect.centerx < 35:
                    self.go_right = True
            elif not self.go_middle_right and self.go_right:
                self.rect.centery -= self.speed
                if self.rect.y <= 400:
                    self.go_middle_right = True
            elif not self.go_straite_right and self.go_right and self.go_middle_right:
                self.rect.centerx += self.speed
                if self.rect.x >= 350:
                    self.go_straite_right = True
            if abs(self.rect.centery - player_y) > 1 and self.go_straite_right:
                if self.rect.centery > player_y:
                    self.rect.centery -= self.speed
                else:
                    self.rect.centery += self.speed
            # Логика для стрельбы моба раз в секунду
            if time.time() - self.last_shoot_time > 1:
                # Выполнить выстрел
                new_bullet = Bullet_mobs(self.screen, self)
                self.bullets_mobs.add(new_bullet)
                self.last_shoot_time = time.time()


    def update_bullets_mobs(self):
        self.bullets_mobs.update(self.shot)
        for bullet in self.bullets_mobs.copy():
            if bullet.rect.right >= self.screen.get_rect().right or bullet.rect.left <= 0:
                self.bullets_mobs.remove(bullet)







