import os
from setuptools import setup, find_packages

from friendship import VERSION


f = open(os.path.join(os.path.dirname(__file__), 'README.rst'))
readme = f.read()
f.close()

setup(
    name='django-friendship',
    version=".".join(map(str, VERSION)),
    description='django-friendship provides an easy extensible interface for following and friendship',
    long_description=readme,
    author='Luis Velez',
    author_email='lvelezsantos@gmail.com',
    url='https://github.com/lvelezsantos/django-friendship',
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    test_suite='friendship.tests.runtests.runtests'
)
