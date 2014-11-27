import setuptools

setuptools.setup(
    name="poxlibpacket",
    version="0.1.0",
    url="https://github.com/pexnet/pox",

    author="pex",
    author_email="pexnet0@gmail.com",maintainer="pex",
    maintainer_email="pexnet0@gmail.com",

    description="A pip package for the package libs in pox",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
