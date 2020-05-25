# multi-armed-bandit-gym
Dummy RL environment for a blog post explaining how to roll your own gym.

### Installing Gym

`pip install -e .`

### Testing Installation
```
import gym
import bandit_gym

env = gym.make("MultiArmedBanditEnv-v0")
env.reset()
for _ in range(1000):
    env.step(env.action_space.sample())
env.render()
env.close()
```
