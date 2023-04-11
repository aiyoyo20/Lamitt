import os

from Lamitt import config


VIDEO_PATH = config.video_config["video_path"]
SUPPORTED_FORMATS = [".mp4", ".avi", ".mkv"]


def get_video_files():
    video_files = [f for f in os.listdir(VIDEO_PATH) if f.lower().endswith(tuple(SUPPORTED_FORMATS))]
    return video_files
