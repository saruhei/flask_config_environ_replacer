# coding: utf-8
import os

from flask import Flask


def replace_flask_config_by_environment(flask_app: Flask):
    for config_key in flask_app.config.keys():
        if config_key in os.environ:
            setattr(flask_app, config_key, os.environ[config_key])
    return flask_app
