import importlib
import os
import subprocess
import argparse


def pycharm_launcher(lib_name: str) -> None:
    pycharm = (
        subprocess.check_output(
            'compgen -c pycharm', shell=True, executable='/bin/bash'
        )
        .decode('utf-8')
        .split('\n')[0]
    )

    package_loc = importlib.util.find_spec(lib_name).submodule_search_locations[0]

    command = f'{pycharm} {package_loc}'

    print(f'running: {command}')
    os.system(command)


def command_line():
    argparser = argparse.ArgumentParser(description='Explore library  with Pycharm')
    argparser.add_argument('lib_name', type=str)
    args = argparser.parse_args()

    pycharm_launcher(args.lib_name)
