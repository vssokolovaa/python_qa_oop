class Figure:
    def add_area(self, figure):
        if isinstance(figure, Figure):
            return self.get_area + figure.get_area
        else:
            raise ValueError("ValueError Incorrect class")
