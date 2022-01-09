from setuptools import setup, find_packages
from pathlib import Path

with open(Path(__file__).parent / 'README.md') as f:
    long_description = f.read()

setup(
    name='pathlib-ext',
    author = 'Egor Abramov',
    author_email = 'coreegor@gmail.com',
    # version=__version__,
    description="pathlib extensions",
    packages=find_packages(),
    include_package_data=True,
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.8',
    install_requires=[
        'paramiko==2.9.2',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',

    ]

)
