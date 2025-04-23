#!/usr/bin/bash

task="set_table"
subtask="close"
obj_name="kitchen_counter"

rm -rf mshab_data/gen_data_save_trajectories/$task/$subtask/train/$obj_name

if [[ ! -e "mshab_data/gen_data_save_trajectories/$task/$subtask/train/$obj_name" && $obj_name != "all" ]]; then
    python -m mshab.utils.gen.gen_data "$task" "$subtask" "$obj_name"
fi
