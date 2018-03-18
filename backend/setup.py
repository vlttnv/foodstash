from setuptools import setup, find_packages

setup(
    name='foodstash',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'flask_sqlalchemy',
        'flask-migrate'
    ],
    # setup_requires=[
    #     'pytest-runner',
    # ],
    # tests_require=[
    #     'pytest',
    # ],
)