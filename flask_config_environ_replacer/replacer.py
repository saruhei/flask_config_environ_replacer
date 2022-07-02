# coding: utf-8
import os

from flask import Flask


def replace_flask_config_by_environment(flask_app: Flask) -> Flask:
    for config_key in flask_app.config.keys():
        if config_key in os.environ.keys():
            flask_app.config[config_key] = os.environ[config_key]
    return flask_app
