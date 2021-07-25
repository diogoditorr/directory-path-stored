class Directory():
    def __init__(self, name: str, path: str):
        self.name = name
        self.path = path

    def __repr__(self):
        return f'<Directory name="{self.name}">'