import random
import gym
from gym import Env, logger, spaces
import numpy as np

np.random.seed(0)

class MultiArmedBanditEnv(Env):

    def __init__(self, n=3, info={}):
        """
        n - number of arms in the bandit
        """
        self.num_bandits = n
        self.action_space = spaces.Discrete(self.num_bandits)
        self.observation_space = spaces.Discrete(1) # just the reward of the last action
        self.bandit_success_prob = np.random.uniform(size=self.num_bandits) # Pick some random success probabilities
        self.info = info

    
    def step(self, action):
        reward = 0
        done = True
        result_prob = np.random.random()
        if result_prob < self.bandit_success_prob[action]:
            reward = 1
        else:
            reward = 0
        return [0], reward, done, self.info

    def reset(self):
        # Get some new bandit success probs
        self.bandit_success_prob = np.random.uniform(size=self.num_bandits) # Pick some random success probabilities

    def render(self, mode='human'):
        print('bandits success prob:')
        for i in range(self.num_bandits):
            print("arm {num} reward prob: {prob}".format(num=i, prob=self.bandit_success_prob[i]))
