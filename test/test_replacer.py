# coding: utf-8
import os

import pytest
from flask import Flask

from flask_config_environ_replacer.replacer import replace_flask_config_by_environment


@pytest.fixture
def set_environ():
    os.environ['TEST_TARGET'] = 'test'
    yield
    del os.environ['TEST_TARGET']


def test_replace_flask_config_by_environment(set_environ):
    app: Flask = Flask(__name__)
    app.config['TEST_TARGET'] = 'before'
    app = replace_flask_config_by_environment(app)
    assert app.config['TEST_TARGET'] == 'test'
