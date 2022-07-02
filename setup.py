import setuptools
from setuptools import setup

setup(
    name='flask_config_environ_replacer',
    version='0.1',
    packages=['flask_config_environ_replacer'],
    url='https://github.com/saruhei/flask_config_environ_replacer',
    license='MIT',
    author='saruhei',
    author_email='',
    description='replace config field by environment variables.',
    install_requires=["flask"],
    python_requires='>=3.7'
)
