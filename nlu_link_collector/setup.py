# Automatically created by: shub deploy

from setuptools import setup, find_packages

setup(
    name         = 'nlu_link_collector',
    version      = '1.0',
    packages     = find_packages(),
    entry_points = {'scrapy': ['settings = nlu_link_collector.settings']},
    package_data = {
        'nlu_link_collector': ['resources/*.csv']
    },
    zip_safe=False
)
