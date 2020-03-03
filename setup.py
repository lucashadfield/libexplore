from setuptools import setup, find_packages

setup(
    name='libexplore',
    version='0.0.1',
    author='Lucas Hadfield',
    packages=find_packages(),
    install_requires=[],
    include_package_data=True,
    entry_points={
        'console_scripts': ['libexplore=libexplore.pycharm_launcher:command_line'],
    },
)
