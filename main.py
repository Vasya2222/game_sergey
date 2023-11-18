# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.

import pygame


# Игрок
class Player:
    def __init__(self, screen_width, screen_height):
        # Размеры
        # Игрок занимает 1/14 по ширине и 1/10 по высоте игрового экрана
        # Игровой спрайт
        self.__sprite = pygame.transform.smoothscale(
            pygame.image.load("sprites/shish.png").convert_alpha(),
            (screen_width // 14, screen_height // 10)
        )
        self.__rect = self.__sprite.get_rect()
        # Положение
        self.__rect.x = screen_width // 2 - self.__rect.width // 2
        self.__rect.y = screen_height // 2 - self.__rect.height // 2
        # Движение
        self.__horizontal_move_flag = self.__vertical_move_flag = 0
        self.__speed = 10

    def check_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.__horizontal_move_flag = -1
            elif event.key == pygame.K_d:
                self.__horizontal_move_flag = 1
            elif event.key == pygame.K_w:
                self.__vertical_move_flag = -1
            elif event.key == pygame.K_s:
                self.__vertical_move_flag = 1

    def check_logic(self, screen_width, screen_height):
        if self.__rect.x < 0:
            self.__rect.x = 0
        elif self.__rect.x > screen_width - self.__rect.width:
            self.__rect.x = screen_width - self.__rect.width
        if self.__rect.y < 0:
            self.__rect.y = 0
        elif self.__rect.y > screen_height - self.__rect.height:
            self.__rect.y = screen_height - self.__rect.height

    def check_collision(self, enemy):
        return self.__rect.colliderect(enemy.rect)

    def move(self):
        self.__rect.x += self.__speed * self.__horizontal_move_flag
        self.__rect.y += self.__speed * self.__vertical_move_flag
        self.__horizontal_move_flag = 0
        self.__vertical_move_flag = 0

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.__rect)
        screen.blit(self.__sprite, self.__rect)


class Enemy:
    def __init__(self, x, y, screen_width, screen_height):
        # Размеры
        # Враг занимает 1/14 по ширине и 1/10 по высоте игрового экрана
        # Игровой спрайт
        self.__sprite = pygame.transform.smoothscale(
            pygame.image.load("sprites/badshish.png").convert_alpha(),
            (screen_width // 14, screen_height // 10)
        )
        self.rect = self.__sprite.get_rect()
        # Положение
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
        screen.blit(self.__sprite, self.rect)


class Game:
    def __init__(self, width=800, height=600, fps=60):
        pygame.init()

        self.__width = width
        self.__height = height
        self.__screen = pygame.display.set_mode((self.__width, self.__height))
        self.__bg_sprite = pygame.transform.smoothscale(
            pygame.image.load("sprites/bg.jpg").convert(),
            (self.__width, self.__height)
        )
        self.__fps = fps
        self.__clock = pygame.time.Clock()
        self.__game_end = False

        self.__player = Player(self.__width, self.__height)
        self.__enemy = Enemy(150, 150, self.__width, self.__height)

    def __del__(self):
        pygame.quit()

    def run(self):
        while not self.__game_end:
            self.__check_events()
            self.__check_logic()
            self.__move_objects()
            self.__draw()

            self.__clock.tick(self.__fps)

    def __check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__game_end = True

            self.__player.check_event(event)

    def __check_logic(self):
        self.__player.check_logic(self.__width, self.__height)

        if self.__player.check_collision(self.__enemy):
            print("Вы столкнулись с Плохишишем!")
            self.__game_end = True

    def __move_objects(self):
        self.__player.move()

    def __draw(self):
        self.__screen.blit(self.__bg_sprite, (0, 0))
        self.__player.draw(self.__screen)
        self.__enemy.draw(self.__screen)
        pygame.display.flip()


def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    main()