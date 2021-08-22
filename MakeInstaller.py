import subprocess
from pathlib import Path
from MakeExecutable import run as MakeExecutableFile

iss_loc = Path.cwd() / 'install_script.iss'
compil32_path = Path('C:/Program Files (x86)/Inno Setup 6') / 'iscc'

print('Making Executable')
MakeExecutableFile()
print('Compiling Installer')
subprocess.check_call([compil32_path, '/Qp', str(iss_loc)])
