from setuptools import setup

setup(
    name='EasyJunction',
    version='0.1.0',
    py_modules=['EasyJunction'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'EasyJunction = EasyJunction:main',
        ],
    },
)