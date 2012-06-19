from pyy_httpserver import *
from subprocess      import *

def filter(cmd, data, shell=False):
  p = Popen([cmd], stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=shell)
  out,err = p.communicate(data)
  if err and not out:
    raise Exception("Error running command '%s':\n%s" % (cmd,err))
  return out

class filterserver(fileserver):
  MIME = dict(fileserver.MIME)
  MIME.update({
    'sass': 'text/css',
    'md':   'text/html',
    'haml': 'text/html',
  })
  def write_file(self, conn, req, res, path, *args):
    fsize = os.path.getsize(path)
    f = file(path, 'rb')
    ft = f #threadio.threadio(f)
    res.body = self.filter(path, ft.read())
    ft.close()
    return
    
    
  def filter(self, path, data):
    if path.endswith('.sass'):
      data = filter('sass --no-cache',  data, shell=True)    
    if path.endswith('.haml'):
      data = filter('haml',             data, shell=True)
    if path.endswith('.md'):
      data = filter('Markdown.pl',      data, shell=True)
    return data
    
