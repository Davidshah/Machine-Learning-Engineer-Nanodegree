import random
#import os
from environment import Agent, Environment
from planner import RoutePlanner
from simulator import Simulator

#cdir = os.path.dirname(__file__)
#path = os.path.join(cdir, '..\\report\\QLearning_report.txt')
#if not os.path.exists('file'):
#    open(path, 'w').close()

class QTable(object):
    """
    Table to store Q-learning data Q(s,a).
    Does not scale well with increasing sizes of state/action space
    """
    
    def __init__(self):
        self.Qhat = dict()

    def get(self, state, action):
        key = (state, action)
        return self.Qhat.get(key, None)

    def set(self, state, action, q):
        key = (state, action)
        self.Qhat[key] = q

class LearningAgent(Agent):
    """
    An agent that learns to drive in the smartcab world.
    """

    def __init__(self, env):
        super(LearningAgent, self).__init__(env) # sets self.env = env, state = None, next_waypoint = None, and a default color
        self.color = 'red' # override color
        self.planner = RoutePlanner(self.env, self) # simple route planner to get next_waypoint
        
        # TODO: Initialize any additional variables here
        self.counter = 1.0
        self.Qhat = QTable() # Q(s, a)
        self.alpha = 1 # learning rate starts at 1 and decreases towards 0.
        self.gamma = 0.72 # discount rate of future value
        self.epsilon = 1 # probability of doing a random move
        self.val_actions = Environment.valid_actions
        
#        # write report
#        with open(path, 'a') as file:
#            file.write("\n****alpha {}, gamma: {}, epsilon: {}****\n".format(self.alpha, self.gamma, self.epsilon))
#            file.write("************************************************\n")
        

    def reset(self, destination=None):
        self.planner.route_to(destination)
        # TODO: Prepare for a new trip; reset any variables here, if required
        self.counter += 1 # count steps to set epsilon
        self.alpha = 1 / self.counter # decay alpha
        self.epsilon = 1 / self.counter # decay epsilon

    def update(self, t):
        # Gather inputs
        self.next_waypoint = self.planner.next_waypoint() # from route planner, also displayed by simulator
        inputs = self.env.sense(self)
        inputs = inputs.items()
        #deadline = self.env.get_deadline(self)

        # TODO: Update state
        self.state = (inputs[0], inputs[1], inputs[3], self.next_waypoint)
        
        # TODO: Select action according to your policy
        if random.random() < self.epsilon: # roll to see if random action taken
            action = random.choice(['forward', 'left', 'right'])
        else: 
            q = [self.Qhat.get(self.state, a) for a in self.val_actions]
            max_q = max(q)
            # Decide tie breaker randomly
            if q.count(max_q) > 1:
                # Create list of tied indices and choose randomly
                tied_actions = [i for i in range(len(self.val_actions)) if q[i] == max_q]  
                action_index = random.choice(tied_actions)
            # If no tie, use max q
            else:
                action_index = q.index(max_q)
            action = self.val_actions[action_index]

        # Execute action and get reward
        reward = self.env.act(self, action)
        
#        # Count values for result analysis
#        if (reward < 0):
#            print "Negative reward: inputs = {}, action = {}, reward = {}, waypoint {}".format(inputs, action, reward, self.next_waypoint)
        
        # Gather inputs for next_state after executing action
        next_inputs = self.env.sense(self) 
        next_inputs = next_inputs.items()
        next_state = (next_inputs[0], next_inputs[1], next_inputs[3], self.next_waypoint)

        # TODO: Learn policy based on state, action, reward
        # Q(s,a) <-- Q(s,a) + alpha * (r + gamma * maxQ(s', a') - Q(s,a))

        # Calculate maxQ(s', a')
        next_q = [self.Qhat.get(next_state, a) for a in self.val_actions]
        future_util = max(next_q)         
        if future_util is None:
            future_util = 0.0

        # Get current q from table
        q = self.Qhat.get(self.state, action)
        
        # Update q through value iteration, setting initial q to reward
        if q is None:
            q = reward
        else:
            # Old value + learning rate * (reward + discount * est future value - old value)
            q += self.alpha * (reward + self.gamma * future_util - q)

        self.Qhat.set(self.state, action, q)

        #print "LearningAgent.update(): deadline = {}, inputs = {}, action = {}, reward = {}".format(deadline, inputs, action, reward)  # [debug]


def run():
    """Run the agent for a finite number of trials."""

    # Set up environment and agent
    e = Environment()  # create environment (also adds some dummy traffic)
    a = e.create_agent(LearningAgent)  # create agent
    e.set_primary_agent(a, enforce_deadline=True)  # specify agent to track
    # NOTE: You can set enforce_deadline=False while debugging to allow longer trials

    # Now simulate it
    sim = Simulator(e, update_delay=0.0, display=False)  # create simulator (uses pygame when display=True, if available)
    # NOTE: To speed up simulation, reduce update_delay and/or set display=False

    sim.run(n_trials=100)  # run for a specified number of trials
    # NOTE: To quit midway, press Esc or close pygame window, or hit Ctrl+C on the command-line


if __name__ == '__main__':
    run()
