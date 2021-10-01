from setuptools import setup, find_namespace_packages

setup(
    name='pylone',
    version='0.2.0',
    description='A Python Serverless framework',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mathix420/pylone',
    author='Arnaud Gissinger',
    author_email='agissing@student.42.fr',
    license='MIT',
    python_requires='>=3.6',
    classifiers=[
                'Intended Audience :: Developers',
                'Intended Audience :: System Administrators',

                'Topic :: Software Development :: Build Tools',

                'License :: OSI Approved :: MIT License',

                'Programming Language :: Python :: 3 :: Only',
                'Programming Language :: Python :: 3.6',
                'Programming Language :: Python :: 3.7',
                'Programming Language :: Python :: 3.8',
                'Programming Language :: Python :: 3.9',
    ],
    install_requires=[
        'python-dotenv==0.10.5',
        'PyInquirer==1.0.3',
        'PyYAML>=3.13',
        'boto3>=1.11.6',
    ],
    packages=find_namespace_packages(include=["pylone", "pylone.*"]),
    entry_points={'console_scripts': ['pylone=pylone.__main__:main']},
)
