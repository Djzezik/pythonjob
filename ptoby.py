import simple_draw as sd
circle (center_position, radius=50, color=COLOR_YELLOW, width=1):
def bubble (point, step, color_):
    radius = 50
    for _ in range(3):
        radius +=step
        sd.circle(center_position=point, radius=radius, width=2, color=color_)


for _ in range(100):
    point = sd.random_point()
    bubble(point=point, step=5)