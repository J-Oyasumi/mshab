import os
import subprocess
from pathlib import Path

def main():
    # 固定任务和子任务
    task = "tidy_house"
    subtask = "place"

    # 获取 MS_ASSET_DIR 环境变量
    ms_asset_dir = os.getenv("MS_ASSET_DIR", os.path.expanduser("~/.maniskill"))
    ckpt_dir = Path(ms_asset_dir) / "data/mshab_checkpoints"

    # 如果检查点目录不存在，使用默认目录
    if not ckpt_dir.exists():
        ckpt_dir = Path("mshab_checkpoints")

    # 构造路径
    subtask_dir = ckpt_dir / "rl" / task / subtask
    if not subtask_dir.exists():
        raise FileNotFoundError(f"Subtask directory '{subtask_dir}' does not exist.")

    # 枚举对象名称
    for obj_name in subtask_dir.iterdir():
        if not obj_name.is_dir() or obj_name.name == "all":
            continue

        # 检查目标路径是否存在
        target_path = Path(f"mshab_exps/gen_data_save_trajectories/{task}/{subtask}/train/{obj_name.name}")
        if not target_path.exists():
            # 调用 Python 脚本生成数据
            subprocess.run(
                ["python", "-m", "mshab.utils.gen.gen_data", task, subtask, obj_name.name],
                check=True
            )

if __name__ == "__main__":
    main()