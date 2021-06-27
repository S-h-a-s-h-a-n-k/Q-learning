# -*- coding: utf-8 -*-
import gym
import numpy as np  
# Create an environment of Taxi-v3:
env = gym.make('Taxi-v3').env 
env.render()
print(env.s)
print(env.observation_space)

state = env.reset()
epochs = 0
penalty, reward = 0, 0 
frames = [{'frame': env.render(mode='ansi' ),'state':state,'action': 'Nil','reward':'Nil'}]
done = False 
while not done :
    action=env.action_space.sample()
    state,reward,done,_=env.step(action)
    if action<=3 : 
      if state==frames[epochs]['state'] :
        penalty+=1
    frames.append({'frame': env.render(mode='ansi' ), 'state': state, 'action': action, 'reward': reward})
    epochs += 1
print("Timesteps taken: {}".format(epochs))
print("Penalties incurred: {}".format(penalty))

from IPython.display import clear_output
from time import sleep
def print_frames(frames):
    for i, frame in enumerate(frames):
        clear_output(wait = True)
        print(frame['frame'])
        print(f"Timestep: {i+1}")
        print(f"State: {frame['state']}")
        print(f"Action: {frame['action']}")
        print(f"Reward: {frame['reward']}")
        sleep(0.1)
print_frames(frames)
