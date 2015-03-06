import os
from setuptools import setup
from imp import load_source

crunchy2mkv = load_source("crunchy2mkv", "crunchy2mkv")

def read(fname):
    filename = os.path.join(os.path.dirname(__file__), fname)
    return open(filename).read().replace('#', '')

setup(
    name="crunchy2mkv",
    version=crunchy2mkv.__version__,
    author=crunchy2mkv.__author__,
    author_email=crunchy2mkv.__email__,
    maintainer=crunchy2mkv.__maintainer__,
    maintainer_email=crunchy2mkv.__email__,
    description=("Download .flv videos from Crunchyroll (and maybe other "
                 "sites) and convert them to .mkv."),
    license=crunchy2mkv.__license__,
    url="https://github.com/m45t3r/crunchy2mkv",
    scripts=["crunchy2mkv"],
    platforms=["Linux", "Mac OSX", "Windows"],
    long_description=read("README.rst"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "Environment :: Console",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Multimedia :: Video",
        "Topic :: Utilities",
    ],
)
