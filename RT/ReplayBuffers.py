from tf_agents.replay_buffers import TFUniformReplayBuffer
from tf_agents.drivers.dynamic_step_driver import DynamicStepDriver

replay_buffer = TFUniformReplayBuffer(
    data_spec=agent.collect_data_spec,
    batch_size=train_env.batch_size,
    max_length=100_000)
