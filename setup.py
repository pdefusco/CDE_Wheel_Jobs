from setuptools import setup, find_packages

import mywheel

setup(
  name='mywheel',
  version=mywheel.__version__,
  author=mywheel.__author__,
  url='https://docs.cloudera.com/data-engineering/cloud/overview/topics/cde-service-overview.html',
  author_email='paul@cloudera.com',
  description='my wheel',
  packages=find_packages(include=['mywheel']),
  entry_points={
    'group_1': 'run=mywheel.__main__:main'
  },
  install_requires=[
    'setuptools'
  ]
)
