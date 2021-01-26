from setuptools import setup
import re

requirements = []
with open('requirements.txt') as f:
	requirements = f.read().splitlines()

version = ''
with open('pluralkit/__init__.py') as f:
	version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
	raise RuntimeError('version is not set')

readme = ''
with open('README.md') as f:
	readme = f.read()

extras_require = {
	'docs': [
		'mkdocs==1.1.2',
		'mkdocs-git-revision-date-plugin==0.3.1',
		'mkdocs-material==6.2.5',
		'mkdocs-material-extensions==1.0.1',
		'pymdown-extensions==8.1'
	]
}

setup(
	name='pluralkit.py',
	author='Johnystar',
	url='https://github.com/Johnystar/pluralkit.py',
	project_urls={
		"Documentation": "https://pluralkit.johnystar.moe/en/latest/",
		"Issue tracker": "https://github.com/Johnystar/pluralkit.py/issues",
	},
	version=version,
	packages=['pluralkit'],
	license='MIT',
	description='A Python wrapper for the PluralKit API',
	long_description=readme,
	long_description_content_type="text/markdown",
	install_requires=requirements,
	extras_require=extras_require,
	python_requires='>=3.5.3',
	classifiers=[
		'Development Status :: 1 - Planning',
		'License :: OSI Approved :: MIT License',
		'Intended Audience :: Developers',
		'Natural Language :: English',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		'Topic :: Internet',
		'Topic :: Software Development :: Libraries',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Topic :: Utilities',
		]
)