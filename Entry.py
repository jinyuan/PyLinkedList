class Entry:

    next = None
    previous = None
    element = None

    def __init__(self, e, next, previous):
        self.element = e
        self.next = next
        self.previous = previous
