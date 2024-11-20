class Symbol():
    
    def __init__(self,name):
        self.name = name
        
    def evaluate(self, model):
        return bool(model[self.name])
    
    def symbols(self):
        return {self.name}
    
class Not():
    
    def __init__(self,operand):
        self.operand = operand
        
    def evaluate(self, model):
        return not(self.operand.evaluate(model))
    
    def symbols(self):
        return self.operand.symbols()
        
class And():
    
    def __init__(self, *conjuncts):
        self.conjuncts = list(conjuncts)
        
    def evaluate(self, model):
        return all(conjunct.evaluate(model) for conjunct in self.conjuncts)
    
    def symbols(self):
        return set.union(*[conjunct.symbols() for conjunct in self.conjuncts])
    
    def add(self, conjunct):
        self.conjuncts.append(conjunct)


class Or():
    
    def __init__(self, *disjuncts):
        self.disjuncts = list(disjuncts)
        
    def evaluate(self, model):
        return any(disjunct.evaluate(model) for disjunct in self.disjuncts)
    
    def symbols(self):
        return set.union(*[disjunct.symbols() for disjunct in self.disjuncts])
        
        
class Implication():
    
    def __init__(self, left, right):
        self.left = left
        self.right = right
        
    def evaluate(self, model):
        return ((not self.left.evaluate(model)) or (self.right.evaluate(model)))
    
    def symbols(self):
        return set.union(self.left.symbols(), self.right.symbols())
        
class Biconditional():
    
    def __init__(self, left,right):
        self.left = left
        self.right = right
        
    def evaluate(self, model):
        return ((self.left.evaluate(model) and self.right.evaluate(model)) or 
                (not (self.left.evaluate(model)) and not(self.right.evaluate(model))))
    
    def symbols(self):
        return set.union(self.left.symbols(), self.right.symbols())
    
def model_check(knowledge,pre_symbols=set(),model=[dict()]):#, query,model=dict()
    KBB = []
    ALL_model = []
    def check_all(knowledge, symbols, model): #query,
        if not symbols:
            if knowledge.evaluate(model):
                #KB
                KBB.append(model)
                #print("ll")
                #print(model)
                #return query.evaluate(model)
                return True
                
            #else:
                #print("lol lol:",model)
            return True
        else:
            remaining = symbols.copy()
            p = remaining.pop()
            model_true = model.copy()
            model_true[p] = True
            model_false = model.copy()
            model_false[p] = False

            # Ensure entailment holds in both models
            #return (check_all(knowledge, query, remaining, model_true) and
                    #check_all(knowledge, query, remaining, model_false)
                
            return (check_all(knowledge, remaining, model_true) and
                    check_all(knowledge, remaining, model_false))

    # Get all symbols in both knowledge and query
    #symbols = set.union(knowledge.symbols(), query.symbols())
    #
    #print(symbols)
    s_symbols = knowledge.symbols()
    symbols = s_symbols.difference(pre_symbols)
    # Check that knowledge entails query
    #return check_all(knowledge, query, symbols, model)
    #return check_all(knowledge, symbols, model),KBB
    for mini_mod in model:
        #print(mini_mod)
        check_all(knowledge, symbols, mini_mod)
        ALL_model.append(KBB)
        KBB = []
    for i in ALL_model:
        for j in i:
            KBB.append(j)
            
    return KBB,s_symbols

def check_res(KB_models,query,check):
    for ji in KB_models:
        if(ji[query]!=check):
            return False
    return True