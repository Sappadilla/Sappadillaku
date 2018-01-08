import pygame
from Board import Board

class Game(object):
    #constructor
    def __init__(self):
        #more states than just start and game over.
        #need a state variable to make it work better
        #much more modular this way I think
        #self.start = False
        #states: opening, selection, in_game, game_over
        pygame.init()
        self.state = "opening"
        self.window = [700,500]
        self.screen = pygame.display.set_mode(self.window)
        pygame.display.set_caption("Sappadillaku")
        self.clock = pygame.time.Clock()
        #self.board = Board(self.window)

    #method processing input
    def process_events(self):
        #event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            #big if sets for the current state of the game
            elif self.state == "opening":
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    self.state = "selection"

            elif self.state == "selection":
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if self.b_but[0] <= pos[0] <= self.b_but[0]+self.btext.get_width()and \
                                            self.b_but[1] <= pos[1] <= self.b_but[1]+30:
                        self.state = "in_game"
                        self.board = Board(self.window)

            elif self.state == "in_game":
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if self.board.x <= pos[0] <= self.board.x+self.board.side and \
                        self.board.y <= pos[1] <= self.board.y+self.board.side:

                        x = (pos[0]-self.board.x)//self.board.square
                        y = (pos[1]-self.board.y)//self.board.square
                        self.board.selected = [x,y]
                    else: self.board.selected = [10,10]

                elif event.type == pygame.KEYDOWN:

                    #arrow keys, moves selected within the board
                    if event.key == pygame.K_UP and self.board.selected[1]>0:
                        self.board.selected = [self.board.selected[0],self.board.selected[1]-1]
                    elif event.key == pygame.K_DOWN and self.board.selected[1] < 8:
                        self.board.selected = [self.board.selected[0], self.board.selected[1] + 1]
                    elif event.key == pygame.K_LEFT and self.board.selected[0] > 0:
                        self.board.selected = [self.board.selected[0] - 1, self.board.selected[1]]
                    elif event.key == pygame.K_RIGHT and self.board.selected[0] < 8:
                        self.board.selected = [self.board.selected[0] + 1, self.board.selected[1]]

                    #numbers, should change beonhodo
                    elif  pygame.K_9 >= event.key >= pygame.K_0:
                        self.board.update(event.key-48)


            elif self.state == "game_over":
                pass
        return False


    #method for main game logic
    def run_logic(self):
        self.clock.tick(60)

    #method for updating display
    def display_frame(self):

        if self.state == "opening":
            #make a welcome screen
            self.screen.fill(0xCCCC99)
            fsize = 40
            font = pygame.font.SysFont("serif",fsize,True)
            font2 = pygame.font.SysFont("serif",fsize,False,True)
            text = font.render("WELCOME TO SAPPADILLAKU", True, (0xFF,0xFF,0xFF))
            text2 = font2.render("Press any key to begin",True,(0xFF,0xFF,0xFF))
            center_x = (self.window[0] // 2) - (text.get_width() // 2)
            center_y = (self.window[1] // 2) - (text.get_height() // 2)
            center_x2 = (self.window[0] // 2) - (text2.get_width() // 2)
            self.screen.blit(text, [center_x, center_y-fsize//2])
            self.screen.blit(text2,[center_x2,center_y+fsize//2])


        elif self.state == "selection":
            #selection screen
            #choose difficulty to start game
            self.screen.fill(0xCCCC99)
            t_size = 70
            title_font = pygame.font.SysFont('serif',t_size,True)
            title_text = title_font.render("Sappadillaku",True,[0x00,0x66,0x00])
            self.screen.blit(title_text,[self.window[0]//2 - title_text.get_width()//2,t_size-10])

            fsize = 30
            font = pygame.font.SysFont("serif",fsize,True)
            text = font.render("Select Difficulty, Holmes",True,(0x00,0x00,0x00))
            center_x = self.window[0]//2 - text.get_width()//2
            self.screen.blit(text,[center_x,200])

            #draw buttons
            #beginner button
            bsize = 30
            bfont = pygame.font.SysFont('serif',bsize)
            self.btext = bfont.render("Beginner",True,(0x00,0x00,0x00))
            self.b_but = [100,300]
            pygame.draw.rect(self.screen,0xCCCCCC,[self.b_but[0],self.b_but[1],self.btext.get_width()+10,bsize+5])
            pygame.draw.rect(self.screen, 0x000000, [self.b_but[0], self.b_but[1], self.btext.get_width() + 10, bsize + 5],3)
            self.screen.blit(self.btext,[self.b_but[0]+5,self.b_but[1]])

            #intermediate button
            itext = bfont.render("Intermediate", True, (0x00, 0x00, 0x00))
            i_but = [self.window[0]//2-itext.get_width()//2, 300]
            pygame.draw.rect(self.screen, 0xCCCCCC, [i_but[0], i_but[1], itext.get_width() + 10, bsize + 5])
            pygame.draw.rect(self.screen, 0x000000, [i_but[0], i_but[1], itext.get_width() + 10, bsize + 5], 3)
            self.screen.blit(itext, [i_but[0] + 5, i_but[1]])

            #advanced button
            atext = bfont.render("Advanced", True, (0x00, 0x00, 0x00))
            a_but = [self.window[0]-(atext.get_width()+100), 300]
            pygame.draw.rect(self.screen, 0xCCCCCC, [a_but[0], a_but[1], atext.get_width() + 10, bsize + 5])
            pygame.draw.rect(self.screen, 0x000000, [a_but[0], a_but[1], atext.get_width() + 10, bsize + 5], 3)
            self.screen.blit(atext, [a_but[0] + 5, a_but[1]])

        elif self.state == "in_game":
            #draw the board and rows
            self.screen.fill(0xCCCC99)
            self.board.draw_board(self.screen)

        elif self.state == "game_over":
            #game over screen
            self.screen.fill(0x000000)

        pygame.display.flip()