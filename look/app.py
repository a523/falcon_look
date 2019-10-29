import os
import falcon
from wsgiref import simple_server
from look import images


def create_app(image_store):
    api = falcon.API()
    api.add_route('/images', images.Collection(image_store))
    api.add_route('/images/{name}', images.Item(image_store))
    return api


def get_app():
    storage_path = os.environ.get('LOOK_STORAGE_PATH', '.')
    image_store = images.ImageStore(storage_path)
    return create_app(image_store)


if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 8000, get_app())
    httpd.serve_forever()
