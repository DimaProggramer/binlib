from setuptools import setup, find_packages

setup(
    name="binlib",
    version="1.0.0",
    description="Library for working with binary code: encoding, decoding and utilities.",
    author="DimaProggramer",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
