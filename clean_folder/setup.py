from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1.0.0',
    description='sorting files in the selected folder',
    url='https://github.com/LenuNeya/Home_work_7',
    author='Olena Lysenko',
    author_email='lenuneya@gmail.com',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder = clean_folder.sort_files:processing_sort']}
)