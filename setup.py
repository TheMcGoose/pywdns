#!/usr/bin/env python

NAME = 'pywdns'
VERSION = '0.9.0'
LICENSE = 'Apache License 2.0'
DESCRIPTION = 'Python extension module for the wdns C library'
URL = 'https://github.com/farsightsec/pywdns'
AUTHOR = 'Farsight Security, Inc.'
AUTHOR_EMAIL = 'software@farsightsecurity.com'

from distutils.core import setup
from distutils.extension import Extension
import subprocess

subprocess.check_call('./gen_pywdns_constants')

def pkgconfig(*packages, **kw):
    flag_map = {
            '-I': 'include_dirs',
            '-L': 'library_dirs',
            '-l': 'libraries'
    }
    pkg_config_cmd = (
    'pkg-config',
        '--cflags',
        '--libs',
        ' '.join(packages),
    )
    pkg_config_output = subprocess.check_output(pkg_config_cmd, universal_newlines=True)
    for token in pkg_config_output.split():
        flag = token[:2]
        arg = token[2:]
        if flag in flag_map:
            kw.setdefault(flag_map[flag], []).append(arg)
    return kw

try:
    from Cython.Distutils import build_ext
    setup(
        name = NAME,
        version = VERSION,
        license = LICENSE,
        description = DESCRIPTION,
        url = URL,
        author = AUTHOR,
        author_email = AUTHOR_EMAIL,
        ext_modules = [ Extension('wdns', ['wdns.pyx'], **pkgconfig('libwdns >= 0.9.0')) ],
        cmdclass = {'build_ext': build_ext},
        py_modules = ['wdns_constants'],

    )
except ImportError:
    import os
    if os.path.isfile('wdns.c'):
        setup(
            name = NAME,
            version = VERSION,
            license = LICENSE,
            description = DESCRIPTION,
            url = URL,
            author = AUTHOR,
            author_email = AUTHOR_EMAIL,
            ext_modules = [ Extension('wdns', ['wdns.c'], **pkgconfig('libwdns >= 0.9.0')) ],
            py_modules = ['wdns_constants'],
        )
    else:
        raise
