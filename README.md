imagepreview
============
[![Build Status](https://travis-ci.org/GaborWnuk/image-preview-python.svg?branch=master)](https://travis-ci.org/GaborWnuk/image-preview-python)

Simple helper module for Image Preview method for REST and GraphQL for immediate image preview on your client's side (Swift, Java, JavaScript and so on).

Idea is to deliver only around 200 bytes of image as a normal base64 data in one of JSON fields of your entities and then issue request to obtain full resolution of an image.

## Short "how does it work"
The main reason to do such thing is to show your user approximate look of your data stream as soon as possible. This method gives you the ability to serve image previews in the sam milisecond you show your text content in your app, as image preview is delivered as one of data fields in your JSON response, i.e:

```json
{
  "data": {
    "articles": [
      {
        "title": "Piotr Cyrwus zostanie fanatykiem wędkarstwa",
        "img": {
          "url": "https://i.wpimg.pl/1000-666/CSM//d.wpimg.pl/1636256103--1868262584_piotr-cyrwus.jpg",
          "b64": "AD8AqOc54pAMDNKTyRnrTkUS/JnBxUAOVSR8qE5pGVwcOu09qvD5AAo+XFVrkk7TjHNMdiLoB7UmT7UpHzU3A9TSEIynOaWLJlGDzmn3DL5zKigAHGR3otQGlxj+E00gLJb5euDUDtukxg8CrJTdVO6Y/aDjjaAOKdhsUZLDilbBY49aiSXYRkZFWMbud3XnrUtWEVCSWJPU81Zsf+Pg/wC7VX+KrVl/x8fhWiEaGBnNY8jb5Gb1Oa1pP9S/+6aypgBKwAwKGAw1cjdfLXI7DvVKlyfWpauM/9k="
        }
      }
    ]
  }
}
```

This library is sort of a helper to achieve above.

Because every thumbnail is compressed as JPEG, with the same size (default: 42x42 pixels) and using the same Huffman table, each JPEG file consist of a common header (620 bytes) and a small picture data part (around 200 bytes, depending on quality you use).

Having this in mind we choose to omit headers and send only 200 bytes (base64) and then prepend this data with a header on client side.

```python
file_bytes = open("matheson.jpg", "rb")

ip = ImagePreview(file_path_or_bytes=file_bytes)

# this is what you should have on your client side and prepend image_body with it
image_header = ip.thumbnail_header_bytes()

# this is what you send in your API to your client
image_body = ip.thumbnail_body_b64()
```

Or fetch from remote location:
```python
import requests

url = "https://upload.wikimedia.org/wikipedia/commons/4/44/Mt_Cook,_NZ.jpg"
response = requests.get(url)
ip = ImagePreview(file_path_or_bytes=BytesIO(response.content))

# this is what you send in your API to your client
image_body = ip.thumbnail_body_b64()
```

You can find basic Swift / iOS example here: [https://github.com/GaborWnuk/image-preview-ios-demo](https://github.com/GaborWnuk/image-preview-ios-demo).

## How to use
To install the package simply use PyPi
```
$ pip install imagepreview
```

## License
MIT License

Copyright (c) 2016 Gabor Wnuk

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
