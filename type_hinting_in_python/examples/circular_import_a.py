from circular_import_b import B


class A:
    def __init__(self, b: B):
        b.a = self
        self.b = b
