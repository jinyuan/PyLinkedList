from Entry import Entry


class LinkedList:
    header = None
    size = 0

    def __init__(self):
        self.header = Entry(None, None, None)
        self.header.next = self.header
        self.header.previous = self.header

    def add(self, e):
        return self.add_before(e, self.header)

    def add_before(self, e, entry):
        new_entry = Entry(e, entry, entry.previous)
        new_entry.previous.next = new_entry
        new_entry.next.previous = new_entry
        self.size = self.size + 1
        return

    def get_size(self):
        return self.size

    def get_first(self):
        if self.size != 0:
            return self.header.next.element
        else:
            return None

    def get_last(self):
        if self.size != 0:
            return self.header.previous.element
        else:
            return None

    def remove_first(self):
        if self.size != 0:
            val = self.get_first()
            self.header.next = self.header.next.next
            self.size = self.size - 1
            return val
        else:
            return None

    def remove_last(self):
        if self.size > 0:
            val = self.get_last()
            self.header.previous = self.header.previous.previous
            self.header.previous.next = Entry(None, self.header, self.header.next)
            self.size = self.size - 1
            return val
        else:
            return None

    def to_array(self):
        temp = self.header.next
        arr = []
        while temp.element is not None:
            arr.append(temp.element)
            temp = temp.next
        return arr
