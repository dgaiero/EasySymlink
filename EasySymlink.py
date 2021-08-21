import ctypes
import os
import sys
from pathlib import Path
from tkinter import Tk, filedialog, messagebox, simpledialog, PhotoImage
# from icon import Icon

import click
import base64
from ntfsutils.junction import create as CreateJunction

kdll = ctypes.windll.LoadLibrary("kernel32.dll")
ctypes.windll.shcore.SetProcessDpiAwareness(1)


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath('.'), relative_path)

@click.command()
@click.argument('in_dir', type=click.Path(exists=True))
@click.option('--quick', help='Add this folder to the root of OneDrive.', default=False, is_flag=True)
def main(in_dir, quick):
    root = Tk()
    # img = base64.b64decode(Icon().img)
    # print(img)
    # ico = PhotoImage(data=base64.b64decode(Icon().img))
    # print(ico)
    # root.wm_iconphoto()
    root.withdraw()
    root.attributes('-topmost', True)
    in_dir = Path(in_dir)
    # root.iconbitmap('app_icon.ico')
    root.wm_iconbitmap(False, resource_path('app_icon.ico'))
    # click.echo(os.path.basename(in_dir))
    onedrive_location = Path(os.path.expandvars('%onedrive%'))
    if not quick:
        out_dir = filedialog.askdirectory(initialdir=onedrive_location)
        if out_dir == "":
            sys.exit()
        else:
            out_dir = Path(out_dir)
        final_dir = simpledialog.askstring("Link Directory", "Please enter the name of the output directory",
                                    initialvalue=os.path.basename(in_dir))
        if final_dir is None:
            sys.exit()
        else:
            out_dir = out_dir / final_dir
    else:
        out_dir = onedrive_location / os.path.basename(in_dir)
    if (os.path.normpath(in_dir) == os.path.normpath(out_dir)):
        messagebox.showerror(
            'Circular Reference', 'The input and output directories are the same. Try again.')
        sys.exit()
    if os.path.exists(out_dir):
        messagebox.showerror(
            'Directory Exists', f'The directory {out_dir} already exists. Please try again with a directory that does not exist.')
        sys.exit()

    in_dir_str = str(in_dir.resolve())
    out_dir_str = str(out_dir.resolve())
    CreateJunction(in_dir_str, out_dir_str)


if getattr(sys, 'frozen', False):
    main(sys.argv[1:])
