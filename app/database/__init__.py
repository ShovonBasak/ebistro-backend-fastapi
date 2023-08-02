import importlib
import os


def load_all_models(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file == 'models.py':
                models_file_path = os.path.join(root, file)
                package_name = os.path.relpath(root, start=directory).replace(os.path.sep, '.')
                module_name = f"{package_name}.models"

                spec = importlib.util.spec_from_file_location(module_name, models_file_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

load_all_models('app/api')
