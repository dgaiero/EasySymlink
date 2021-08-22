import os

import PyInstaller.__main__
from dotenv import load_dotenv

def run():
    load_dotenv()
    PyInstaller.__main__.run([
        'EasyJunction.py',
        '--hidden-import', 'tkinter',
        '--key', os.environ.get('ENCRYPTION_KEY'),
        '--noconfirm',
        '--noconsole',
        '--clean',
        '--icon', 'app_icon.ico',
        '--add-data', 'app_icon.ico;.'
    ])

if __name__ == "__main__":
    run()