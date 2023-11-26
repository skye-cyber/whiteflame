from setuptools import setup

setup(
    name='whiteflame',
    version='1.0',
    author="Wambua aka Bullet Angel",
    packages=["whiteflame"],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    entry_points={
        'console_scripts': [
            "whiteflame=whiteflame:restart_program"],
    },
    python_requires='>=3.6',
    install_requires=[

    ],
    include_package_data=True,
    license="MIT",
    keywords='whiteflame',
    classifiers=[
        "Environment :: Console",
        "Operating System :: POSIX :: Linux",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
