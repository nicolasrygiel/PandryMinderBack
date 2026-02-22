# import os
# import pkgutil
# import importlib

# # Spécifiez le nom du module de base
# module_name = 'pdm.models'

# # Importer tous les modules de modèle
# for importer, modname, is_pkg in pkgutil.walk_packages([os.path.dirname(__file__)], module_name + '.'):
#     importlib.import_module(modname)

# # Maintenant, vous pouvez accéder à chaque modèle directement
# from .base_model import BaseModel