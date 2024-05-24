from setuptools import setup

setup(
    name='PrivatBank API',
    description='Client to interact with privat bank public api',
    version='0.1',
    packages=['privatbank_api'],
    install_requires=[
        'requests>=2.32.2',
    ]
)
