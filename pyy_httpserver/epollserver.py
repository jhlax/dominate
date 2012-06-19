__license__ = '''
This file is part of pyy.

pyy is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as
published by the Free Software Foundation, either version 3 of
the License, or (at your option) any later version.

pyy is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General
Public License along with pyy.  If not, see
<http://www.gnu.org/licenses/>.
'''

'''

This module uses epoll to implement stackless asynchronous IO.

when a blocking read() or write() call to an fd is made in a tasklet,
the fd will be regisered with an epoll set and stackless.schedule()
will be called to execute other tasklets while waiting.

When data is available (or can be written), the tasklet is woken up.


'''


import stackless
import socket
import select
import threading
import time

