from setuptools import setup

setup(
    name = "shortboy",
    version = "0.1.0",
    description = "A good version for good people",
    author = "AitzazImtiaz",
    url = "https://github.com/AitzazImtiaz/Short-Boy",
    packages = ["shortboy"],
    entry_points = {
        'console_scripts': [
            'shortboy = shortboy.__main__:main'
        ]
    },
)
