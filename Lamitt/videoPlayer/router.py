from flask import Blueprint

from Lamitt.videoPlayer.views import index
from Lamitt.videoPlayer.views import videos

video_bp = Blueprint(
    "video",
    __name__,
    url_prefix="/video"
    )

video_bp.add_url_rule('/', view_func=index)
video_bp.add_url_rule('/<filename>', view_func=videos)
