
from setuptools import setup

with open("README", 'r') as f:
    long_description = f.read()

setup(

   name='pyes',
   version='0.1',
   description='Extendscript to Python bridge',
   license="GNU",
   long_description=long_description,
   author='Yahia Boudah',
   author_email='yahiabouda@hotmail.com',
   url="",
   packages=['pyes'], #same as name
   install_requires=[], #external packages as dependencies
   scripts=[]
)