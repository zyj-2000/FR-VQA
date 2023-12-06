import subprocess
import os
import re

import os
import shutil

def detect_file():
    # 获取当前文件夹路径
    folder_path = os.getcwd()

    # 遍历当前文件夹中的文件和文件夹
    for file_name in os.listdir(folder_path):
        # 检查文件是否以 "ffmpeg" 开头且不是文件夹
        if file_name.startswith("ffmpeg") and os.path.isfile(file_name):
            # 拷贝文件为 "copy.txt"
            shutil.copy(file_name, "copy.txt")

            # 删除原文件
            os.remove(file_name)

            print(f"文件 {file_name} 已拷贝为 copy.txt 并删除成功！")

def detect_file_psnr():
    # 获取当前文件夹路径
    folder_path = os.getcwd()

    # 遍历当前文件夹中的文件和文件夹
    for file_name in os.listdir(folder_path):
        # 检查文件是否以 "ffmpeg" 开头且不是文件夹
        if file_name.startswith("psnr") and os.path.isfile(file_name):
            # 拷贝文件为 "copy.txt"
            shutil.copy(file_name, "psnr.txt")

            # 删除原文件
            os.remove(file_name)

            print(f"文件 {file_name} 已拷贝为 copy.txt 并删除成功！")

def vmaf(video1, video2):
    command = f'ffmpeg.exe -i {video1} -i {video2} -lavfi libvmaf -report -f null - '
    os.system(command)

    detect_file()

    with open("copy.txt", 'r') as f:
        lines = f.readlines()

    vmaf_score = None

    for line in lines:
        if 'VMAF score:' in line:
            vmaf_score = float(line.split(':')[1])
            print(vmaf_score)

    return vmaf_score

    os.remove("copy.txt")

def psnr(video1, video2):
    command = f'ffmpeg.exe -i {video1} -i {video2} -lavfi psnr=stats_file=psnr_logfile.txt -report -f null - '
    os.system(command)

    detect_file()

    with open("copy.txt", 'r') as f:
        lines = f.readlines()

    psnr_score = None
    pattern = r'average:(.*?)(?= min)'
    for line in lines:
        if 'average:' in line:
            match = re.search(pattern, line)
            extracted_content = match.group(1)
            # psnr_score = float(line.split(':')[1])
            print(extracted_content)

    #return psnr_score

    # os.remove("copy.txt")

def ssim(video1, video2):
    command = f'ffmpeg.exe -i {video1} -i {video2} -lavfi ssim=stats_file=ssim_logfile.txt -report -f null - '

    os.system(command)

    detect_file()

    with open("copy.txt", 'r') as f:
        lines = f.readlines()

    ssim_score = None
    pattern = r'average:(.*?)(?= min)'

    for line in lines:
        if 'All:' in line:
            ssim_score_p = line.split('All:')[1]
            if 'inf' in ssim_score_p:
                ssim_score = 1
                print("inf")
            else:
                ssim_score = float(ssim_score_p)
            print(ssim_score)

    return ssim_score

    # os.remove("copy.txt")

score = ssim("test.mp4","test.mp4")
print(score)