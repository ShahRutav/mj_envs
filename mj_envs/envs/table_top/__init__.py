import os
from gym.envs.registration import register

print("RS:> Registering Table Top Envs")
# Swing the door open
curr_dir = os.path.dirname(os.path.abspath(__file__))
TABLE_TOP_ENVS = {'reorient-fixed-v0', 'reorient-random-v0', 'reorient-random-full-v0', 'reorient-fixed-v1', 'reorient-random-v1', 'reorient-random-full-v1', 'reorient-tool_color-full-v1', 'reorient-table_color-full-v1'}

MODEL_PATH=curr_dir+'/assets/reorient.xml'
register(
    id='reorient-fixed-v0',
    entry_point='mj_envs.envs.table_top:ReorientEnvV0',
    kwargs={
        "model_path": MODEL_PATH,
        "goal": [[1.57, 1.57], [0.0, 0.0], [0.0, 0.0]], # Sets the orientation of the body. (0,0,0) sets it to default
        "ctrl1": [[0.05, 0.05], [-0.1, -0.1], [0.035, 0.035]], # 0.05 -0.1 0.035
        #"obs_keys_wt": obs_keys_wt,
        "generate_rd_tools": {"rd_tool_rgba":False, "rd_tool_type":False, "rd_tool_size":False, "rd_table_rgba":False},
        "num_tools": 1,
        "num_tables": 1,
    },
    max_episode_steps=100,
)
register(
    id='reorient-random-v0',
    entry_point='mj_envs.envs.table_top:ReorientEnvV0',
    kwargs={
        "model_path": MODEL_PATH,
        "goal": [[1.57, 1.57], [0.0, 6.28], [0.0, 0.0]], # Sets the orientation of the body.
        "ctrl1": [[0.05, 0.05], [-0.1, -0.1], [0.035, 0.035]], # 0.05 -0.1 0.035
        #"obs_keys_wt": obs_keys_wt,
        "generate_rd_tools": {"rd_tool_rgba":False, "rd_tool_type":False, "rd_tool_size":False, "rd_table_rgba":False},
        "num_tools": 1,
        "num_tables": 1,
    },
    max_episode_steps=100,
)
register(
    id='reorient-random-full-v0',
    entry_point='mj_envs.envs.table_top:ReorientEnvV0',
    kwargs={
        "model_path": MODEL_PATH,
        "goal": [[1.57, 1.57], [0.0, 6.28], [0.0, 0.0]], # Sets the orientation of the body.
        "ctrl1": [[-0.1, 0.2], [-0.1, -0.1], [0.035, 0.035]],
        #"obs_keys_wt": obs_keys_wt,
        "generate_rd_tools": {"rd_tool_rgba":False, "rd_tool_type":False, "rd_tool_size":False, "rd_table_rgba":False},
        "num_tools": 1,
        "num_tables": 1,
    },
    max_episode_steps=100,
)
register(
    id='reorient-fixed-v1',
    entry_point='mj_envs.envs.table_top:ReorientEnvV0',
    kwargs={
        "model_path": MODEL_PATH,
        "goal": [[1.57, 1.57], [0.0, 0.0], [0.0, 0.0]], # Sets the orientation of the body. (0,0,0) sets it to default
        "ctrl1": [[0.05, 0.05], [-0.1, -0.1], [0.035, 0.035]], # 0.05 -0.1 0.035
        #"obs_keys_wt": obs_keys_wt,
        "generate_rd_tools": {"rd_tool_rgba":True, "rd_tool_type":True, "rd_tool_size":True, "rd_table_rgba":False},
        "num_tools": 1000,
        "num_tables": 1,
    },
    max_episode_steps=100,
)
register(
    id='reorient-random-v1',
    entry_point='mj_envs.envs.table_top:ReorientEnvV0',
    kwargs={
        "model_path": MODEL_PATH,
        "goal": [[1.57, 1.57], [0.0, 6.28], [0.0, 0.0]], # Sets the orientation of the body.
        "ctrl1": [[0.05, 0.05], [-0.1, -0.1], [0.035, 0.035]], # 0.05 -0.1 0.035
        #"obs_keys_wt": obs_keys_wt,
        "generate_rd_tools": {"rd_tool_rgba":True, "rd_tool_type":True, "rd_tool_size":True, "rd_table_rgba":False},
        "num_tools": 1000,
        "num_tables": 1,
    },
    max_episode_steps=100,
)
register(
    id='reorient-random-full-v1',
    entry_point='mj_envs.envs.table_top:ReorientEnvV0',
    kwargs={
        "model_path": MODEL_PATH,
        "goal": [[1.57, 1.57], [0.0, 6.28], [0.0, 0.0]], # Sets the orientation of the body.
        "ctrl1": [[-0.1, 0.2], [-0.1, -0.1], [0.035, 0.035]],
        #"obs_keys_wt": obs_keys_wt,
        "generate_rd_tools": {"rd_tool_rgba":True, "rd_tool_type":True, "rd_tool_size":True, "rd_table_rgba":False},
        "num_tools": 1000,
        "num_tables": 1,
    },
    max_episode_steps=100,
)
register(
    id='reorient-tool_color-full-v1',
    entry_point='mj_envs.envs.table_top:ReorientEnvV0',
    kwargs={
        "model_path": MODEL_PATH,
        "goal": [[1.57, 1.57], [0.0, 6.28], [0.0, 0.0]], # Sets the orientation of the body.
        "ctrl1": [[-0.1, 0.2], [-0.1, -0.1], [0.035, 0.035]],
        #"obs_keys_wt": obs_keys_wt,
        "generate_rd_tools": {"rd_tool_rgba":True, "rd_tool_type":False, "rd_tool_size":False, "rd_table_rgba":False},
        "num_tools": 1000,
        "num_tables": 1,
    },
    max_episode_steps=100,
)
register(
    id='reorient-table_color-full-v1',
    entry_point='mj_envs.envs.table_top:ReorientEnvV0',
    kwargs={
        "model_path": MODEL_PATH,
        "goal": [[1.57, 1.57], [0.0, 6.28], [0.0, 0.0]], # Sets the orientation of the body.
        "ctrl1": [[-0.1, 0.2], [-0.1, -0.1], [0.035, 0.035]],
        #"obs_keys_wt": obs_keys_wt,
        "generate_rd_tools": {"rd_tool_rgba":False, "rd_tool_type":False, "rd_tool_size":False, "rd_table_rgba":True},
        "num_tools": 1,
        "num_tables": 10,
    },
    max_episode_steps=100,
)
from mj_envs.envs.table_top.reorient_v0 import ReorientEnvV0
