import pygame
from Beonho import Beonho

class Board(object):

    def __init__(self,window):
        self.window = window
        self.side = window[1]-100
        if self.side%9 != 0:
            self.side -= self.side%9
        self.square = self.side//9
        self.x = self.window[0]//2 - self.side//2
        self.y = 50
        #self.beonho = [1,2,3,4,5,6,7,8,9]
        self.beonho = Beonho()
        self.selected = [9,9] #coords of square from 0-8, starts outside so is blank


    def update(self,num):
        #spaghetti code, seems to process index backwards...idk why
        self.beonho[self.selected[1]][self.selected[0]] = num

    def draw_board(self,screen):
        pygame.draw.rect(screen, 0xFFFFFF, [self.x, self.y, self.side, self.side])
        pygame.draw.rect(screen,0x000000,[self.x,self.y,self.side,self.side],4)
        for i in range(1,9):
            #vertical line
            weight = 1
            if i%3==0:
                weight = 3
            pygame.draw.line(screen,0x0000000,[self.x+self.square*i,self.y],
                             [self.x+self.square*i,self.y+self.side],weight)
            #horizontal line
            pygame.draw.line(screen, 0x0000000, [self.x, self.y+self.square*i],
                             [self.x + self.side, self.y + self.square*i], weight)

        #draw highlighted square
        offset = 1
        if 0<=self.selected[0]<9 and 0<=self.selected[1]<9 :
            pygame.draw.rect(screen,0xFFFF00,[(self.selected[0])*self.square+self.x+offset,
                                          (self.selected[1])*self.square+self.y+offset,
                                          self.square-offset,self.square-offset])
        self.draw_rows(screen)

    def draw_rows(self,screen):
        size = self.square-2
        font = pygame.font.SysFont('serif', size)
        for i in range(0,9):
            for j in range(0,9):
                if self.beonho[i][j] != 0:
                    text = font.render(str(self.beonho[i][j]), True, (0x00, 0x00, 0x00))
                    screen.blit(text, [self.x+self.square*j+self.square//3,self.y-2+self.square*i])