import pygame
from Game import Game

def main():

    #intialize variable for main program loop
    done = False
    #create instance of game class
    illa_game = Game()

    #main program loop
    while not done:
        done = illa_game.process_events()
        illa_game.run_logic()
        illa_game.display_frame()

    #quit the program if we reach here as we are doneski
    pygame.quit()

if __name__ == "__main__":
    main()