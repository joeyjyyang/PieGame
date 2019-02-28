class HitBox:
        def __init__(self, left, top, width, height):
                self.left = left
                self.top = top
                self.width = width
                self.height = height
                self.rectangle = (self.left, self.top, self.width, self.height)
