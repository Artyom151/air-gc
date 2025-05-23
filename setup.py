from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='air-gc',
    version='0.1.0',
    author='?',
    author_email='?',
    description='Инструмент для проверки портов и SQL-инъекций',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Artyom151/air-gc',
    packages=find_packages(),
    install_requires=[
        'requests>=2.25.1',
        'beautifulsoup4>=4.9.3',
    ],
    entry_points={
        'console_scripts': [
            'air-gc=airgc.cli:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Information Technology',
        'Topic :: Security',
    ],
    python_requires='>=3.6',
)