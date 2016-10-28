#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    __init__.py
    ~~~~~~~~~~~

    no description available

    :copyright: (c) 2016 by GaborWnuk.
    :license: see LICENSE for more details.
"""

__title__ = 'imagepreview'
__version__ = '0.0.1'
__author__ = 'Gabor Wnuk'

import base64
from io import BytesIO
from PIL import Image, ImageOps

class ImagePreview(object):
    """Simple helper module for Image Preview method for REST and GraphQL for
    immediate image preview on your client's side (Swift, Java, JavaScript
    and so on).

    Idea is to deliver only around 200 bytes of image data as a normal
    base64 data in one of JSON fields of your entities and then issue request
    yo obtain full resolution of an image.

    Attributes:
        file_path_or_bytes: Standard PIL Image constructor argument for either
                            file path (string) or BytesIO object.
        thumbnail_size: desired thumbnail image size.
        quality: desired JPEG compression quality, where 0 is the lowest quality,
                    and 100 the highest.
    """

    __image = None

    __thumbnail_bytes = None
    __thumbnail_header_bytes = None
    __thumbnail_body_bytes = None

    __header_size = 620

    def __init__(self, file_path_or_bytes, thumbnail_size=(42, 42), quality=15):
        self.__image = Image.open(file_path_or_bytes)

        thumbnail = ImageOps.fit(self.__image, thumbnail_size, Image.ANTIALIAS)
        thumbnail_bytes = BytesIO()

        thumbnail.save(thumbnail_bytes, "JPEG", quality=quality, optimize=False)

        self.__thumbnail_bytes = thumbnail_bytes.getvalue()

        self.__thumbnail_header_bytes = self.__thumbnail_bytes[:self.__header_size]
        self.__thumbnail_body_bytes = self.__thumbnail_bytes[self.__header_size:]

    def thumbnail_bytes(self):
        return self.__thumbnail_bytes

    def thumbnail_header_bytes(self):
        return self.__thumbnail_header_bytes

    def thumbnail_body_bytes(self):
        return self.__thumbnail_body_bytes

    def thumbnail_b64(self):
        return base64.b64encode(self.__thumbnail_bytes).decode('utf-8')

    def thumbnail_header_b64(self):
        return base64.b64encode(self.__thumbnail_header_bytes).decode('utf-8')

    def thumbnail_body_b64(self):
        return base64.b64encode(self.__thumbnail_body_bytes).decode('utf-8')

