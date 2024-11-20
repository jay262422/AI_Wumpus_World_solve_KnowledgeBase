import numpy as np
import random
import os
import pygame
from pygame.locals import *
import time


os.chdir(r'resources')

class make_agent:
    def __init__(self,n):
        self.start = [3,0]
        self.visited = []
        self.currant = self.start
        self.curr_di = 0
        self.move_di = {0:[[0,1],'-> '],
                       1:[[-1,0],'|^ '],
                       2:[[0,-1],'<- '],
                       3:[[1,0],'_| ']}
        self.size = n
        self.im_agent = pygame.image.load(r'player.png').convert_alpha()
        
        
    def move_forward(self):
        if((self.curr_di==0 and self.currant[1]==self.size-1) or (self.curr_di==1 and self.currant[0]==0) or (self.curr_di==2 and self.currant[1]==0) or (self.curr_di==3 and self.currant[0]==self.size-1)):
            pass
        else:
            self.currant = [sum(i) for i in zip(self.currant, self.move_di[self.curr_di][0])]
        
    def turn_90(self,pan):
        if(self.curr_di == 0 and pan == -1):
            pan = 3
        if(self.curr_di == 3 and pan == 1):
            pan = -3
        self.curr_di = self.curr_di+pan
        
    def make_turn(self,dirr):
        #print('enter "right" or "left"')
        #dirr = input()
        if(dirr=='right'):
            self.turn_90(-1)
            self.im_agent = pygame.transform.rotate(self.im_agent,-90)
        if(dirr=='left'):
            self.turn_90(1)
            self.im_agent = pygame.transform.rotate(self.im_agent,90)
            
    


class block():
    
    def __init__(self):
        self.gold = False
        self.pit = False
        self.wumpus = False
        self.breeze = False
        self.stench = False
        self.adj = []
        self.neighbor = []
        self.posi = []


