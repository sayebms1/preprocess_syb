import setuptools

with open('README.md', 'r') as file:
    long_description = file.read() # the redme description will directly come here



setuptools.setup(
    name = 'preprocess_syb', # this should be unique and its the name of the pytho pakcage
    include_package_data=True,
    version = '0.1.11',
    author = 'Mohammad Sayeb',
    author_email = 'sayebms@gmail.com' ,
    description = 'This is a pre-processing package',
    long_description=long_description,
    long_description_content_type = 'text/markdown', # its a markdown file
    packages = setuptools.find_packages(), # find the directory of the package autmatically
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'],
    python_requires = '>=3.5'
)
