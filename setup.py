import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='xecd_rates',
    version='1.0.3',
    url='https://github.com/doguskidik/xecd-rates-python',
    packages=setuptools.find_packages(exclude=['tests*']),
    description='Xecd Rates Python: Free currency  rates converter',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Doğuş KIDIK',
    license='MIT',
    author_email='dogus.kidik@gmail.com',
    zip_safe=True,
    test_suite='tests',
    install_requires=[
        'requests',
        'lxml'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta"
    ]
)
