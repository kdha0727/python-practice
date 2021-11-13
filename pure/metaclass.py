# Class dynamic creation by using type
JustClass = type('SimpleClass', (), {})
print(JustClass)  # <class '__main__.SimpleClass'>
print(JustClass())  # <__main__.Hello object at 0x00000000>


def replace(self, old, new):
    while old in self:
        self[self.index(old)] = new


_bases = (list, )
_namespace = {'desc': 'advanced list', 'replace': replace}
AdvancedList = type('AdvancedList', _bases, _namespace)

x = AdvancedList([1, 2, 3, 1, 2, 3])
x.replace(1, 100)
print(x, x.desc)


# Inheriting type

class MakeClass(type):
    def __new__(mcs, name, bases, namespace):
        """
        :param name: class name
        :param bases: base class list (or tuple)
        :param namespace: additional namespace dict
        """
        new = super().__new__(mcs, name, bases, namespace)
        return new


Cls = MakeClass('Cls', (), {})
obj = Cls()


# Singleton
class Singleton(type):
    __instances = {}

    def __new__(mcs, name, bases, namespace):
        print('Singleton.__new__ called')
        return super().__new__(mcs, name, bases, namespace)

    def __call__(cls, *args, **kwargs):  # First called in Hello()
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__call__(*args, **kwargs)  # Calls Hello.__init__
        return cls.__instances[cls]

    @staticmethod
    def yang():
        return 11111


class Greeting(metaclass=Singleton):

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.args = args
        self.kwargs = kwargs


class Hello(Greeting):
    pass


print(Hello.yang())
# print(Hello().yang())  # Error
a = Hello(1, 2, 3)
b = Hello()
print(a is b)
