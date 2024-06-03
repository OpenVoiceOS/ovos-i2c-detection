import os
from setuptools import setup

BASEDIR = os.path.abspath(os.path.dirname(__file__))


def get_version():
    """ Find the version of the package"""
    version = None
    version_file = os.path.join(BASEDIR, 'version.py')
    major, minor, build, alpha, post = (None, None, None, None, None)
    with open(version_file) as f:
        for line in f:
            if 'VERSION_MAJOR' in line:
                major = line.split('=')[1].strip()
            elif 'VERSION_MINOR' in line:
                minor = line.split('=')[1].strip()
            elif 'VERSION_BUILD' in line:
                build = line.split('=')[1].strip()
            elif 'VERSION_ALPHA' in line:
                alpha = line.split('=')[1].strip()
            elif 'VERSION_POST' in line:
                post = line.split('=')[1].strip()

            if ((major and minor and build and alpha) or
                    '# END_VERSION_BLOCK' in line):
                break
    version = f"{major}.{minor}.{build}"
    if alpha and int(alpha) > 0:
        version += f"a{alpha}"
    elif post and int(post) > 0:
        version += f"post{post}"
    return version


with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='ovos_i2c_detection',
    version=get_version(),
    url='https://github.com/OpenVoiceOS/ovos_i2c_detection',
    license='MIT',
    author='builderjer',
    author_email='builderjer@gmail.com',
    description='i2c detection for some devices',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['ovos_i2c_detection'],
)