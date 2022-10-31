from setuptools import setup

with open("README.md") as file:
	big_descr = file.read()

setup(name='templus',
      description='library for reading and receiving messages from https://tempmail.plus/ru/#!',
      version = "1.1",
      long_description = big_descr,
      long_description_content_type="text/markdown",
      url = "https://github.com/BitterTruth1/templus",
      author_email='bonnita1900432@gmail.com')
