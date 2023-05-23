import os
from moviepy.editor import VideoFileClip

# 输入文件夹路径和目标文件格式（例如 MP4）
import glob
video_list1=glob.glob("C:/Users/WY/Desktop/user_study&demo/#user_study/*")
video_list2=glob.glob("C:/Users/WY/Desktop/user_study&demo/#user_study_exp/*")
for input_folder in video_list1[:-1]:
    # input_folder ='C:/Users/WY/Desktop/user_study_demo/user_study/case (1)'
    print(input_folder)
    output_format = 'mp4'

    # 遍历文件夹中的视频文件
    for filename in os.listdir(input_folder):
        if 'PIR'in filename:
            # 构建输入视频文件路径
            input_path = os.path.join(input_folder, filename)
            
            # 创建 MoviePy 的 VideoFileClip 对象
            clip = VideoFileClip(input_path)
            
            # 设置输出视频的参数
            output_path = "P"+os.path.splitext(filename)[0] + '.' + output_format
            output_path = os.path.join(input_folder, output_path)
            
            # 输出为目标格式的视频文件
            clip.write_videofile(output_path, codec='libx264', audio=False)
