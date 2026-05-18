from ursina import Entity as UrsinaEntity

class Entity(UrsinaEntity):
    '''Расширенный Entity с поддержкой компонентов (Unity-like)'''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.components = {}
    
    def add_component(self, component):
        component_type = type(component)
        self.components[component_type] = component
        component.entity = self
        
    def get_component(self, component_type):
        return self.components.get(component_type)
