import os
import coffeafrag

pjoin = os.path.join

# This function takes as input any path (inside of coffeafrag/coffeafrag), and returns the absolute path
def coffeafrag_path(path_in_repo):
    return pjoin(coffeafrag.__path__[0], path_in_repo)
