from distutils.core import*
import sys, py2exe

sys.argv.append('py2exe')

setup(options = {'py2exe': {'bundle_files': 1, 'compressed': True}}, windows = [{'script': '<script_name>'}], zipfile = None)