class make_wumpus_world:
    def __init__(self,parent_screen,n):
        
        self.size = n
        self.blocks = [block() for i in range(n**2)]
        random_sample = random.sample(self.blocks[1:],2+int(0.2 * (n**2)))
        self.start = [self.blocks[0]]
        self.gold = [random_sample[0]]
        self.wumpus = [random_sample[1]]
        self.pits = random_sample[2:]
        self.set_grid()
        #self.grid = np.flipud(self.grid)
        self.agent = make_agent(self.size)
        
        self.im_wumpus = pygame.image.load(r'wumpus_image.png').convert_alpha()
        self.im_gold = pygame.image.load(r'gold.png').convert_alpha()
        self.im_pit = pygame.image.load(r'pit.png').convert_alpha()
        self.im_breeze = pygame.image.load(r'breeze.png').convert_alpha()
        self.im_stench = pygame.image.load(r'stench.png').convert_alpha()
        
        self.im_wumpus.set_alpha(150)
        self.im_gold.set_alpha(150)
        self.im_pit.set_alpha(120)
        self.im_breeze.set_alpha(70)
        self.im_stench.set_alpha(70)
        
        self.sizz = 100
        self.parent_screen = parent_screen
   
    def set_grid(self):
        
        self.grid = np.asarray(self.blocks).reshape(self.size,self.size)
        self.grid = np.flipud(self.grid)
        self.get_nie()
        self.gold[0].gold = True
        self.wumpus[0].wumpus = True
        for i in self.wumpus[0].neighbor:
            i.stench = True
        for i in self.pits:
            i.pit = True
            for j in i.neighbor:
                j.breeze = True
        
    def get_nie(self):
        for i in range(self.size):
            for j in range(self.size):
                self.grid[i,j].posi = [i,j]
                if(i!=0):
                    self.grid[i,j].neighbor.append(self.grid[i-1,j])
                if(j!=self.size-1):
                    self.grid[i,j].neighbor.append(self.grid[i,j+1])
                if(i!=self.size-1):
                    self.grid[i,j].neighbor.append(self.grid[i+1,j])
                if(j!=0):
                    self.grid[i,j].neighbor.append(self.grid[i,j-1])
                    
    
    def draw_block(self,block,k,l):
        
        if(self.agent.currant==[k,l]):
            self.parent_screen.blit(self.agent.im_agent,((l+1)*self.sizz,(k+1)*self.sizz))

        if(block.gold==True):
            self.parent_screen.blit(self.im_gold,((l+1)*self.sizz+30,(k+1)*self.sizz))
            
        if(block.pit==True):
            self.parent_screen.blit(self.im_pit,((l+1)*self.sizz,(k+1)*self.sizz))
        if(block.wumpus==True):
            self.parent_screen.blit(self.im_wumpus,((l+1)*self.sizz,(k+1)*self.sizz))
        if(block.breeze==True):
            self.parent_screen.blit(self.im_breeze,((l+1)*self.sizz,(k+1)*self.sizz))
        if(block.stench==True):
            self.parent_screen.blit(self.im_stench,((l+1)*self.sizz,(k+1)*self.sizz))

    
    def draw_grid(self):
        #self.parent_screen.fill((110,110,5))
        for i in range(self.size):
            for j in range(self.size):
                self.draw_block(self.grid[i,j],i,j)
            print()
            
    
    
    def print_block(self,block,k,l):
        string = ''
        
        
        if(self.agent.currant==[k,l]):
            string += ' Agent '
            
            string += self.agent.move_di[self.agent.curr_di][1]
                #string += '-> '

            
        if(block.gold==True):
            string += ' gold '
            
        if(block.pit==True):
            string += ' pit '
        if(block.wumpus==True):
            string += ' wumpus '
        if(block.breeze==True):
            string += ' breeze '
        if(block.stench==True):
            string += ' stench '
        return string
            
            
    def print_grid(self):
        for i in range(self.size):
            for j in range(self.size):
                print(np.char.center(self.print_block(self.grid[i,j],i,j),25),end='')
            print()
            
    
    def shoot_arrow(self):
        temp = self.agent.currant
        while(not((self.agent.curr_di==0 and temp[1]==self.size-1) or (self.agent.curr_di==1 and temp[0]==0) or (self.agent.curr_di==2 and temp[1]==0) or (self.agent.curr_di==3 and temp[0]==self.size-1))):
            temp = [sum(i) for i in zip(temp, self.agent.move_di[self.agent.curr_di][0])]
            if(self.check_wumpus()):
                self.grid[temp[0],temp[1]].wumpus = False
            
            print("Done")
            
    def check_gold(self):
        if(self.grid[self.agent.currant[0],self.agent.currant[1]].gold==True):
            return True
        return False
    
    def check_wumpus(self):
        if(self.grid[self.agent.currant[0],self.agent.currant[1]].wumpus==True):
            return True
        return False
            
    def check_pit(self):
        if(self.grid[self.agent.currant[0],self.agent.currant[1]].pit==True):
            return True
        return False
    
    
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Wupus Game')
        self.surface = pygame.display.set_mode((1000,600))
        pygame.mixer.init()
        self.surface.fill((110,110,5))
        self.wumpus_world = make_wumpus_world(self.surface,4)
        self.wumpus_world.draw_grid()
        self.wumpus_world.print_grid()
        self.text_show()
        pygame.display.flip()
        self.run()
        
    def play(self):
        pygame.display.flip()
        
        if(self.wumpus_world.check_gold()):
            self.game_win()
        
        elif(self.wumpus_world.check_wumpus()):
            self.game_over()
            
        elif(self.wumpus_world.check_pit()):
            self.game_over()
        
        pygame.display.flip()
            
            
    
    def run(self):
        
        running = True
        pause = False
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running =  False
                    if event.key == K_UP:
                        self.wumpus_world.agent.move_forward()
                    if event.key == K_LEFT:
                        self.wumpus_world.agent.make_turn('left')
                    if event.key == K_RIGHT:
                        self.wumpus_world.agent.make_turn('right')
                    if event.key == K_DOWN:
                        print("HIII")
                        self.wumpus_world.shoot_arrow()
                        
                    self.surface.fill((110,110,5))
                    self.wumpus_world.draw_grid()
                    self.wumpus_world.print_grid()
                    self.text_show()

                    
                    #time.sleep(0.3)
                
                elif event.type == QUIT:
                    running = False
            self.play()
            try:
                if not pause:
                    self.play()
            except Exception as e:
                #self.show_game_over()
                pause = True
                #self.reset()
                    
    def text_show(self):
        
        
        font1 = pygame.font.SysFont('arial',45)
        font2 = pygame.font.SysFont('arial',30)
        
        self.im_arrow = pygame.transform.scale(pygame.image.load(r'Arrow.png'),(50,50))
        
        score = font1.render("Wumpus World",True,(255,255,255))
        self.surface.blit(score,(650,100))
        
        
        score = font2.render(" Move Forword ",True,(255,255,255))
        self.surface.blit(score,(650,200))
        self.surface.blit(pygame.transform.rotate(self.im_arrow,180),(850,190))
        
        score = font2.render("   Turn Right ",True,(255,255,255))
        self.surface.blit(score,(650,270))
        self.surface.blit(pygame.transform.rotate(self.im_arrow,-90),(850,260))
        
        score = font2.render("    Turn Left ",True,(255,255,255))
        self.surface.blit(score,(650,340))
        self.surface.blit(pygame.transform.rotate(self.im_arrow,90),(850,330))
        
    def game_win(self):
        font3 = pygame.font.SysFont('arial',50)
        self.surface.fill((110,110,5))
        score = font3.render(" winner ",True,(255,255,255))
        self.surface.blit(score,(400,400))
        
    def game_over(self):
        font3 = pygame.font.SysFont('arial',50)
        self.surface.fill((110,110,5))
        score = font3.render(" Game Over ",True,(255,255,255))
        self.surface.blit(score,(400,400))
        
        
kll = Game()