from setuptools import setup

setup(
  name='First_Steps_Python',
  version='1.0',
  author=@asofcs,
  licence="MIT",
  packages=['First_Steps_Python'], 
  install_requires=['pandas==2.2.2'], # external dependencies,
  scripts=[
           'functions/functions.py', 
          ]
)
