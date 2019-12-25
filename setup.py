"""This is the installation toolset for this project."""
from setuptools import setup, find_packages

with open('README.rst', 'r') as fh:
    long_description = fh.read()

setup(name='cotizacion_mep',
      version='0.1.0',
      author='dantebarba',
      description='cotizaciones del dolar MEP de Argentina',
      long_description=long_description,
      install_requires=["flask==1.1.1", "requests", "python-dateutil"],
      packages=find_packages(exclude=('tests',)),
      entry_points={
          'console_scripts': [
              'cotizacion_mep = cotizacion_mep.__main__:main'
          ]
      })
