from flask import Flask

from Lamitt.videoPlayer.router import video_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(video_bp)

    return app
