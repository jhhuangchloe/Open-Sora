import pandas as pd

# 读取 CSV 文件
file_path = 'NS_video_vinfo.csv'  # 替换为你的 CSV 文件路径
df = pd.read_csv(file_path)

# 添加新列 'text' 并将其值设置为 'caption'
df['text'] = 'caption'

# 保存修改后的 CSV 文件
output_file_path = 'NS_video_new.csv'  # 设置输出文件路径
df.to_csv(output_file_path, index=False)

print("New column 'text' with value 'caption' added successfully.")