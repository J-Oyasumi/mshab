import os
import subprocess
from pathlib import Path
from termcolor import cprint

def main():
    # 获取 MS_ASSET_DIR 环境变量
    ms_asset_dir = os.getenv("MS_ASSET_DIR", os.path.expanduser("~/.maniskill"))
    ckpt_dir = Path(ms_asset_dir) / "data/mshab_checkpoints"

    # 如果检查点目录不存在，使用默认目录
    if not ckpt_dir.exists():
        ckpt_dir = Path("mshab_checkpoints")

    # 指定任务名称
    task_name = "set_table"  # 这里替换为你需要的任务名称
    task_dir = ckpt_dir.joinpath("rl", task_name)

    if not task_dir.is_dir():
        print(f"Task directory '{task_dir}' does not exist.")
        return

    # 遍历子任务和对象名称
    for subtask in task_dir.iterdir():
        if not subtask.is_dir():
            continue
        for obj_name in subtask.iterdir():
            if not obj_name.is_dir() or obj_name.name == "all":
                continue

            # 检查目标路径是否存在
            target_path = Path(f"mshab_exps/gen_data_save_trajectories/{task_name}/{subtask.name}/train/{obj_name.name}")
            if not target_path.exists():
                cmd = ["python", "-m", "mshab.utils.gen.gen_data", task_name, subtask.name, obj_name.name]
                cprint(" ".join(cmd), "red")
                # 调用 Python 脚本生成数据
                subprocess.run(cmd, check=True)

if __name__ == "__main__":
    main()