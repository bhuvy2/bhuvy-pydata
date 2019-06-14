
import os
import setuptools
from setuptools.command.install import install
import bhuvy_pydata

class Installer(install):
    def run(self):
        bhuvy_pydata.register_style()
        install.run(self)

setuptools.setup(
  name              = 'bhuvy_pydata',
  version           = '0.0.1',
  author            = 'Bhuvan Venkatesh',
  author_email      = 'bhuvan.venkatesh21@gmail.com',
  url               = 'https://github.com/bhuvy2/bhuvy-pydata',
  keywords          = 'data, matplotlib, visualization',
  description       = 'Custom Visualization and Manipulation Functions',
  long_description  = '',
  license           = 'BSD3',
  install_requires  = ['matplotlib>=2.0.0', 'numpy>=1.0.0'],
  packages          = ['bhuvy_pydata'],
  cmdclass          = {'install': Installer},
)
