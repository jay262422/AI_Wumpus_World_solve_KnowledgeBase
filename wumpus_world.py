from logic import *
from agent import *
import random

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
        self.visited = False
        self.ok = False
        self.children = []
        self.parent= None
        
    def add_child(self,child):
        child.parent = self
        self.children.append(child)
        
        
class make_wumpus_world:
    def __init__(self,n):
        
        self.size = n
        self.blocks = [block() for i in range(n**2)]
        random_sample = random.sample(self.blocks[1:],2+int(0.2 * (n**2)))
        self.start = [self.blocks[0]]
        #self.gold = [random_sample[0]]
        #self.wumpus = [random_sample[1]]
        #self.pits = random_sample[2:]
        self.set_grid()
        #self.grid = np.flipud(self.grid)
        self.agent = make_agent(self.size)
        self.kb = And()
        self.dic = {True:'',False:'Not'}
        self.win = False
   
    def set_grid(self):
        
        self.grid = np.asarray(self.blocks).reshape(self.size,self.size)
        self.grid = np.flipud(self.grid)
        self.get_nie()
        #self.gold[0].gold = True
        #self.wumpus[0].wumpus = True
        #for i in self.wumpus[0].neighbor:
            #i.stench = True
        #for i in self.pits:
            #i.pit = True
            #for j in i.neighbor:
                #j.breeze = True
                
    def start_state(self):
        self.di = {}
        lists = ['P','B','G','W','S']
        for i in range(self.size):
            for j in range(self.size):
                for k in lists:
                    self.di[f'{k}{i}{j}'] = Symbol(f'{k}{i}{j}')
        
        
    def get_nie(self):
        self.rule_neighbor = [[[] for i in range(self.size)] for j in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                self.grid[i,j].posi = [i,j]
                if(i!=0):
                    self.grid[i,j].neighbor.append(self.grid[i-1,j])
                    self.rule_neighbor[i][j].append(f'{i-1}{j}')
                if(j!=self.size-1):
                    self.grid[i,j].neighbor.append(self.grid[i,j+1])
                    self.rule_neighbor[i][j].append(f'{i}{j+1}')
                if(i!=self.size-1):
                    self.grid[i,j].neighbor.append(self.grid[i+1,j])
                    self.rule_neighbor[i][j].append(f'{i+1}{j}')
                if(j!=0):
                    self.grid[i,j].neighbor.append(self.grid[i,j-1])
                    self.rule_neighbor[i][j].append(f'{i}{j-1}')

    def join_sym(self,smb,terms,extra='',extra2=''):
        temp = f'{smb}('
        for i in terms:
            temp = temp +f' {extra}{i}{extra2},'
        temp = temp[:-1] + ')'
        return temp
                    
    def rule_add(self):
        i = self.agent.currant[0]
        j = self.agent.currant[1]
        self.kb.add(eval(self.join_sym("Biconditional",[f"self.di['B{i}{j}']",self.join_sym('Or',self.rule_neighbor[i][j],"self.di['P","']")])))
        self.kb.add(eval(self.join_sym("Biconditional",[f"self.di['S{i}{j}']",self.join_sym('Or',self.rule_neighbor[i][j],"self.di['W","']")])))
        for ii in range(self.size):
            for jj in range(self.size):
                if self.agent.visited[ii,jj]==1:
                    self.kb.add(eval(self.join_sym("Or",[self.join_sym('Not',[f"self.di['G{i}{j}']"]),self.join_sym('Not',[f"self.di['G{ii}{jj}']"])])))
                    self.kb.add(eval(self.join_sym("Or",[self.join_sym('Not',[f"self.di['W{i}{j}']"]),self.join_sym('Not',[f"self.di['W{ii}{jj}']"])])))
        
        
        #print(self.join_sym(self.dic[self.grid[self.agent.currant[0],self.agent.currant[1]].gold],[f"self.di['G{ii}{jj}']"]))
        self.kb.add(eval(self.join_sym(self.dic[self.grid[self.agent.currant[0],self.agent.currant[1]].gold],[f"self.di['G{i}{j}']"])))
        #self.kb.add(eval(self.join_sym(self.dic[self.grid[self.agent.currant[0],self.agent.currant[1]].pit],[f"self.di['P{i}{j}']"])))
        #self.kb.add(eval(self.join_sym(self.dic[self.grid[self.agent.currant[0],self.agent.currant[1]].wumpus],[f"self.di['W{i}{j}']"])))
        self.kb.add(eval(self.join_sym(self.dic[self.grid[self.agent.currant[0],self.agent.currant[1]].breeze],[f"self.di['B{i}{j}']"])))
        self.kb.add(eval(self.join_sym(self.dic[self.grid[self.agent.currant[0],self.agent.currant[1]].stench],[f"self.di['S{i}{j}']"])))
        #print(self.kb)
        self.agent.visited[i,j]=1
                    
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
    
    
    def get_array(self,pre=None):
        if pre != None:
            return [0,0,0,0]
        """write code hear"""
        #col = Detect_color()
        col = input()
        if(col=='yellow'):
            self.grid[self.agent.currant[0],self.agent.currant[1]].gold = True
            return [1,0,0,0,0]
        elif(col=='green'):
            self.grid[self.agent.currant[0],self.agent.currant[1]].breeze = True
            return [0,0,0,1,0]
        elif(col=='pink'):
            self.grid[self.agent.currant[0],self.agent.currant[1]].stench = True
            return [0,0,0,0,1]
        elif(col=="black"):
            return [0,0,0,0,0]
    
    def print_block(self,block,k,l):
        
        #if ()
        
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