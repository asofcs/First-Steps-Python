from setuptools import setup

setup(
  name='First_Steps_Python',
  version='1.0',
  author=@asofcs,
  licence="MIT",
  packages=['First_Steps_Python'], 
  install_requires=['numpy==2.1.0',
                    'pandas==2.2.2',
                    'scikit_learn==1.5.1'], # external dependencies,
  scripts=[
           'scripts/source.py', 
           'model/source.py', 
          ]
)

