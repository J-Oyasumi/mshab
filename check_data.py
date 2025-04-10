import h5py

path = 'mshab_debug/gen_data_save_trajectories/set_table/pick/train/013_apple/20250410_072522.h5'


with h5py.File(path, 'r') as f:
    # 定义一个递归函数来打印文件结构
    def print_structure(name, obj):
        if isinstance(obj, h5py.Group):
            print(f"Group: {name}")
        elif isinstance(obj, h5py.Dataset):
            print(f"Dataset: {name}, Shape: {obj.shape}, Dtype: {obj.dtype}, type: {type(obj[0])}")

    # 遍历文件中的所有对象
    f.visititems(print_structure)