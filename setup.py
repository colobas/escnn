
from setuptools import setup, find_packages

about = {}
with open("escnn/__about__.py") as fp:
    exec(fp.read(), about)

install_requires = [
    'torch',
    'numpy',
    'scipy',
    'lie_learn',
    'joblib',
    'pymanopt',
    'autograd',
    'py3nj'
]


setup_requires = []
tests_require = ['scikit-learn', 'scikit-image']

with open("README.md", 'r', encoding='utf-8') as f:
    long_description = f.read()

download_url = 'https://github.com/QUVA-Lab/escnn/archive/v{}.tar.gz'.format(about['__version__'])

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__summary__'],
    author=about['__author__'],
    author_email=about['__email__'],
    url=about['__url__'],
    download_url=download_url,
    license=about['__license__'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=['test', 'test.*']),
    python_requires='>=3.7',
    keywords=[
        'pytorch',
        'cnn',
        'convolutional-networks'
        'equivariant',
        'isometries',
    ],
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
)
