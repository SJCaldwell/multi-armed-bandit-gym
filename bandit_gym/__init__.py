from gym.envs.registration import register

from .multi_armed_bandit_env import MultiArmedBanditEnv

environments = [['MultiArmedBanditEnv', 'v0']]

for environment in environments:
    register(
        id='{}-{}'.format(environment[0], environment[1]),
        entry_point='bandit_gym:{}'.format(environment[0]),
        nondeterministic=True
    )
