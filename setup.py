from distutils.core import setup
import glob,re, os



def get_version():
  """
  Gets version from script file
  """
  buffer = open('scripts/make_connect_copy').read()
  match = re.search("VERSION\s+=\s+'(.*)'", buffer)
  return match.group(1)
  
setup(name='connect-copy',
      version=get_version(),
      description='Package for connect-copy and associated scripts',
      author='Suchandra Thapa',
      author_email='sthapa@ci.uchicago.edu',
      scripts=['scripts/make_connect_copy'],
      data_files=[('share/connect-copy', ['scripts/connect_copy'])]
      )

