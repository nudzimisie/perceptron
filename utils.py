from importlib import import_module as get_module

class PolymorphicClass:
    
    def __init__(self, core):
        self.core = core

    @staticmethod
    def get_object(_class, *args, **kwargs):
        try:
            new_object = _class(*args, **kwargs)
        except Exception as e:
            print(e)
            new_object = _class()
        finally:
            return new_object

    def __call__(self, source, *args, **kwargs):
        polymorphic_class_name = f'{self.core.__name__}From{source.__class__.__name__.title()}'
        try:
            polymorphic_class = getattr(get_module(self.core.__module__), polymorphic_class_name)
        except Exception as e:
            print(e)
            polymorphic_class = self.core
        finally:
            return self.get_object(polymorphic_class, source, *args, **kwargs)