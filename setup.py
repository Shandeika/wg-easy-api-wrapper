from setuptools import setup

setup(
    name='wg-easy-api-wrapper',
    version='1.0.0',
    packages=['wg_easy_api_wrapper'],
    url='https://github.com/Shandeika/wg-easy-api-wrapper',
    license='GNU General Public License v3.0',
    author='MrShandy',
    author_email='mrshandy@shandy-dev.ru',
    description='Wrapper for wg-easy API',
    install_requires=[
        'aiohttp~=3.8.4'
    ],
)
