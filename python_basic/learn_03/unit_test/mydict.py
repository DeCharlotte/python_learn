# 编写一个Dict类，这个类的行为和dict一致，但是可以通过属性来访问


class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):  # # 仅在访问不存在的属性时调用
        try:
            return self[key]
        except KeyError:
            raise AttributeError(f"'Dict' object has no attribute '{key}'")

    def __setattr__(self, key, value):  # # 控制属性赋值
        self[key] = value


