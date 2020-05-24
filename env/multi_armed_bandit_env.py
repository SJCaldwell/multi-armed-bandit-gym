import random
import gym
from gym import Env, logger, spaces
import numpy as np

class MultiArmedBanditEnv(Env):

    def __init__(self, n):
        """
        number of arms
        """
        self.action_space = spaces.Discrete(n)
    
    def step(self, action):
        raise NotImplementedError()

    def reset(self):
        # do the stuff you did in init, but again
        raise NotImplementedError

    def render(self, mode='human'):
        raise NotImplementedError