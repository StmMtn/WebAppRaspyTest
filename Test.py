from samplebase import SampleBase

class RotatingBlockGenerator(SampleBase):

    def __init__(self, x,y):
        super(RotatingBlockGenerator, self).__init__(32, 32)
    def run(self):
        offset_canvas.SetPixel(1, 1, 0, 255, 0)
        offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
        
if __name__ == "__main__":
    rotating_block_generator = RotatingBlockGenerator(x=32,y=32)