# http://stackoverflow.com/questions/14354171/add-scrolling-to-a-platformer-in-pygame


def complex_camera(camera, target_rect, half_size):
    HALF_WIDTH, HALF_HEIGHT = half_size
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t, _, _ = -l+HALF_WIDTH, -t+HALF_HEIGHT, w, h  # center player

    l = min(0, l)                            # stop scrolling at the left edge
    l = max(-(camera.width-WIN_WIDTH), l)    # stop scrolling at the right edge
    t = max(-(camera.height-WIN_HEIGHT), t)  # stop scrolling at the bottom
    t = min(0, t)                            # stop scrolling at the top

    return Rect(l, t, w, h)


def simple_camera(camera, target_rect, half_size):
    HALF_WIDTH, HALF_HEIGHT = half_size
    l, t, _, _ = target_rect  # l = left,  t = top
    _, _, w, h = camera       # w = width, h = height
    return Rect(-l+HALF_WIDTH, -t+HALF_HEIGHT, w, h)


class Camera:
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(
            self.state,
            target.rect,
            (width//2, height//2))
