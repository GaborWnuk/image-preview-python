imagepreview
============
[![Build Status](https://travis-ci.org/GaborWnuk/image-preview-python.svg?branch=master)](https://travis-ci.org/GaborWnuk/image-preview-python)

Simple helper module for Image Preview method for REST and GraphQL for immediate image preview on your client's side (Swift, Java, JavaScript and so on).

Idea is to deliver only around 200 bytes of image data as a normal base64 data in one of JSON fields of your entities and then issue request to obtain full resolution of an image.

## Short "how does it work"
The main reason to do such thing is to show your user approximate look of your data stream as soon as possible. This method gives you the ability to serve image previews in the sam milisecond you show your text content in your app, as image preview is delivered as one of data fields in your JSON response.

This library is sort of a helper to achieve above.

Because every thumbnail is compressed as JPEG, with the same size (default: 42x42 pixels) and using the same Huffman table, each JPEG file consist of a common header (620 bytes) and a small picture data part (around 200 bytes, depending on quality you use).

Having this in mind we choose to omit headers and send only 200 bytes (base64) and then prepend this data with a header on client side.

You can find basic Swift / iOS example here: [https://github.com/GaborWnuk/image-preview-ios-demo](https://github.com/GaborWnuk/image-preview-ios-demo).
