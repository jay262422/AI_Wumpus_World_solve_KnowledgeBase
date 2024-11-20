import numpy as np

class make_agent():
    
    def __init__(self,n):
        self.start = [n-1,0]
        self.visited = np.zeros((n,n))
        self.currant = self.start
        self.curr_di = 0
        self.move_di = {0:[[0,1],'-> '],
                       1:[[-1,0],'|^ '],
                       2:[[0,-1],'<- '],
                       3:[[1,0],'_| ']}
        self.size = n
        
    def move_forward(self):
        if((self.curr_di==0 and self.currant[1]==self.size-1) or (self.curr_di==1 and self.currant[0]==0) or (self.curr_di==2 and self.currant[1]==0) or (self.curr_di==3 and self.currant[0]==self.size-1)):
            pass
        else:
            self.currant = [sum(i) for i in zip(self.currant, self.move_di[self.curr_di][0])]
        #55#move_forword()
        
        ## car move
        
    def turn_90(self,pan):
        if(self.curr_di == 0 and pan == -1):
            pan = 3
        if(self.curr_di == 3 and pan == 1):
            pan = -3
        self.curr_di = self.curr_di+pan
        
        
        ## move car
        
    def make_turn(self,dirr):
        if(dirr=='right'):
            self.turn_90(-1)
            #55#turn_right()
        if(dirr=='left'):
            self.turn_90(1)
            #55#turn_left()