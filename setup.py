import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="FDown",
    version="0.1",
    author="Ibrahim Cetin",
    author_email="cetinibrahim@yahoo.com",
    license='MIT',
    description="Simple File Downloader Module for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ibrahimcetin/FDown",
    packages=setuptools.find_packages(),
    keywords='Simple File Downloader Module for Python',
    install_requires=[
        'requests',
        'tqdm',
        'huepy',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
    entry_points={
        'console_scripts': [
            'fdown = fdown.__main__:client']}
)
