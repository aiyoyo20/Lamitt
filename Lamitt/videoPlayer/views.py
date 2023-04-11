from flask import render_template, request, send_from_directory

from Lamitt.videoPlayer.utils import get_video_files
from Lamitt import config


def index():
    video_files = get_video_files()
    current_video = request.args.get('video')
    if current_video is None:
        current_video = video_files[0]
    return render_template(
        'video.html',
        video_files=video_files,
        current_video=current_video
        )


def videos(filename):
    VIDEO_PATH = config.video_config["video_path"]
    return send_from_directory(VIDEO_PATH, filename)
