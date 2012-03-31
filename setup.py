"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['run.py']
DATA_FILES = [
# 'webbox.icns', # assigned as icon of app in options
 'html',
 'data',
 'rww',
 '4store',
 'initial_setup.py',
 'config2env.py',
 'webbox.json.default',
 'scripts',

 # don't really need these to run, but nice to include them
 'setup_env.sh',
 'COPYING',
 'tests',
 'README.md',
 ]

OPTIONS = {
    'iconfile': 'webbox.icns',
    'argv_emulation': True,
    'includes': # all external modules, taken from generate_includes.py
        ['querycache', 'cStringIO', 'traceback', 'cherrypy', 'SimpleHTTPServer', 'subscriptions', 'cherrypy.lib.encoding', 'cherrypy.wsgiserver', 'rdfcrypto', 'webbox', 'BaseHTTPServer', 'shutil', 'hashlib', 'lxml.builder', 'cherrypy.wsgiserver.ssl_builtin', 'lxml', 'uuid', 'webboxhandler', 'base64', 'OpenSSL', 'urllib', 'securestore', 're', 'json', 'rdflib', 'fourstore', 'time', 'sqlite3', 'ConfigParser', 'SocketServer', 'glob', 'mimetypes', 'setuptools', 'httputils', 'journal', 'diskstore', 'urllib2', 'sys', 'certificates', 'M2Crypto', 'sparqlresults', 'webboxx509', 'pickle', 'Crypto.Cipher', 'os.path', 'posixpath', 'hashstorage', 'httplib', 'logging', 'socket', 'cElementTree', 'vaults', 'journalmodule', 'sparqlparse', 'urlparse', 'securestorewsgi', 'shelve', 'securestoreproxy', 'os', 'rdflib.graph', 'lxml._elementpath', 'autobahn', 'twisted'],
    }

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
