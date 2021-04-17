import setuptools

setuptools.setup(name='Crystally',
                 version='0.2.3',
                 description='Python module to model and analyze crystal structures',
                 url='https://git.rwth-aachen.de/john.arnold/Crystally.git',
                 author='John Arnold',
                 author_email='arnold@pc.rwth-aachen.de',
                 license='None',
                 packages=setuptools.find_packages(),
                 package_dir={'crystally': 'crystally'},
                 install_requires=['numpy'])
