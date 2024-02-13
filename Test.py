from samplebase import SampleBase

class RotatingBlockGenerator(SampleBase):
    def run(self):
        offset_canvas.SetPixel(1, 1, 0, 255, 0)
        offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
        
if __name__ == "__main__":
    rotating_block_generator = RotatingBlockGenerator()
    rotating_block_generator.run