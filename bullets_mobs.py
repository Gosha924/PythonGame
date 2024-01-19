import pygame


class Bullet_mobs(pygame.sprite.Sprite):
    def __init__(self, screen, person):
        super(Bullet_mobs, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 12, 2)
        self.color = (0, 0, 0)
        self.speed = 11.5
        self.rect.left = person.rect.centerx
        self.rect.centery = person.rect.centery
        self.x_left = float(self.rect.x)
        self.x_right = float(self.rect.x)

    def update(self, shot_right):
        # перемещение пули
        if shot_right == 2:
            self.x_right += self.speed
            self.rect.x = self.x_right
        else:
            self.x_left -= self.speed
            self.rect.x = self.x_left

    def draw_bullet_mob(self):
        # рисуем пулю на экране
        pygame.draw.rect(self.screen, self.color, self.rect)