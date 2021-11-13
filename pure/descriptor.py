class casemethod(object):

    def __init__(self, func):
        self.__func__ = func

    def __get__(self, instance, cls=None):
        if instance is None:
            if cls is None:
                raise TypeError('__get__(None, None) is invalid')
            return classmethod(self.__func__).__get__(instance, cls)
        return self.__func__.__get__(instance, cls)


class DescriptorExample(object):

    def __init__(self, name=None):
        self.name = name

    def __set__(self, instance, value):
        setattr(instance, '__' + str(self.name), value)
        print("Call __set__")

    def __get__(self, instance, owner=None):
        print("Call __get__")
        return getattr(instance, '__' + str(self.name))

    def __delete__(self, instance):
        delattr(instance, '__' + str(self.name))
        print("Call __delete__")


class SimpleClass(object):

    attr1 = DescriptorExample('1')
    attr2 = DescriptorExample('2')

    __c = 10


if __name__ == '__main__':

    a = SimpleClass()
    b = SimpleClass()

    a.attr1 = 10
    a.attr2 = 20
    b.attr1 = 30
    b.attr2 = 40

    print(a.attr1, a.attr2, b.attr1, b.attr2)

    del a.attr1
    try:
        a.attr1
    except AttributeError as e:
        print("Handled AttributeError:", e)

    a.attr1 = 10
    print(a._SimpleClass__c)
