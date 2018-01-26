import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.

options = {
    'build_exe': {
        'packages': [
            "pandas",
            "numpy"
        ],
        'includes': [
            'datacut',
            'setting',
            'plotgraph',
            'matplotlib.backends.backend_tkagg',
            'tkinter.filedialog'
        ],
        'path': sys.path + ["src"]
    }
}

base = 'Console'

executables = [
    Executable('plotlog.py', base=base)
]

setup(name='plotlog',
      version='1.0.0',
      description='Plot graph for many log file that is managed by DATE',
      options=options,
      executables=executables)
