class TroverButtonSolver:
    '''
        Applies the numbered button function
    '''
    def apply_function(self, state, index):
        if(index == 0): 
            return state ^ 0b110110010
        if(index == 1): 
            return state ^ 0b111010101
        if(index == 2): 
            return state ^ 0b101100100
        if(index == 3): 
            return state ^ 0b111100000
        if(index == 4): 
            return state ^ 0b000111000
        if(index == 5): 
            return state ^ 0b001001001
        if(index == 6): 
            return state ^ 0b001010100
        if(index == 7): 
            return state ^ 0b010010010
        if(index == 8): 
            return state ^ 0b111111111
    
    def print_state(self, state):
        print(format(state, '09b'))
        
    '''
        Call to map out all possible states for given starting state
    '''
    def find_all_states(self, state):
        #Start with an empty list of solutions
        self.all_solutions = [False] * 512
        self.find_all_states_helper(state, 0) #Start trying with the first function
        return self.all_solutions
        
    '''
        See find_all_states(). Don't call directly.
    '''
    def find_all_states_helper(self, state, function):
        if(function == 9): #After we have applied all functions, we are done.
            return
        
        #Mark current location as reachable
        self.all_solutions[state] = True
        
        #Apply the function
        result = self.apply_function(state, function) 
        self.all_solutions[result] = True
        
        #Try the next function with both possible options for the current function
        self.find_all_states_helper(state, function+1) #Option 1: function not applied
        self.find_all_states_helper(result, function+1) #Option 1: function applied
        
    '''
        Call to map out all possible states for given starting state
    '''
    def find_solution(self, state, goal):
        #Start with an empty list of solutions
        self.solution_buttons = []
        if(self.find_solution_helper(state, goal, 0)): #Start trying with the first function
            return self.solution_buttons
        else:
            return None #No solution found
    
    '''
        See find_solution(). Don't call directly.
    '''
    def find_solution_helper(self, state, goal, function):
        #If we reached the goal
        if(state == goal):
            return True
        
        if(function == 9): #After we have applied all functions, we are done.
            return False #No solution down this branch
    
        #Apply the function
        result = self.apply_function(state, function) 
        
        #Try the next function with both possible options for the current function
        if(self.find_solution_helper(state, goal, function+1)): #If we reached a solution without applying the function
            return True
        if(self.find_solution_helper(result, goal, function+1)): #If we reached a solution by applying the function
            self.solution_buttons.append(function)
            return True
        return False #If it reaches here, it failed to find any solutions

#Runs when file is run directly 
if __name__ == "__main__":
        
    #initial state from the game
    #initial_state = 0b011010001 
            
    #Example inside the solution space
    initial_state = 0b110101101
    
    state = 0b111111111
    solver = TroverButtonSolver()
    solutions = solver.find_all_states(state)
    
    if(solutions[initial_state]):
        print("Yay, it worked! To solve it, press these buttons:")
        solution = solver.find_solution(state, initial_state)
        print(solution)
    else:
        print("That value doesn't exist in the solution space")
    


