# Copyright (c) 2014 King's College London
# Created by the Software Development Team <http://soft-dev.org/>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

import helper

class PHP(helper.Generic):
    def language_box(self, name, node):
        if name == "<Python + PHP>":
            buf = Python().pp(node)
            self.buf.append("embed_py_func(\"%s\")" % (_escapepy(buf)))

class Python(helper.Generic):
    def language_box(self, name, node):
        if name == "<PHP + Python>":
            buf = PHP().pp(node)
            self.buf.append("embed_php_func(\"\"\"\n%s\n\"\"\")" % (_escape(buf)))

def _escapepy(s):
    return s.replace("\\", "\\\\").replace("\"", "\\\"").replace("'", "\\'").replace("\n", "\\n").replace("$", "\$")

def _escape(s):
    return s.replace("\\", "\\\\").replace("\"", "\\\"").replace("'", "\\'")

def export(node):
    return "<?php\n%s\n?>" % (PHP().pp(node),)
