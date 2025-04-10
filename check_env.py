import gymnasium as gym
from mani_skill import ASSET_DIR

import mshab.envs
from mshab.envs.planner import plan_data_from_file
task = "tidy_house" # "tidy_house", "prepare_groceries", or "set_table"
subtask = "pick"    # "sequential", "pick", "place", "open", "close"
                    # NOTE: sequential loads the full task, e.g pick -> place -> ...
                    #     while pick, place, etc only simulate a single subtask each episode
split = "train"     # "train", "val"


REARRANGE_DIR = ASSET_DIR / "scene_datasets/replica_cad_dataset/rearrange"

plan_data = plan_data_from_file(
    REARRANGE_DIR / "task_plans" / task / subtask / split / "all.json"
)
spawn_data_fp = REARRANGE_DIR / "spawn_data" / task / subtask / split / "spawn_data.pt"

env = gym.make(
    f"{subtask.capitalize()}SubtaskTrain-v0",
    # Simulation args
    num_envs=252,  # RCAD has 63 train scenes, so 252 envs -> 4 parallel envs reserved for each scene
    obs_mode="pointcloud",
    sim_backend="gpu",
    robot_uids="fetch",
    control_mode="pd_joint_delta_pos",
    # Rendering args
    reward_mode="normalized_dense",
    render_mode="rgb_array",
    shader_dir="minimal",
    # TimeLimit args
    max_episode_steps=200,
    # SequentialTask args
    task_plans=plan_data.plans,
    scene_builder_cls=plan_data.dataset,
    # SubtaskTrain args
    spawn_data_fp=spawn_data_fp,
    # optional: additional env_kwargs
)

print(env.observation_space)
print(env.action_space)