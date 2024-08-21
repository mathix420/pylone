from setuptools import setup, find_namespace_packages

setup(
    name='pylone',
    version='1.0.1',
    description='A Python Serverless framework',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mathix420/pylone',
    author='Arnaud Gissinger',
    author_email='agissing@student.42.fr',
    license='MIT',
    python_requires='>=3.8',
    classifiers=[
                'Intended Audience :: Developers',
                'Intended Audience :: System Administrators',

                'Topic :: Software Development :: Build Tools',

                'License :: OSI Approved :: MIT License',

                'Programming Language :: Python :: 3 :: Only',
                'Programming Language :: Python :: 3.9',
                'Programming Language :: Python :: 3.10',
                'Programming Language :: Python :: 3.11',
                'Programming Language :: Python :: 3.12',
    ],
    install_requires=[
        'python-dotenv>=1.0.1',
        'InquirerLib>=0.0.2',
        'requests>=2.32.3',
        'boto3>=1.35.2',
        'PyYAML>=6.0.2',
    ],
    packages=find_namespace_packages(include=["pylone", "pylone.*"]),
    entry_points={'console_scripts': ['pylone=pylone.__main__:main']},
)
