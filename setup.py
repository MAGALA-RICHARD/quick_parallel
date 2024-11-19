from setuptools import setup, find_packages

VERSION = '0.0.1.2'
DESCRIPTION = 'Quick parallel processing library'
LONG_DESCRIPTION = 'Parallelize your function with ease, no need to be a master of parallelization'

# Read the README file for the long description
with open('README.rst', 'r', encoding='utf-8') as readme_file:
    readme = readme_file.read()

setup(
    name='quick_parallel',
    version=VERSION,
    url='https://github.com/MAGALA-RICHARD/quick_parallel',
    license='MIT',
    author='Richard Magala',
    author_email='magalarich20@gmail.com',
    description=DESCRIPTION,
    long_description=readme,
    long_description_content_type='text/x-rst',  # Specify the content type of the long description
    packages=find_packages(),
    include_package_data=True,
    keywords=['python', 'quick parallel', 'worker', 'cores', 'threading', 'parallel processing'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
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
