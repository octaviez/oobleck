import os

import setuptools

version = os.environ["OOBLECK_VERSION"]

with open("README.md", "r") as readme:
    readme = readme.read()

with open("requirements.txt", "r") as requirements:
    requirements = requirements.read()

setuptools.setup(
    name="oobleck",
    version=version,
    author="Harmonai-org",
    author_email="",
    description="OOBLECK: Out-of-the-box latent construction toolkit",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    package_data={
        'oobleck/configs': ['*.gin'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements.split("\n"),
    python_requires='>=3.9',
    include_package_data=True,
)