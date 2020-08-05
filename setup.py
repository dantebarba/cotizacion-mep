"""This is the installation toolset for this project."""
from setuptools import setup, find_packages

with open('README.rst', 'r') as fh:
    long_description = fh.read()

setup(name='cotizacion_mep',
      version='0.5.0',
      author='dantebarba',
      description='cotizaciones del dolar MEP de Argentina',
      long_description=long_description,
      install_requires=["flask==1.1.1", "requests==2.20.0", "python-dateutil==2.7.5", "apscheduler==3.5.3", "pymongo==3.7.1"],
      packages=find_packages(exclude=('tests',)),
      entry_points={
          'console_scripts': [
              'cotizacion_mep = cotizacion_mep.__main__:main'
          ]
      })
