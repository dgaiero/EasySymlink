from setuptools import setup

setup(
    name='EasySymlink',
    version='0.1.0',
    py_modules=['EasySymlink'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'EasySymlink = EasySymlink:main',
        ],
    },
)