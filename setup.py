from distutils.core import setup

setup(
    name='safire',
    version='0.1',
    packages=['safire',],
    package_data={'safire': ['static/js/*',
                                'templates/*']
    },
    install_requires=[
        "Flask >= 0.9"
    ],
)