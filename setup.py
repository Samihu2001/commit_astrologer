from setuptools import setup, find_packages

setup(
    name='commit-astrologer',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'commit-astrologer=commit_astrologer.cli:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A humorous CLI tool for analyzing commit messages astrologically.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='[Your Repository URL]',
    license='[Your License Name]',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: [Your License Name]',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)