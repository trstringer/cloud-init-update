from setuptools import setup, find_packages

setup(
    name='cloud-init-update',
    version='0.1',
    description='cloud-init update',
    url='http://github.com/trstringer/cloud-init-update',
    author='Thomas Stringer',
    author_email='github@trstringer.com',
    license='MIT',
    packages=find_packages(),
    entry_points=dict(
        console_scripts=['cloudinitupdate=src.main:main']
    )
)
