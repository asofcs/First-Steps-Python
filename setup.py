from setuptools import setup

setup(
  name='First_Steps_Python',
  version='1.0',
  author=@asofcs,
  licence="MIT",
  packages=['First_Steps_Python'], 
  install_requires=[], # external dependencies,
  scripts=[
           'functions/x', 
           'functions/y',
          ]
)
