def setup():
    size(600, 600)
    background(255)
    noStroke()
    fill(0)
    draw_fractal(300, 500, 200, 0)
def draw_fractal(x, y, size, angle):
    if size < 1:
        return
    x1 = x - size / 2
    y1 = y - size / 2
    x2 = x + size / 2
    y2 = y + size / 2
    x3 = x - size / 2
    y3 = y + size / 2
    x4 = x + size / 2
    y4 = y - size / 2
    quad(x1, y1, x, y3, x2, y2, x3, y)
    draw_fractal(x1, y1, size / 2, angle + 45)
    draw_fractal(x2, y2, size / 2, angle + 135)
    draw_fractal(x3, y3, size / 2, angle + 225)
    draw_fractal(x4, y4, size / 2, angle + 315)
if __name__ == "__main__":
    run()
