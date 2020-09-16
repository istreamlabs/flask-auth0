# Created by Samuel Lesuffleur 02-10-2017
#
# Copyright (c) 2017 Sandtable Ltd. All rights reserved.
from setuptools import setup, find_packages


setup(
    name='istreamplanet-flask-auth0',
    license='MIT',
    version='0.1.0',
    description='A Flask extension for authenticating web applications using Auth0. Forked from https://github.com/sandtable/flask-auth0',
    author='Samuel Lesuffleur, Jason LaDuke',
    author_email='jasonladuke0311@gmail.com',
    url='https://github.com/istreamlabs/flask-auth0',
    packages=find_packages(),
    platforms='any',
    include_package_data=False,
    install_requires=[
        'flask',
        'authlib',
    ],
    tests_require=[
        'pytest'
    ],
    zip_safe=False,
    keywords='flask auth0 authentication',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Framework :: Flask'
    ]
)
