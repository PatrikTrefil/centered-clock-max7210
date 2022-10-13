class monospace_numbers(object):
    """
    Wraps an existing font array, and trims as much
    whitespace as possible while keeping the font monospace
    """

    def __init__(self, font):
        self.font = font
        self.minFirst = min([self._get_first(item) for item in font[48:58]])
        self.maxLast = max([self._get_last(item) for item in font[48:58]])

    def __getitem__(self, ascii_code):
        try:
            bitmap = self.font[ascii_code]
            # Return a slim version of the space character
            if ascii_code == 32:
                return [0] * 4
            else:
                return self._trim(bitmap) + [0]
        except IndexError:
            raise IndexError(f"Font does not have ASCII code: {ascii_code}")

    def _trim(self, arr):
        return arr[self.minFirst:self.maxLast]

    def _get_first(self, arr):
        nonzero = [idx for idx, val in enumerate(arr) if val != 0]
        return nonzero[0]

    def _get_last(self, arr):
        nonzero = [idx for idx, val in enumerate(arr) if val != 0]
        return nonzero[-1] + 1
