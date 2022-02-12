from controllers import app
from os.path import dirname, basename, isfile, join
import glob
modules = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]


@app.route('/word_finder')
def service_word_finder():
    return 'Word Finder TR service - 200'
