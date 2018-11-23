import sys
# sys.path.insert(0, '/Users/whitexozu/dev/pycharm_workspace/pythonExample/example/class/lib')

import gameclass1
from lib import gameclass2

instance = gameclass1.character_stat()
instance.print()
instance.set_all( 100, 150)
instance.print()

instance = gameclass2.character_stat()
instance.print()
instance.set_all( 100, 150)
instance.print()
