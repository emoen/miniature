from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import itertools

from tf_agents.environments import py_environment
from tf_agents.specs import array_spec
from tf_agents.trajectories import time_step as ts
import numpy as np

#https://heartbeat.comet.ml/stock-trading-rl-agent-using-tf-agents-framework-9713a778edb6
class StockTraderEnv(py_environment.PyEnvironment):

    def __init__(self, data, initInvestment=20000):
        self._action_spec = array_spec.BoundedArraySpec(
            shape=(), dtype=np.int32, minimum=0, maximum=26, name='action')
        self._observation_spec = array_spec.BoundedArraySpec(
            shape=(7,), dtype=np.float64, name='observation')
        self.stock_price_history = data
        self.init_investment = initInvestment
        self.state = 0
        self.episode_ended = False
        self.stock_owned = None
        self.stock_price = None
        self.cash_in_hand = None
        self.n_stock = 3
        self.n_step = self.stock_price_history.shape[0]
        self.action_list = list(map(list, itertools.product([0, 1, 2], repeat=self.n_stock)))
#[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 1, 2], [0, 2, 0], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 1], [1, 0, 2], [1, 1, 0],
#[1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 0], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]
        self.action_space = np.arange(3 ** self.n_stock)
        ###[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26]##np.ndarray
        self.scaler = None

    def action_spec(self):
        return self._action_spec

    def observation_spec(self):
        return self._observation_spec

    def set_scaler(self, scaler):
        self.scaler = scaler

    def get_obs(self):
        obs = np.empty(7)
        obs[:self.n_stock] = self.stock_owned
        obs[self.n_stock:2 * self.n_stock] = self.stock_price
        obs[-1] = self.cash_in_hand
        if self.scaler != None:
            obs = self.scaler.transform([obs]).flatten()
        return obs

    def get_val(self):
        return self.stock_owned.dot(self.stock_price) + self.cash_in_hand

    def _reset(self):
        self.state = 0
        self.episode_ended = False
        self.stock_owned = np.zeros(self.n_stock)
        self.stock_price = self.stock_price_history[self.state]
        self.cash_in_hand = self.init_investment
        return ts.restart(self.get_obs())

    def _step(self, action):

        if self.episode_ended:
            # The last action ended the episode. Ignore the current action and start
            # a new episode.
            return self._reset()

        # get current value before performing the action
        prev_val = self.get_val()

        self.stock_price = self.stock_price_history[self.state]

        # update price, i.e. go to the next day
        self.state += 1

        # perform the trade
        self.trade(action)

        # get the new value after taking the action
        cur_val = self.get_val()

        # reward is the increase in porfolio value
        reward = cur_val - prev_val

        # done if we have run out of data
        done = self.state == self.n_step - 1

        # store the current value of the portfolio here
        info = {'cur_val': self.state}

        # conform to the Gym API
        # return self._get_obs(), reward, done, info
        if (done != True):
            return ts.transition(self.get_obs(), reward=reward, discount=1.0)
        else:
            self.episode_ended = True
            return ts.termination(self.get_obs(), reward)

    def trade(self, action):
        # index the action we want to perform
        # 0 = sell
        # 1 = hold
        # 2 = buy
        # e.g. [2,1,0] means:
        # buy first stock
        # hold second stock
        # sell third stock
        action_vec = self.action_list[action]

        # determine which stocks to buy or sell
        sell_index = []  # stores index of stocks we want to sell
        buy_index = []  # stores index of stocks we want to buy
        for i, a in enumerate(action_vec):
            if a == 0:
                sell_index.append(i)
            elif a == 2:
                buy_index.append(i)

        # sell any stocks we want to sell
        # then buy any stocks we want to buy
        if sell_index:
            # NOTE: to simplify the problem, when we sell, we will sell ALL shares of that stock
            for i in sell_index:
                self.cash_in_hand += self.stock_price[i] * self.stock_owned[i]
                self.stock_owned[i] = 0
        if buy_index:
            # NOTE: when buying, we will loop through each stock we want to buy,
            #       and buy one share at a time until we run out of cash
            can_buy = True
            while can_buy:
                for i in buy_index:
                    if self.cash_in_hand > self.stock_price[i]:
                        self.stock_owned[i] += 1  # buy one share
                        self.cash_in_hand -= self.stock_price[i]
                    else:
                        can_buy = False
