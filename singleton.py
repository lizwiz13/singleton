'implementation of single-instance classes'

# black magic
class Singleton(type):
    instances = {}

    def __call__(cls, *args, **kwargs):
        try:
            return cls.instances[cls]
        except KeyError as ke:
            if cls not in cls.instances:
                instance = super(Singleton, cls).__call__(*args, **kwargs)
                cls.instances[cls] = instance
                return instance
            raise ke
        
    # does not work
    """
    def __del__(cls):
        if cls in cls.instances:
            del cls.instances[cls]
    """


# decorator variant - kinda buggy
def singleton(cls):
    cls._instance=None
    oldnew = cls.__new__
    oldinit = cls.__init__

    def new(_cls, *args, **kwargs):
        if _cls._instance is not None:
            return _cls._instance
        return oldnew(_cls)
    
    def init(self, *args, **kwargs):
        if cls._instance is not None:
            return
        oldinit(self, *args, **kwargs)
        cls._instance = self 

    cls.__new__ = new
    cls.__init__ = init

    return cls


