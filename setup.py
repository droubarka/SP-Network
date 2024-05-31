from setuptools import setup, find_packages

with open("README.md", 'r') as file:
	long_description = file.read()

setup(
	name="spnetwork",
	version='0.0.10',
	description="SP-Network",
	long_description=long_description,
	long_description_content_type="text/markdown",
	author="Mohamed A. Oubarka",
	author_email="droubarka@gmail.com",
	url="https://github.com/droubarka/sp-network",
	license="",
	packages=find_packages(),
	python_requires=">=3.8",
)
