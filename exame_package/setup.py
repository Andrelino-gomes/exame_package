import os
requirementPath = 'requirements.txt'
install_requires = []

if os.path.isfile(requirementPath):
    with open(requirementPath) as f:
        install_requires = f.read().splitlines()

from setuptools import setup, find_packages
setup(
      name="exame_packeg",
      version="0.1",
      description="opstring Distribution Package",
      packages=find_packages(),
      include_package_data=True,
      install_requires=install_requires,
      entry_points={
            'console_scripts': [
                  'exame_packeg=exame_packeg.cli:main'
            ]
      }
)