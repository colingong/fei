from setuptools import setup

setup(name='fei',
      version='0.1',
      description="My django demo",
      long_description="",
      author='Fei',
      author_email='vxfs@qq.com',
      license='TODO',
      packages=['fei'],
      zip_safe=False,
      install_requires=[
          'Django',
          # 'Sphinx',
          # ^^^ Not sure if this is needed on readthedocs.org
          # 'something else?',
          ],
      )