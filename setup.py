import os
import sys
from setuptools import setup, find_packages
from tethys_apps.app_installation import custom_develop_command, custom_install_command

# -- Apps Definition -- #
app_package = 'get_to_know_brandon'
release_package = 'tethysapp-' + app_package
app_class = 'get_to_know_brandon.app:GetToKnowBrandon'
app_package_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tethysapp', app_package)

# -- Python Dependencies -- #
dependencies = []

setup(
    name=release_package,
    version='0.0.1',
    tags='info,aboutme,nerdalicious',
    description='&quot;Get to know your friendly neighborhood web app developer&quot;',
    long_description='',
    keywords='',
    author='Brandon Roberts',
    author_email='brobs@byu.net',
    url='',
    license='RobCorp95',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['tethysapp', 'tethysapp.' + app_package],
    include_package_data=True,
    zip_safe=False,
    install_requires=dependencies,
    cmdclass={
        'install': custom_install_command(app_package, app_package_dir, dependencies),
        'develop': custom_develop_command(app_package, app_package_dir, dependencies)
    }
)
