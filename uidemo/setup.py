from setuptools import setup, find_packages
setup(
    name = "UIDemo",
    version = "0.1",
    packages = find_packages(),
    scripts=['MainUi.py'],
    install_requires=['PyQt5>=5.11.3','QtAwesome>=1.6.0'],
    package_data={
            '': ['*.jpg'],
            'uidemo': ['data/*.jpg'],
    },
    author = "chamu",
    author_email = "393829394@qq.com",
    description = "PyQt5图形界面布局包",
    keywords = "PyQt5",
)
