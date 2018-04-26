from libdw import sm
import copy
class VacuumRobot(sm.SM):
	start_state = None
	displacement = {'up':(0,1), 'left':(-1,0), 'right':(1,0),'down':(0,-1)}
	def get_next_values(self, state, inp):
        pass
        
        return next_state, output

	def done(self, state):
		pass
    
v = VacuumRobot()
print('Test 1:')
inp = [False, True, False, False, True, True, False, False]
ans = v.transduce(inp)
print(ans)

print('Test 2:')
v = VacuumRobot()
inp = [False, False, True, False, False, True, False, True, False, False, False, False]
ans = v.transduce(inp)
print(ans)

print('Test 3:')
v = VacuumRobot()
inp = [False, False, False, True, False, False, True, False, False, True, False, False, False,
False,False, False]
ans = v.transduce(inp)
print(ans)

print('Test 4:')
v = VacuumRobot()
v.start()
inp = [False, True, False, False, True, True, False, False]
state = v.state
for i in inp:
	ns, o = v.get_next_values(state, i)
	state = ns
status = v.state == v.start_state
print('State:', v.state)
print('Not Modified:',status)
