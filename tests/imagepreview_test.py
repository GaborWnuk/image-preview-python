# -*- coding: utf-8 -*-

"""
    imagepreview_test.py
    ~~~~~~~~~~~

    Unit tests for imagepreview package.

    :copyright: (c) 2016 by GaborWnuk.
    :license: see LICENSE for more details.
"""

import os
import sys
import unittest

path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, path + '/../')

from imagepreview import ImagePreview

class ImagePreviewTest(unittest.TestCase):
    def test_image_bytes_open(self):
        file_bytes = open("%s/assets/emerald.jpg" % path, "rb")
        ip = ImagePreview(file_path_or_bytes=file_bytes)

    def test_image_bytes_attribute_error(self):
        with self.assertRaises(AttributeError):
            ip = ImagePreview(file_path_or_bytes=0)

    def test_image_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            ip = ImagePreview(file_path_or_bytes="Nonexistent file")

    def test_image_bytes_not_image(self):
        with self.assertRaises(OSError):
            file_bytes = open("%s/assets/bytes.bin" % path, "rb")
            ip = ImagePreview(file_path_or_bytes=file_bytes)

    def test_image_header_length(self):
        file_bytes = open("%s/assets/emerald.jpg" % path, "rb")
        ip = ImagePreview(file_path_or_bytes=file_bytes)

        self.assertEqual(len(ip.thumbnail_header_bytes()), 620)

    def test_image_header_body_length(self):
        file_bytes = open("%s/assets/emerald.jpg" % path, "rb")
        ip = ImagePreview(file_path_or_bytes=file_bytes)

        self.assertEqual(len(ip.thumbnail_body_bytes()), 226)

    def test_image_b64(self):
        file_bytes = open("%s/assets/emerald.jpg" % path, "rb")
        ip = ImagePreview(file_path_or_bytes=file_bytes)

        self.assertEqual(len(ip.thumbnail_b64()), 1128)

    def test_image_header_b64(self):
        file_bytes = open("%s/assets/emerald.jpg" % path, "rb")
        ip = ImagePreview(file_path_or_bytes=file_bytes)

        self.assertEqual(len(ip.thumbnail_header_b64()), 828)

    def test_image_body_b64(self):
        file_bytes = open("%s/assets/emerald.jpg" % path, "rb")
        ip = ImagePreview(file_path_or_bytes=file_bytes)

        self.assertEqual(len(ip.thumbnail_body_b64()), 304)

    def test_check_if_header_from_different_image_creates_proper_thumbnail(self):
        from PIL import Image
        from io import BytesIO

        file_bytes = open("%s/assets/emerald.jpg" % path, "rb")
        file_bytes_second = open("%s/assets/matheson.jpg" % path, "rb")

        ip = ImagePreview(file_path_or_bytes=file_bytes)
        ip_second = ImagePreview(file_path_or_bytes=file_bytes_second)

        composited_image_bytes = ip.thumbnail_header_bytes() + ip_second.thumbnail_body_bytes()

        composited_image_bytes = ip.thumbnail_bytes()

        ip_composited = Image.open(BytesIO(composited_image_bytes))

        width, height = ip_composited.size

        self.assertEqual(width, 42)
        self.assertEqual(height, 42)
        self.assertEqual(ip_composited.format, "JPEG")


