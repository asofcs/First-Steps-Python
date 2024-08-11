from setuptools import setup

setup(
  name='First_Steps_Python',
  version='1.0',
  author=@asofcs,
  licence="MIT",
  packages=['First_Steps_Python'], 
  install_requires=['matplotlib==3.8.0', 
                    'numpy==2.0.1',
                    'pandas==2.2.2',
                    'scikit_learn==1.3.0'], # external dependencies,
  scripts=[
           'source/source.py', 
          ]
)
