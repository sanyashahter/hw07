from setuptools import setup, find_namespace_packages

setup(
    name='my_project',
    version='0.0.1',
    description='cleaner for folders',
    author='sanya',
    author_email='sanyashahter870@gmail.com',
    url='https://sanyashahter.github.io/go_it_hw06/',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points = {'console_script': ['clean-folder=clean_folder.clean:run']}
)
                                