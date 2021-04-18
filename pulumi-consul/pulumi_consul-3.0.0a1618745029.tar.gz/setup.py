# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import errno
from setuptools import setup, find_packages
from setuptools.command.install import install
from subprocess import check_call


class InstallPluginCommand(install):
    def run(self):
        install.run(self)
        try:
            check_call(['pulumi', 'plugin', 'install', 'resource', 'consul', '3.0.0-alpha.1618745029+fb08aa98'])
        except OSError as error:
            if error.errno == errno.ENOENT:
                print("""
                There was an error installing the consul resource provider plugin.
                It looks like `pulumi` is not installed on your system.
                Please visit https://pulumi.com/ to install the Pulumi CLI.
                You may try manually installing the plugin by running
                `pulumi plugin install resource consul 3.0.0-alpha.1618745029+fb08aa98`
                """)
            else:
                raise


def readme():
    with open('README.md', encoding='utf-8') as f:
        return f.read()


setup(name='pulumi_consul',
      version='3.0.0a1618745029',
      description="A Pulumi package for creating and managing consul resources.",
      long_description=readme(),
      long_description_content_type='text/markdown',
      cmdclass={
          'install': InstallPluginCommand,
      },
      keywords='pulumi consul',
      url='https://pulumi.io',
      project_urls={
          'Repository': 'https://github.com/pulumi/pulumi-consul'
      },
      license='Apache-2.0',
      packages=find_packages(),
      package_data={
          'pulumi_consul': [
              'py.typed',
          ]
      },
      install_requires=[
          'parver>=0.2.1',
          'pulumi>=3.0.0a1,<4.0.0',
          'semver>=2.8.1'
      ],
      zip_safe=False)
