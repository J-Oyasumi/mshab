#!/usr/bin/bash

# shellcheck disable=SC2045

if [[ -z "${MS_ASSET_DIR}" ]]; then
    MS_ASSET_DIR="$HOME/.maniskill"
fi

if [[ -f "$MS_ASSET_DIR/data/mshab_checkpoints" ]]; then
    CKPT_DIR="$MS_ASSET_DIR/data/mshab_checkpoints"
else
    CKPT_DIR="mshab_checkpoints"
fi

for task in $(ls -1 "$CKPT_DIR/rl")
do
    for subtask in $(ls -1 "$CKPT_DIR/rl/$task")
    do
        for obj_name in $(ls -1 "$CKPT_DIR/rl/$task/$subtask")
        do
            if [[ ! -e "mshab_exps/gen_data_save_trajectories/$task/$subtask/train/$obj_name" && $obj_name != "all" ]]; then
                python -m mshab.utils.gen.gen_data "$task" "$subtask" "$obj_name"
            fi
        done
    done
done