class Base(object):
    @classmethod
    def make(cls, *args, **kwargs):
        print("Base.make(%s, %s) start" % (args, kwargs))
        print("Base.make end")


class Foo(Base):
    @classmethod
    def make(cls, *args, **kwargs):
        print("Foo.make(%s, %s) start" % (args, kwargs))
        super(Foo, cls).make(*args, **kwargs)
        print("Foo.make end")


class Bar(Base):
    @classmethod
    def make(cls, *args, **kwargs):
        print("Bar.make(%s, %s) start" % (args, kwargs))
        super(Bar, cls).make(*args, **kwargs)
        print("Bar.make end")


class FooBar(Foo,Bar):
    @classmethod
    def make(cls, *args, **kwargs):
        print("FooBar.make(%s, %s) start" % (args, kwargs))
        super(FooBar, cls).make(*args, **kwargs)
        print("FooBar.make end")


FooBar.make(1, 2, c=3)
