#Driver: Drivers are the main worker in the RL learning process. The training process of the RL agent involves multiple steps, 
#including selecting an action based on the epsilon value, performing the action, calculating the reward, adjusting the weight values, etc. 
#TF-Agents drivers abstract all the underlying action and help you define them with a single command.



train_env._reset()

init_driver = DynamicStepDriver(
    train_env,
    random_policy,
    observers=[replay_buffer.add_batch],
    num_steps=2_500)
final_time_step, final_policy_state = init_driver.run()



# Create a driver to collect experience.
collect_driver = DynamicStepDriver(
    train_env,
    agent.collect_policy,
    observers=[replay_buffer.add_batch],
    num_steps=4) # collect 4 steps for each training iteration


