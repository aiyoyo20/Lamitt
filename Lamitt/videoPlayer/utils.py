import os

from Lamitt import config


VIDEO_PATH = config.video_config["video_path"]
SUPPORTED_FORMATS = [".mp4", ".avi", ".mkv"]


def get_video_files():
    '''获取目标地址下的所有视频文件
    '''

    video_files = [f for f in os.listdir(VIDEO_PATH) if f.lower().endswith(tuple(SUPPORTED_FORMATS))]
    return video_files
