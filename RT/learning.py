

num_iterations = 100_000
while True:
    # Collect a few steps using collect_policy and save to the replay buffer.
    time_step, policy_state = collect_driver.run(time_step, policy_state)

    # Sample a batch of data from the buffer and update the agent's network.
    experience, unused_info = next(iterator)
    train_loss = agent.train(experience).loss

    step = agent.train_step_counter.numpy()
    print(f'\r step {step}', end='')

    if step % log_interval == 0:
        print('step = {0}: loss = {1}'.format(step, train_loss))

    if step % eval_interval == 0:
        avg_return = compute_avg_return(train_env, agent.policy, num_episodes=1)
        print('step = {0}: Average Return = {1}'.format(step, avg_return))
        returns = np.append(returns, avg_return)

    # if step % save_interval == 0:
    #     save_checkpoint_to_local()

    if step > num_iterations:
        break


