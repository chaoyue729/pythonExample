# import gameclass1
# import lib.gameclass2
import sys
sys.path.insert(0, '/Users/whitexozu/dev/pycharm_workspace/pythonExample/example/class/lib')

import gameclass2

instance = gameclass1.character_stat()
# instance = gameclass2.character_stat()
instance.set_all( 100, 150)
instance.print()
