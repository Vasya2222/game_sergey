import pygame


class Game:
    def __init__(self, w=800, h=400, c=(80, 22, 100), fps=50):
        pygame.init()
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
        self.speed = 10
        self.speed2 = 10
        self.horizontal_move_flag = self.vertical_move_flag = 0
        self.horizontal_move_flag2 = self.vertical_move_flag2 = 0
    def draw(self):

        self.screen.fill(self.color)
        self.rect(self.x_rect, self.y_rect)
        self.rect2()
        pygame.display.flip()

    def zikl(self):
        while not self.game_and:
            self.draw()
            self.clock.tick(self.fps)
            self.check_event()
            self.check_event2()
            self.move()
            self.move2()
            self.logek2(self.width, self.heidth)
            self.logek(self.width, self.heidth)

    def __del__(self):
        pygame.quit()

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_and = True
            self.event(event)
    def check_event2(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_and = True
            self.event2(event)

    def rect(self, x_rect, y_rect, color2=(255, 0, 0), width_rect=20, heidth_cert=10):
        pygame.draw.rect(self.screen, color2, (x_rect, y_rect, width_rect, heidth_cert))

    def move(self):
        self.x_rect += self.speed * self.horizontal_move_flag
        self.y_rect += self.speed * self.vertical_move_flag
        self.__horizontal_move_flag = 0
        self.__vertical_move_flag = 0

    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.horizontal_move_flag = -1
            elif event.key == pygame.K_d:
                self.horizontal_move_flag = 1
            elif event.key == pygame.K_w:
                self.vertical_move_flag = -1
            elif event.key == pygame.K_s:
                self.vertical_move_flag = 1
            elif event.key == pygame.K_q:
                self.horizontal_move_flag = self.vertical_move_flag = 0
            elif event.key == pygame.K_f:
                self.game_and = True

    def logek(self, width, heidth, width_rect=20, heidth_rect=10):
        if self.x_rect < 0:
            self.x_rect = 0
        elif self.x_rect > width - width_rect:
            self.x_rect = width - width_rect
        if self.y_rect < 0:
            self.y_rect = 0
        elif self.y_rect > heidth - heidth_rect:
            self.y_rect = heidth - heidth_rect

    def rect2(self, x_rect2=340, y_rect2=200, color3=(255, 0, 0), width_rect2=20, heidth_cert2=10):
        pygame.draw.rect(self.screen, color3, (x_rect2, y_rect2, width_rect2, heidth_cert2))

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
p = Game()
p.zikl()
