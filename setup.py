from setuptools import setup, find_packages

setup(name='gomoku-ui',
      version='0.5',
      url='https://github.com/LouisCaixuran/gomoku-ui',
      license='Apache',
      author='Louis Caixuran',
      author_email='louiscaixuran@163.com',
      description='Use Monte Carlo/AI/... method to play gomoku',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      zip_safe=False,
      include_package_data = True,      

      entry_points={
          'console_scripts':[
	    'play-go-web = gomoku_ui.manage:main',
              ]
      }
)
