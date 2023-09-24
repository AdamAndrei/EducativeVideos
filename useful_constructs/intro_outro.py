from useful_constructs.utils import *


def generateVertices(x_0, y_0, side, number_of_iterations, t) -> list[list[np.array([float])]]:
    vertices = []
    initial_vertices = [np.array([x_0, y_0, 0]), np.array([x_0 - side, y_0, 0]),
                        np.array([x_0 - side, y_0 + side, 0]), np.array([x_0, y_0 + side, 0])]
    vertices.append(initial_vertices)
    for i in range(number_of_iterations):
        p1 = initial_vertices[0]
        p2 = initial_vertices[1]
        p3 = initial_vertices[2]
        p4 = initial_vertices[3]
        next_vertices = [combinePoints(p1, p2, t), combinePoints(p2, p3, t),
                         combinePoints(p3, p4, t), combinePoints(p4, p1, t)]
        vertices.append(next_vertices)
        initial_vertices = next_vertices

    return vertices


def logo_animations(frame_width, frame_height, text: str):
    square_frame_length = min(frame_width, frame_height)
    x_0 = square_frame_length / 5
    y_0 = - square_frame_length / 5
    side = 2 * square_frame_length / 5
    number_of_iterations = 100
    t = 0.05
    hello_location = np.array([- x_0 / 2, -y_0 * 7 / 10, 0])
    font_size = square_frame_length * 5

    hello = Text(text, color=TEAL, font="Fantasy", font_size=font_size)
    hello.rotate(about_point=hello.get_center(), angle=PI / 6).move_to(hello_location)

    vertices: list[list[np.array([float])]] = generateVertices(x_0, y_0, side, number_of_iterations, t)
    n = len(vertices)
    poly = [Polygon(*vertices[i], stroke_width=2).set_opacity(i / n).set_fill(opacity=0.02) for i in range(n)]
    fade_in_animations = []
    fade_out_animations = []
    for i in range(n):
        fade_in_animations.append(FadeIn(poly[i]))
        fade_out_animations.append(FadeOut(poly[n - 1 - i]))
    return [hello, fade_in_animations, fade_out_animations]


def animate_logo(scene: Scene, text: str):
    frame_width = config["frame_width"]
    frame_height = config["frame_height"]
    logo_anim = logo_animations(frame_width, frame_height, text)
    hello = logo_anim[0]
    anim_in = logo_anim[1]
    anim_out = logo_anim[2]
    scene.play(*[Write(hello, run_time=2.5), LaggedStart(*anim_in, run_time=3)])
    scene.wait(0.5)
    scene.play(*[Unwrite(hello, run_time=1), LaggedStart(*anim_out, run_time=2)])
    scene.wait(0.5)
    scene.clear()
    scene.wait(0.5)


def animate_intro_logo(scene: Scene):
    animate_logo(scene, "Hi there, hello!")


def animate_outro_logo(scene: Scene):
    animate_logo(scene, "Peace 'ut!")
