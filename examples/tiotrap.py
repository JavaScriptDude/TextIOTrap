#########################################
# .: tiotrap.py :.
# Python Helpers For Capturing TextIO Streams 
# .: Other :.
# Author: Timothy C. Quinn
# Home: https://github.com/JavaScriptDude/tiotrap
# Licence: https://opensource.org/licenses/BSD-3-Clause
#########################################

class TextIOTrap():
    name=None
    buffer=None
    encoding=None
    errors=None
    newlines=None
    line_buffering=None
    def __init__(self, **args):
        self.write_handler = args.get('write_handler', None)
        self.name = args.get('name', '-')
        self.encoding = args.get('name', 'utf-8')
        self.store = args.get('store', False)
        if self.store: self._entries = []
    def close(self):pass
    def detach(self): pass
    def fileno(self):return 0
    def flush(self):pass
    def isatty(self):return False
    def read(self, n=None): return ''
    def readable(self):return False
    def readline(self, limit=-1):pass
    def readlines(self, hint=-1):return []
    def seek(self, offset, whence=0): pass
    def seekable(self): return False
    def tell(self): return 0
    def truncate(self, size=None): pass
    def writable(self): return True
    def write(self, s):
        if len(s) > 0:
            s = s.decode(self.encoding) if isinstance(s, bytes) else s
            if self.write_handler: 
                self.write_handler(s)
            elif self.store:
                self._entries.append(s)
        return 0
    def writelines(self, lines):
        if isinstance(lines, list):
            for s in lines: self.write(s)
    def entries(self, rstrip:bool=True): 
        if not self.store: return None
        s = "".join(self._entries)
        return s.rstrip() if rstrip else s
    def __iter__(self):
        return iter(self._entries if self.store else [])


DEVNULL = TextIOTrap()