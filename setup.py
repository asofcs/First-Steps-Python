from setuptools import setup

setup(
  name='First_Steps_Python',
  version='1.0',
  author=@asofcs,
  licence="MIT",
  packages=['First_Steps_Python'], 
  install_requires=['network==3.3', 
                    'pandapower==2.14.9',], # external dependencies,
  scripts=[
           'source/source.py', 
          ]
)
