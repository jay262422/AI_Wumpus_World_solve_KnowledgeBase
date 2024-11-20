from wumpus_world import *

class Game:
    def __init__(self):

        self.wumpus_world = make_wumpus_world(4)
        self.wumpus_world.start_state()
        self.listed_do_p = []
        self.listed_do_w = []
        self.listed_done_p = []
        self.listed_done_w = []
        self.list_done_wumpus = []
        self.listed_w = []
        self.Total_sym = {}
        self.predi_models = [{}]
        self.ok = []
        self.moves = []
        self.back = {"F":"Back",
                    "L":"R",
                    "R":"L"}
        self.wumpus_world.win = False
        self.cont = 0
        self.ch_f = False
        self.priv = [3,0]
        self.track = [[3,0]]
        

    def start(self):
        print(self.wumpus_world.agent.currant)
        #self.wumpus_world.get_array(45)
        self.wumpus_world.rule_add()
        self.evu()
        #print("ok its",self.ok)
        self.temp_move()
        while 1:
            #sleep(2)
            self.run()
            if (self.wumpus_world.win==True):
                break
            
        
        #self.run()
    def adder(self,count,st):
        for i in range(count):
            st = st + 1
            if(st==4):
                st = 0
        #print("ST",st)
        return st
    
    def ender(self):
        while 1:
            tempmp = self.wumpus_world.agent.currant
            self.wumpus_world.print_grid()
            if len(self.track)!=0:
                if self.priv != self.wumpus_world.agent.currant:
                    self.ch_f = True
                if self.ch_f == True:
                    self.kokko = self.track.pop()
                    print("go to back : ",self.kokko)
                    print(self.planner(self.kokko))
                    move = self.move_car(self.planner(self.kokko))
                    self.ch_f = False
                else:
                    print("go to back : ",self.kokko)
                    print(self.planner(self.kokko))
                    move = self.move_car(self.planner(self.kokko))
            else:
                break
            self.wumpus_world.print_grid()
            self.priv = tempmp
        while self.wumpus_world.agent.currant != [3,0]:
            move = self.move_car(self.planner([3,0]))
            self.wumpus_world.print_grid()
                
    
    def ender_old(self):
        while 1:
            if len(self.moves) != 0:
                ko = self.moves.pop()
                #print(self.moves)
                print("go to: ",self.back[ko])
                if self.back[ko] == "Back":
                    self.move_car('L')
                    self.move_car('L')
                    self.move_car("F")
                else:
                    self.move_car(self.back[ko])
            self.wumpus_world.print_grid()
            if self.wumpus_world.agent.currant == [3,0]:
                break
            
    def planner(self,dest):
        for i in range(4):
            #print("co coc oc")
            #print(dest)
            #print(self.wumpus_world.agent.currant)
            #print([self.wumpus_world.agent.currant[0] + self.wumpus_world.agent.move_di[i][0][0],self.wumpus_world.agent.currant[1] + self.wumpus_world.agent.move_di[i][0][1]])
            #print()
            #print(self.wumpus_world.agent.currant + self.wumpus_world.agent.move_di[i][0])
            if [self.wumpus_world.agent.currant[0] + self.wumpus_world.agent.move_di[i][0][0],self.wumpus_world.agent.currant[1] + self.wumpus_world.agent.move_di[i][0][1]] == dest:
                print(i)
                self.wumpus_world.agent.curr_di
                if i==self.wumpus_world.agent.curr_di:
                    #print('F')
                    #self.ch_f = True
                    return 'F'
                elif i == self.adder(1,self.wumpus_world.agent.curr_di):
                    return 'L'
                #print(self.adder(3,self.wumpus_world.agent.curr_di))
                elif i == self.adder(3,self.wumpus_world.agent.curr_di):
                    return 'R'
                #print("halo",self.adder(3,self.wumpus_world.agent.curr_di))
                #print(i)
        return 'R'
                
    def back_word(self):
        ko = self.moves.pop()
        if ko == "F":
            if (self.ch_f == True):
                self.move_car('L')
                self.move_car('L')
                self.move_car('F')
                self.moves.append('L')
                self.moves.append('L')
                self.moves.append('F')
                self.ch_f = False
                print("go to: Back")
            else:
                self.move_car('F')
                self.moves.append('F')
                print("go to F")
        elif ko == "L":
            self.move_car('R')
            self.moves.append('L')
            print("go to R")
        elif ko == "R":
            self.move_car('L')
            print("go to R")
            
    def back_word_2(self):
        pass
        
            
    def add_bol(self):
        #print("come in function")
        #print("previs:",self.priv)
        #print("curr:",self.wumpus_world.agent.currant)
        if (self.priv != self.wumpus_world.agent.currant):
           # print("first")
            if self.wumpus_world.agent.currant in self.track:
                jojj = len(self.track)
                for ind in range(len(self.track)):
                    if self.track[ind]==self.wumpus_world.agent.currant:
                        jojj = ind
                self.track = self.track[:jojj+1]
            #    print("second")
                
            else:
                self.track.append(self.wumpus_world.agent.currant)
             #   print("third")
            #print("chuu chale")
        print("track:",self.track)
            
        
    def temp_move(self):
        for pos in self.wumpus_world.grid[self.wumpus_world.agent.currant[0]][self.wumpus_world.agent.currant[1]].neighbor:
            #print(pos.posi)
            #print(pos.visited)
            #print(pos.ok)
            #print("pos",pos.posi)
            if (pos.ok == True and pos.visited == False):
                self.ch_f = True
                print("go to: ",pos.posi)
                #print(self.planner(pos.posi))
                self.add_bol()
                move = self.move_car(self.planner(pos.posi))
                
                
                self.moves.append(move)
                return pos.posi
        if len(self.moves) != 0:
            if self.priv != self.wumpus_world.agent.currant:
                self.ch_f = True
            if self.ch_f == True:
                self.kokko = self.track.pop()
                print("go to back : ",self.kokko)
                #print(self.planner(self.kokko))
                move = self.move_car(self.planner(self.kokko))
                self.ch_f = False
            else:
                print("go to back : ",self.kokko)
                #print(self.planner(self.kokko))
                move = self.move_car(self.planner(self.kokko))
                
                
            #self.back_word_2()
            """
            ko = self.moves.pop()
            #print(self.moves)
            print("go to: ",self.back[ko])
            if self.back[ko] == "Back":
                self.move_car('L')
                self.move_car('L')
                self.move_car("F")
            else:
                self.move_car(self.back[ko])
            """
            return 0
        print("it end")
        self.cont += 1
        if self.cont ==1:
            for ko in self.wumpus_world.grid:
                print(ko)
                ko.visited == False
            self.wumpus_world.win = True
            
        
    def move_car(self,move=None):
        
        #if move == None:
            #move = input("Move car with F L R: ")
        
        if(move=='F'):
            self.wumpus_world.agent.move_forward()
        elif(move=='L'):
            self.wumpus_world.agent.make_turn('left')
        elif(move=='R'):
            self.wumpus_world.agent.make_turn('right')
        return move
            
    def evu(self):
        
        for nigh in self.wumpus_world.rule_neighbor[self.wumpus_world.agent.currant[0]][self.wumpus_world.agent.currant[1]]:
            if ((nigh not in self.listed_do_p) and (nigh not in self.listed_done_p)):
                self.listed_do_p.append(nigh)
                #print(self.listed_do_p)
                
            if ((nigh not in self.listed_do_w) and (nigh not in self.listed_done_w)):
                self.listed_do_w.append(nigh)
                #print(self.listed_do_w)
            
        
        #temp_2,KB_cu = model_check(self.wumpus_world.kb)    
        self.predi_models, self.Total_sym = model_check(self.wumpus_world.kb,self.Total_sym,self.predi_models)
        KB_cu = self.predi_models.copy()
        temp = self.listed_do_p.copy()        
        for nigh in temp:                       #print(self.wumpus_world.di) #if model_check(self.wumpus_world.kb, eval(f'self.wumpus_world.di[f"P{nigh}"]'))==True:
            
            if check_res(KB_cu,'P'+nigh,True):  
                print(f"pit at {nigh}")
                #print()
                self.wumpus_world.kb.add(eval(self.wumpus_world.join_sym("",[f"self.wumpus_world.di['P{nigh}']"])))
                self.listed_do_p.remove(nigh)
                self.listed_done_p.append(nigh)
                self.wumpus_world.grid[int(nigh[0]),int(nigh[1])].pit=True

                
            #elif model_check(self.wumpus_world.kb, eval(f'Not(self.wumpus_world.di[f"P{nigh}"])'))==True:
            elif check_res(KB_cu,'P'+nigh,False):    
                print(f"No pit at {nigh}")
                #print(eval(self.wumpus_world.join_sym("Not",[f"self.wumpus_world.di[P{nigh}]"])))
                self.wumpus_world.kb.add(eval(self.wumpus_world.join_sym("Not",[f"self.wumpus_world.di['P{nigh}']"])))
                #print(self.wumpus_world.kb)
                self.listed_do_p.remove(nigh)
                self.listed_done_p.append(nigh)
                self.wumpus_world.grid[int(nigh[0]),int(nigh[1])].pit=False
                if ((nigh in self.listed_done_w) and (self.wumpus_world.grid[int(nigh[0]),int(nigh[1])].wumpus==False)):
                    self.wumpus_world.grid[int(nigh[0]),int(nigh[1])].ok=True
                    self.ok.append(nigh)
           
        temp = self.listed_do_w.copy() 
        for nigh in temp:
                
            if check_res(KB_cu,'W'+nigh,True):  
                print(f"wumpus at {nigh}")
                #print()
                
                self.wumpus_world.kb.add(eval(self.wumpus_world.join_sym("",[f"self.wumpus_world.di['W{nigh}']"])))
                self.listed_do_w.remove(nigh)
                self.listed_done_w.append(nigh)
                self.wumpus_world.grid[int(nigh[0]),int(nigh[1])].wumpus=True

            #elif model_check(self.wumpus_world.kb, eval(f'Not(self.wumpus_world.di[f"P{nigh}"])'))==True:
            elif check_res(KB_cu,'W'+nigh,False):    
                print(f"No wumpus at {nigh}")
                #print(eval(self.wumpus_world.join_sym("Not",[f"self.wumpus_world.di[P{nigh}]"])))
                self.wumpus_world.kb.add(eval(self.wumpus_world.join_sym("Not",[f"self.wumpus_world.di['W{nigh}']"])))
                #print(self.wumpus_world.kb)
                self.listed_do_w.remove(nigh)
                self.listed_done_w.append(nigh)
                self.wumpus_world.grid[int(nigh[0]),int(nigh[1])].wumpus=False
                if ((nigh in self.listed_done_p) and (self.wumpus_world.grid[int(nigh[0]),int(nigh[1])].pit==False)):
                    self.wumpus_world.grid[int(nigh[0]),int(nigh[1])].ok=True
                    self.ok.append(nigh)
                    
        
    def run(self):
        print(self.track)
        #print([self.wumpus_world.agent.currant[0],self.wumpus_world.agent.currant[1]])
        
        print("come")
        print(self.wumpus_world.agent.currant)
        if(self.wumpus_world.agent.visited[self.wumpus_world.agent.currant[0],self.wumpus_world.agent.currant[1]]==0):
            self.wumpus_world.grid[self.wumpus_world.agent.currant[0],self.wumpus_world.agent.currant[1]].visited = 1
            #print("ki")
            if (self.wumpus_world.get_array()==[1,0,0,0,0]):
                self.ender()
                self.wumpus_world.win=True
                return 0
            self.wumpus_world.rule_add()
            self.evu()
            print("ok its",self.ok)
            temp = self.wumpus_world.agent.currant.copy()
            self.temp_move()
            self.priv = temp
            
            
        else:
            print("ok its",self.ok)
            temp = self.wumpus_world.agent.currant.copy()
            #print("previous:",self.wumpus_world.agent.currant)
            self.temp_move()
            self.priv = temp
            #print("gone to ",self.wumpus_world.agent.currant)
            #self.wumpus_world.print_grid()
        self.wumpus_world.print_grid()