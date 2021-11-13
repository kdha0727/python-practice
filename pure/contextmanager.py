
class MyContextManager(object):

    def __init__(self, thing=None, close=False):
        self.thing = thing
        self.close = close

    def __enter__(self):
        return self.thing

    def __exit__(self, *exc_info):
        if self.close and self.thing is not None:
            self.thing.close()


if __name__ == '__main__':
    with MyContextManager() as p:
        print(p)
