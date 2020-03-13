#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2020
import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('ko_notification_utils/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

with open('README.md', 'rb') as f:
    readme = f.read().decode('utf-8')

with open('requirements.txt', 'r') as f:
    requirements = [x.strip() for x in f.readlines()]

setup(
    name='ko-notification-utils',
    version=version,
    keywords=['kubeOperator', 'DingTalk', 'WeiChat', 'Email'],
    description='kubeOperator notification util',
    long_description=readme,
    license='MIT Licence',
    url='https://kubeoperator.io/',
    author='kubeOperator team',
    author_email='support@fit2cloud.com',
    packages=['ko_notification_utils'],
    data_files=[('requirements', ['requirements.txt'])],
    include_package_data=True,
    install_requires=requirements,
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6'
    ]
)
