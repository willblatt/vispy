# -*- coding: utf-8 -*-

"""
Tests for PolygonVisual
All images are of size (100,100) to keep a small file size
"""

import numpy as np

from vispy.scene import visuals, transforms
from vispy.testing import (requires_application, assert_image_approved,
                           requires_scipy, TestingCanvas,
                           run_tests_if_main)


@requires_application()
@requires_scipy()
def test_square_draw():
    """Test drawing squares without transforms using PolygonVisual"""
    pos = np.array([[-0.5, 0.5, 0],
                    [0.5, 0.5, 0],
                    [0.5, -0.5, 0],
                    [-0.5, -0.5, 0]])
    with TestingCanvas() as c:
        polygon = visuals.Polygon(pos=pos, color=(1, 0, 0, 1))
        polygon.transform = transforms.STTransform(scale=(50, 50),
                                                   translate=(50, 50))
        c.draw_visual(polygon)
        assert_image_approved("screenshot", 'visuals/square1.png')

        polygon = visuals.Polygon(pos=pos, color=(1, 0, 0, 1),
                                  border_color=(1, 1, 1, 1))
        polygon.transform = transforms.STTransform(scale=(50, 50),
                                                   translate=(50, 50))
        c.draw_visual(polygon)
        assert_image_approved("screenshot", 'visuals/square2.png')

        polygon = visuals.Polygon(pos=pos, border_color=(1, 1, 1, 1))
        polygon.transform = transforms.STTransform(scale=(50, 50),
                                                   translate=(50, 50))
        c.draw_visual(polygon)
        assert_image_approved("screenshot", 'visuals/square3.png',
                              min_corr=0.45)


@requires_application()
@requires_scipy()
def test_rectangle_draw():
    """Test drawing rectangles with transforms using PolygonVisual"""
    pos = np.array([[-0.1, 0.5, 0],
                    [0.1, 0.5, 0],
                    [0.1, -0.5, 0],
                    [-0.1, -0.5, 0]])
    with TestingCanvas() as c:
        polygon = visuals.Polygon(pos=pos, color=(1, 1, 0, 1))
        polygon.transform = transforms.STTransform(scale=(200.0, 25),
                                                   translate=(50, 50))
        c.draw_visual(polygon)
        assert_image_approved("screenshot", 'visuals/rectangle1.png')

        polygon = visuals.Polygon(pos=pos, color=(1, 1, 0, 1),
                                  border_color=(1, 0, 0, 1))
        polygon.transform = transforms.STTransform(scale=(200.0, 25),
                                                   translate=(50, 50))
        c.draw_visual(polygon)
        assert_image_approved("screenshot", 'visuals/rectangle2.png')

        polygon = visuals.Polygon(pos=pos, border_color=(1, 0, 0, 1),
                                  border_width=1)
        polygon.transform = transforms.STTransform(scale=(200.0, 25),
                                                   translate=(50, 49))
        c.draw_visual(polygon)
        assert_image_approved("screenshot", 'visuals/rectangle3.png',
                              min_corr=0.7)


@requires_application()
@requires_scipy()
def test_reactive_draw():
    """Test reactive polygon attributes"""
    pos = np.array([[-0.1, 0.5, 0],
                    [0.1, 0.5, 0],
                    [0.1, -0.5, 0],
                    [-0.1, -0.5, 0]])
    with TestingCanvas() as c:
        polygon = visuals.Polygon(pos=pos, color='yellow')
        polygon.transform = transforms.STTransform(scale=(50, 50),
                                                   translate=(50, 50))
        c.draw_visual(polygon)

        polygon.pos += [0.1, -0.1, 0]
        c.draw_visual(polygon)
        assert_image_approved("screenshot", 'visuals/reactive_polygon1.png')

        polygon.color = 'red'
        c.draw_visual(polygon)
        assert_image_approved("screenshot", 'visuals/reactive_polygon2.png')

        polygon.border_color = 'yellow'
        c.draw_visual(polygon)
        assert_image_approved("screenshot", 'visuals/reactive_polygon3.png',
                              min_corr=0.8)


run_tests_if_main()
