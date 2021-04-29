from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name='gslocalize',
    version='1.0',
    description='Localize Xcode projects with Google Sheets',
    license='MIT',
    packages=find_packages(),
    author='OLEKSII SAVCHENKO',
    author_email='nahalem@ukr.net',
    keywords=['xcode', 'localization', 'localizable'],
    url='https://github.com/alexey-savchenko/gslocalize',
    include_package_data=True
)

install_requires = [
    'PyYAML',
    'google-api-python-client',
    'google-auth-httplib2',
    'google-auth-oauthlib'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)