
       
from libdw import sm

# TASK: implement the class SMExtra

class SMExtra(sm.SM):
    pass
    
# The following state machine classes are provided to
#    test SMExtra. You do not need to modify these.
#    The test cases are at the end of this file.

class TorchLight(SMExtra):
    start_state = 0
    
    valid_inputs = ['push']
    
    def get_next_values(self, state, inp):        
        if state == 0:
            next_state = 1
            output = 'on'
        elif state == 1:
            next_state = 0
            output = 'off'
            
        return next_state, output
    
class UpAndDown(SMExtra):
    start_state = 0
    
    valid_inputs = ['up', 'down']
    
    def get_next_values(self, state, inp):
        assert(inp == 'up' or inp == 'down')
        assert(0 <= state)
        
        if inp == 'up':
            next_state = state + 1
            output = next_state
        elif inp == 'down':
            next_state = state - 1
            output = next_state
            
        return next_state, output
    
class CokeMachine(SMExtra):
    start_state = 0
    
    valid_inputs = [5, 10, 20, 50, 100]

    def get_next_values(self,state, inp):
        if state == 0 and inp == 100:
            next_state = 0
            output=(0,'coke',0)
        elif state == 0 and inp == 50:
            next_state = 1
            output=(50,'--',0)
        elif state == 1 and inp ==100:
            next_state = 0
            output = (0, 'coke', 50)
        elif state == 1 and inp==50:
            next_state = 0
            output = (0,'coke',0)
        else:
            next_state = state
            if state == 1:
                balance = 50
            else:
                balance = 0
            output = (balance,'--',inp)
        return next_state,output
    

# TEST CASES

# these are the test cases from the question paper
# please uncomment them to run and check the outputs
#    against those in the paper
    
#s = TorchLight()
#print('TorchLight:')
#print(s.get_input_for_output([]))
#print(s.get_input_for_output(['off']))
#print(s.get_input_for_output(['on']))
#print(s.get_input_for_output(['on', 'off'] * 4))
        
#print()

#s = TorchLight()
#print('TorchLight:')
#s.start()
#s.get_input_for_output(['on','off','on'])
#print(s.state == s.start_state)

#print()

#s = UpAndDown()
#print('UpAndDown:')
#print(s.get_input_for_output([]))
#print(s.get_input_for_output([1,2,3,4,5,6,7,8,9,10]))
#print(s.get_input_for_output([1,2,3,2,1,0,1,2,3,4,5]))
#print(s.get_input_for_output([1,2,3,2,1,0,1,0]))
        
#print()

#s = CokeMachine()
#print('CokeMachine:')
#print(s.get_input_for_output([]))
#print(s.get_input_for_output([(0,'coke',0)]))
#print(s.get_input_for_output([(0,'--',20)]))
#print(s.get_input_for_output([(0,'coke',0), (0,'coke',0), (0,'coke',0), (0,'coke',0), (0,'coke',0)]))
#print(s.get_input_for_output([(50,'--',0), (0,'coke',50)] * 4))
#print(s.get_input_for_output([(50,'--',0), (50,'--',10), (0,'coke',0)]))






