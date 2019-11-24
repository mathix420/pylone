from setuptools import setup

setup(
	name='pylone',
	version='0.1',
	description='A Python Serverless framework',
	long_description=open('README.md').read(),
	url='https://github.com/mathix420/pylone',
	author='Arnaud Gissinger',
	author_email='agissing@student.42.fr',
	license='MIT',
	classifiers=[
		'Intended Audience :: Developers',
		'Intended Audience :: System Administrators',

		'Topic :: Software Development :: Build Tools',

		'License :: OSI Approved :: MIT License',

		'Programming Language :: Python :: 3 :: Only'
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		'Programming Language :: Python :: 3.9',
	],
	packages=['src', 'src.utils', 'src.provider'],
	entry_points={'console_scripts': ['pylone=src.__main__:main']},
)