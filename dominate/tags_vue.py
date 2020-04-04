# author: jhlax <John Harrington: jhlax95@outlook.com>

from .tags import html_tag, div

"""
notes
=====

implementing a smart vue HTML generator with dominate. possible automated js
linking and organization, referencing, etc.

step 1
------

implement a simple vue app that works in sandbox.
"""


class vue_app(div):
    """
    Represents a div element with id of the first keyward argument being
    the name of the app.
    """
