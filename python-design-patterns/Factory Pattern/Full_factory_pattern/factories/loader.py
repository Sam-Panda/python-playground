from importlib import import_module
from inspect import getmembers, isabstract, isclass
from .abstract_factories import AbstractFactory

def load_factory(factory_name):
    try:
        factory_module = import_module('.' + factory_name, 'factories')
        print(f"Loaded module {factory_module}")
    except ImportError as e:
        factory_module = import_module('.null_factory', 'factories')
    
    classes = getmembers(factory_module, lambda m: isclass(m) and not isabstract(m))

    for name, _type in classes:
        if isclass(_type) and issubclass(_type, AbstractFactory):
            return _type()
    