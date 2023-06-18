import sys
from cx_Freeze import setup, Executable

# Include any necessary files
options = {
    'build_exe': {
        'include_files': [],
    }
}

# Set up the executable
exe = Executable(
    script='launcher.py',
    base='Win32GUI',
    icon='LOGO.ico',
)

# Set up the setup function
setup(
    name='Polyhack2023_Forward_Roll',
    version='1.0',
    description='CARE: Cyberbullying Assessment and Response Engine',
    options=options,
    executables=[exe],
)