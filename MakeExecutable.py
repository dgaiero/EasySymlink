import base64
import os

import PyInstaller.__main__
from dotenv import load_dotenv

import base64
with open("app_icon.py", "w") as f:
    f.write('class Icon(object):\n')
    f.write('\tdef __init__(self):\n')
    f.write("\t\tself.img='")
with open("app_icon.ico", "rb") as i:
    b64str = base64.b64encode(i.read())
    with open("icon.py", "ab+") as f:
        f.write(b64str)
with open("icon.py", "a") as f:
    f.write("'")

load_dotenv()

PyInstaller.__main__.run([
    'EasySymlink.py',
    '--hidden-import', 'tkinter',
    '--key', os.environ.get('ENCRYPTION_KEY'),
    '--noconfirm',
    '--clean',
    '--icon', 'app_icon.ico',
    '--add-data', 'app_icon.ico;.'
])
