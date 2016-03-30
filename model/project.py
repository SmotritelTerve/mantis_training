from sys import maxsize


class Project:

    def __init__(self, name=None, description=None, id=None):
        self.name = name
        self.description = description
        self.id = id

    def __repr__(self):
        return '%s%s%s' % (self.name, self.id, self.description)

    def __eq__(self, other):
        return self.name == other.name and (self.id is None or other.id is None or self.id == other.id)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
