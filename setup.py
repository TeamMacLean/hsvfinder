from setuptools import setup, find_packages

setup(
    name="hsvfinder",
    version="0.0.1",
    author="Dan MacLean, Alexander Reynolds",
    install_requires=["opencv-python"],
    packages=find_packages(),
    description="Reporting HSV values in flood filled masked areas.",
)
