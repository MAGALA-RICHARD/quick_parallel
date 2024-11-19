from setuptools import setup, find_packages

VERSION = '0.0.1.2'
DESCRIPTION = 'quick parallel process set up library'
LONG_DESCRIPTION = 'parallelize your function with ease, no need to be a master of parallelization'

with open('README.rst') as readme_file:
    readme = readme_file.read()
setup(
    name='quick_parallel',
    version=VERSION,
    url='https://github.com/MAGALA-RICHARD/quick_parallel.git',
    license='MIT',
    author='Richard Magala, Iowa State University, Ames, Iowa, magalarich20@gmail.com, rmagala@iastate.edu',
    author_email='magalarich20@gmail.com',
    description=DESCRIPTION,
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,

    keywords=['python', 'quick parallel', 'worker', 'cores', 'threading', 'parallel processing'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=">=3.4",
    install_requires=[
        'tqdm >= 4.66.2',

    ]
)
