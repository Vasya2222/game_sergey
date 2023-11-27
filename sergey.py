import pygame


class Game:
    def __init__(self, w=800, h=400, c=(80, 22, 100), fps=50):
        pygame.init()
        # self.count = 0
        self.width = w
        self.heidth = h
        self.color = c
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.heidth))
        self.game_and = False
        self.x_rect = self.width // 2
        self.y_rect = self.heidth // 2

        self.x_rect2 = 340
        self.y_rect2 = 200

        self.x_rect3 = 40
        self.y_rect3 = 100

        self.width_rect = 20
        self.heidth_cert = 10
        self.color2 = (255, 0, 0)
        self.rect = pygame.Rect

        self.width_rect2 = 20
        self.heidth_cert2 = 10
        self.color3 = (0, 0, 255)
        self.rect2 = pygame.Rect

        self.width_rect3 = 10
        self.heidth_cert3 = 20
        self.color4 = (0, 255, 0)
        self.rect3 = pygame.Rect

        self.speed = 10

        self.speed2 = 10

        self.speed3 = 10

        self.horizontal_move_flag = self.vertical_move_flag = 0
        self.horizontal_move_flag2 = self.vertical_move_flag2 = 0
        self.horizontal_move_flag3 = 0

    def func_rect(self):
        self.rect = pygame.draw.rect(self.screen, self.color2,
                                     (self.x_rect, self.y_rect, self.width_rect2, self.heidth_cert2))

    def func_rect2(self):
        self.rect2 = pygame.draw.rect(self.screen, self.color3,
                                      (self.x_rect2, self.y_rect2, self.width_rect2, self.heidth_cert2))

    def func_rect3(self):
        self.rect3 = pygame.draw.rect(self.screen, self.color4,
                                      (self.x_rect3, self.y_rect3, self.heidth_cert3, self.width_rect3))

    def draw(self):

        self.screen.fill(self.color)
        self.func_rect()
        self.func_rect2()
        self.func_rect3()
        pygame.display.flip()

    def zikl(self):
        while not self.game_and:
            self.clock.tick(self.fps)
            self.check_event()
            self.move()
            self.move2()
            self.move3()
            self.logek3(self.width, self.heidth)
            self.logek2(self.width, self.heidth)
            self.logek(self.width, self.heidth)
            self.draw()
            self.collision(self.rect, self.rect2)
            self.collision2(self.rect, self.rect2, self.rect3)

    def __del__(self):
        pygame.quit()

    def check_event(self):
        for event in pygame.event.get():
            if event == pygame.QUIT:
                self.game_and = True
            self.event(event)
            self.event2(event)

    # def rect(self, x_rect, y_rect, color2=(255, 0, 0), width_rect=20, heidth_cert=10):
    #     self.my_rect = pygame.draw.rect(self.screen, color2, (x_rect, y_rect, width_rect, heidth_cert))

    def move(self):
        self.x_rect += self.speed * self.horizontal_move_flag
        self.y_rect += self.speed * self.vertical_move_flag
        self.horizontal_move_flag = 0
        self.vertical_move_flag = 0

    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.horizontal_move_flag = -1
            elif event.key == pygame.K_RIGHT:
                self.horizontal_move_flag = 1
            elif event.key == pygame.K_UP:
                self.vertical_move_flag = -1
            elif event.key == pygame.K_DOWN:
                self.vertical_move_flag = 1
            elif event.key == pygame.K_SPACE:
                self.horizontal_move_flag = self.vertical_move_flag = 0
            elif event.key == pygame.K_f:
                self.game_and = True

    def logek(self, width, heidth, width_rect=20, heidth_rect=10, ):
        if self.x_rect < 0:
            self.x_rect = 0
        elif self.x_rect > width - width_rect:
            self.x_rect = width - width_rect
        if self.y_rect < 0:
            self.y_rect = 0
        elif self.y_rect > heidth - heidth_rect:
            self.y_rect = heidth - heidth_rect

    # def rect2(self, x_rect2=340, y_rect2=200, color3=(255, 0, 0), width_rect2=20, heidth_cert2=10):
    #     pygame.draw.rect(self.screen, color3, (x_rect2, y_rect2, width_rect2, heidth_cert2))

    def move2(self):
        self.x_rect2 += self.speed2 * self.horizontal_move_flag2
        self.y_rect2 += self.speed2 * self.vertical_move_flag2
        self.horizontal_move_flag2 = 0
        self.vertical_move_flag2 = 0

    def event2(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_j:
                self.horizontal_move_flag2 = -1
            elif event.key == pygame.K_l:
                self.horizontal_move_flag2 = 1
            elif event.key == pygame.K_i:
                self.vertical_move_flag2 = -1
            elif event.key == pygame.K_k:
                self.vertical_move_flag2 = 1
            elif event.key == pygame.K_q:
                self.horizontal_move_flag2 = self.vertical_move_flag2 = 0
            elif event.key == pygame.K_f:
                self.game_and = True

    def logek2(self, width, heidth, width_rect2=20, heidth_rect2=10):
        if self.x_rect2 < 0:
            self.x_rect2 = 0
        elif self.x_rect2 > width - width_rect2:
            self.x_rect2 = width - width_rect2
        if self.y_rect2 < 0:
            self.y_rect2 = 0
        elif self.y_rect2 > heidth - heidth_rect2:
            self.y_rect2 = heidth - heidth_rect2

    def collision(self, rect, rect2):
        if rect.colliderect(rect2):
            self.game_and = True

    def move3(self):
        self.x_rect3 += self.speed3 * self.horizontal_move_flag3

    def logek3(self, width, heidth, width_rect3=20, heidth_rect3=10):
        if self.x_rect3 <= width:
            self.horizontal_move_flag3 = 1
        elif self.x_rect3 > width - width_rect3:
            self.horizontal_move_flag3 = -1
        # if self.x_rect3 < width:
        #     self.horizontal_move_flag3 = 1
        # elif self.x_rect3 > width - width_rect3:
        #     self.horizontal_move_flag3 = -1
        # if self.y_rect3 < 0:
        #     self.y_rect3 = 0
        # elif self.y_rect3 > heidth - heidth_rect3:
        #     self.y_rect3 = heidth - heidth_rect3

    def collision2(self, rect, rect2, rect3):
        if rect2.colliderect(rect3) or rect.colliderect(rect3):
            self.game_and = True


p = Game()
p.zikl()
