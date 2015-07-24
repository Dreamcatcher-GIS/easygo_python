from distutils.core import setup
import sys

import easygo

kw = dict(
    name = 'easygopy',
    version = easygo.__version__,
    description = 'Easygo API Python SDK',
    author = 'DreamCatcher',
    author_email = 'kp_clown@126.com',
    url = 'https://github.com/Dreamcatcher-GIS/easygo_python',
    download_url = 'https://github.com/Dreamcatcher-GIS/easygo_python',
    py_modules = ['easygo'],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ])

setup(**kw)
