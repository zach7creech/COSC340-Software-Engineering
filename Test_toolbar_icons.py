"""Test that each image path exists. Images are used for icons.

Since this script tests paths, it needs to be run from the same location as
main_window, which should also contain the images directory that holds each of these images"""

import unittest
import os


class Test_IconsPathExist(unittest.TestCase):
    """Methods are not documented.
    Look at the file name string to see which image is being test"""

    def test_cut_icon(self):
        self.assertTrue(os.path.exists(
            os.path.join('images', 'icons8-cut-80.png')))

    def test_copy_icon(self):
        self.assertTrue(os.path.exists(
            os.path.join('images', 'icons8-copy-80.png')))

    def test_paste_icon(self):
        self.assertTrue(os.path.exists(
            os.path.join('images', 'icons8-paste-80.png')))

    def test_add_image_icon(self):
        self.assertTrue(os.path.exists(
            os.path.join('images', 'icons8-add-image-80.png')))

    def test_search_icon(self):
        self.assertTrue(os.path.exists(
            os.path.join('images', 'icons8-search-80.png')))

    def test_text_color_icon(self):
        self.assertTrue(os.path.exists(
            os.path.join('images', 'icons8-text-color-80.png')))

    def test_highlight_icon(self):
        self.assertTrue(os.path.exists(
            os.path.join('images', 'icons8-marker-pen-80.png')))

    def test_bold_icon(self):
        self.assertTrue(os.path.exists(
            os.path.join('images', 'icons8-bold-80.png')))

    def test_italic_icon(self):
        self.assertTrue(os.path.exists(
            os.path.join('images', 'icons8-italic-80.png')))

    def test_bullet_icon(self):
        self.assertTrue(os.path.exists(
            os.path.join('images', 'icons8-bulleted-list-80.png')))

    def test_numbered_icon(self):
        self.assertTrue(os.path.exists(
            os.path.join('images', 'icons8-numbered-list-80.png')))

    def test_aln_left_icon(self):
        self.assertTrue(os.path.exists(
            os.path.join('images', 'icons8-align-left-80.png')))

    def test_aln_center_icon(self):
        self.assertTrue(os.path.exists(
            os.path.join('images', 'icons8-align-center-80.png')))

    def test_aln_right_icon(self):
        self.assertTrue(os.path.exists(
            os.path.join('images', 'icons8-align-right-80.png')))

    def test_aln_justify_icon(self):
        self.assertTrue(os.path.exists(
            os.path.join('images', 'icons8-align-justify-80.png')))

    def test_add_group_icon(self):
        self.assertTrue(os.path.exists(os.path.join(
            'images', 'icons8-add-user-group-man-man-80.png')))

    def test_add_user_icon(self):
        self.assertTrue(os.path.exists(os.path.join(
            'images', 'icons8-add-user-male-80.png')))

    def test_app_icon(self):
        self.assertTrue(os.path.exists(
            os.path.join('images', 'icons8-note-64.png')))
