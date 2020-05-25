import random
import gym
from gym import Env, logger, spaces
import numpy as np

np.random.seed(0)

class MultiArmedBanditEnv(Env):

    def __init__(self, n=3):
        """
        n - number of arms in the bandit
        """
        self.num_bandits = n
        self.action_space = spaces.Discrete(self.num_bandits)
        self.observation_space = spaces.Discrete(1) # just the reward of the last action
        self.bandit_success_prob = np.random.uniform(size=self.num_bandits) # Pick some random success probabilities
        self.bandits_reward = [1 for x in range(self.num_bandits)] # For this formulation of the bandit problem, all rewards are 1

    
    def step(self, action):
        result_prob = np.random.random()
        if result_prob < self.bandit_success_prob[action]:
            return 1
        else:
            return 0

    def reset(self):
        # Get some new bandit success probs
        self.bandit_success_prob = np.random.uniform(size=self.num_bandits) # Pick some random success probabilities

    def render(self, mode='human'):
        print('bandits success prob:')
        for i in range(len(self.num_bandits)):
            print("arm {num} reward prob: {prob}".format(num=i, prob=self.bandit_success_prob[i]))
