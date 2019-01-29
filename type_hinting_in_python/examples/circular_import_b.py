from circular_import_a import A


class B:
    def get_a(self) -> A:
        return self.a
