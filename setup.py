from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()
with open(path.join(here, 'VERSION')) as version_file:
    version = version_file.read().strip()


setup(
    name='{{APP_NAME}}',
    version=version,
    description='{{SHORT_DESCRIPTION}}',
    long_description=long_description,
    url='{{URL}}',

    author='Michael Wright',
    author_email='mkwright@gmail.com',

    license='MIT',
    keywords='library',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        # Set this topic to what works for you
        'Topic :: Python :: Library',
        # Pick your license as you wish (should match "license" above)
        'License :: MIT',
        'Programming Language :: Python :: 3.5',
    ],

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    install_requires=[
        #'spacy>=1.3,<1.4'
    ],

    extras_require={
        'dev': [
            'wheel>=0.29'
        ],
        'test': [
            'pytest>=3.0,<4',
            'pytest-cov>=2.4,<3'
        ],
    },

    package_data={
        # 'sample': ['package_data.dat'],
    },

    # entry_points={
        # 'console_scripts': [
            # 'sample=sample:main',
        # ],
    # },
)
