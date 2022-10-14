from os.path import abspath, dirname, join

from setuptools import find_packages, setup

install_reqs = [req for req in
                open(abspath(join(dirname(__file__), 'requirements.txt')))]

setup(
        name='m3u8-To-MP4',
        version="0.1.10",
        description="Python downloader for saving m3u8 video to local MP4 file.",
        author='songs18',
        author_email='songhaohao2018@cqu.edu.cn',
        license='MIT',
        packages=find_packages(),
        platforms=['all'],
        url="https://github.com/songs18/m3u8_To_MP4",
        zip_safe=False,
        include_package_data=True,
        install_requires=install_reqs,
        python_requires='>=3.7'
)
