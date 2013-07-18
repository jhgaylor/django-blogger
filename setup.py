import os
#from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name = "django-blogger",
    version = "1.0.0.6",
    author = "Jake Gaylor",
    author_email = "jake@codegur.us",
    description = "A package to administer a simple blog via Django.",
    url = "https://github.com/jhgaylor/django-blogger/",
    dependancy_links = ['https://github.com/yedpodtrzitko/django-taggit.git#egg=django-taggit-0.9.3'],
    install_requires = [ln for ln in open('requirements.txt')],
    packages = find_packages(), 
    #package_data=package_data,
    include_package_data = True,
)