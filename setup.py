#!/usr/bin/env python

from setuptools import setup

setup(name='ontap-api-wrapper',
      version='0.5.2',
      description='Python wrapper for NetApp Manageability SDK',
      author='Andrew Leonard',
      author_email='andy.leonard@sbri.org',
      maintainer='Jiri Machalek',
      maintainer_email='machalekj@gmail.com',
      license='Apache License',
      py_modules=['Ontap'],
      packages=['netapp'],
      install_requires=['six'],
      url='https://github.com/machalekj/ontap-api-wrapper',
     )

