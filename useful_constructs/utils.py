"""
this file should contain all the methods that have general use
a collection of methods made for a specific usage should have its own file
"""
from manim import *


def combinePoints(p1: np.array([float]), p2: np.array([float]), t: float):
    return (1 - t) * p1 + t * p2


def get_label(v: Arrow, axes: Axes) -> Matrix:
    end_aux = v.get_end() - axes.coords_to_point(0, 0)
    end = np.array([end_aux[0] / axes.get_x_unit_size(), end_aux[1] / axes.get_y_unit_size(), 0])
    end = np.round(end).astype(int)
    end = end[:2]
    end = end.reshape((2, 1))
    label = Matrix(end)
    label.scale(LARGE_BUFF - 0.2)
    shift_dir = np.array(v.get_end()) - axes.coords_to_point(0, 0)
    if shift_dir[0] >= 0:  # Pointing right
        shift_dir -= label.get_left() + DEFAULT_MOBJECT_TO_MOBJECT_BUFFER * LEFT - axes.coords_to_point(0, 0)
    else:  # Pointing left
        shift_dir -= label.get_right() + DEFAULT_MOBJECT_TO_MOBJECT_BUFFER * RIGHT - axes.coords_to_point(0, 0)
    label.shift(shift_dir)
    label.set_color(YELLOW)
    return label
