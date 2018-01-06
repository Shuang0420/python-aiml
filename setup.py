'''
Build the python-aiml Py2/Py3 Chinese version package
'''

from setuptools import setup
import glob

from aiml.constants import VERSION

#package_prefix = "Lib/site-packages/aiml"


setup_args = dict( name="aiml",
    version=VERSION,
    author="Shuang0420",
    author_email="sxu1@alumni.cmu.edu",
    
    description="An interpreter package for AIML, the Artificial Intelligence Markup Language",
    long_description="""aiml implements an interpreter for AIML, the Artificial Intelligence
Markup Language developed by Dr. Richard Wallace of the A.L.I.C.E. Foundation.
It can be used to implement a conversational AI program.

Forked from python-aiml 0.9.1 (https://github.com/paulovn/python-aiml) 
""",
    url="https://github.com/Shuang0420/aiml.git",
    platforms=["any"],
    classifiers=["Development Status :: 4 - Beta",
                 "Environment :: Console",
                 "Intended Audience :: Developers",
                 "Programming Language :: Python",
                 "Programming Language :: Python :: 2.7",
                 "Programming Language :: Python :: 3",
                 "Programming Language :: Python :: 3.4",
                 "Programming Language :: Python :: 3.5",
                 "Programming Language :: Python :: 3.6",
                 "License :: OSI Approved :: BSD License",
                 "Operating System :: OS Independent",
                 "Topic :: Communications :: Chat",
                 "Topic :: Scientific/Engineering :: Artificial Intelligence"
                 ],
 
    install_requires = [ 'setuptools',
    ],

    packages=[ "aiml", 'aiml.script' ],
#    package_dir = { 'aiml': 'aiml',
#                    'aiml.script' : 'aiml/script' },

    include_package_data = False,       # otherwise package_data is not used
    package_data={ 'aiml': ['botdata/standard/*.aiml',
                            'botdata/standard/*.xml',
                            'botdata/alice/*.aiml',
                            'botdata/alice/*.xml',
                            ]},

    entry_points = { 'console_scripts': [
        'aiml-validate = aiml.script.aimlvalidate:main',
        'aiml-bot = aiml.script.bot:main',
    ]},

    test_suite = 'test.__main__.load_tests',

#    data_files=[
#        (package_prefix, glob.glob("aiml/self-test.aiml")),
#        (package_prefix, glob.glob("*.txt")),
#    ],
)

if __name__ == '__main__':
    setup( **setup_args )
