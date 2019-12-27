# project/server/__init__.py


import os

from flask import Flask
from flask_bootstrap import Bootstrap
from deepgeo import Engine
# instantiate the extensions
bootstrap = Bootstrap()


def create_app(script_info=None):

    # instantiate the app
    app = Flask(
        __name__,
        template_folder="../client/templates",
        static_folder="../client/static",
    )

    # set config
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    # set up extensions
    bootstrap.init_app(app)

    # register blueprints
    from project.server.main.views import main_blueprint

    app.engine = Engine()
    app.engine.add_model('mscoco_maskrcnn','maskrcnn','/home/DeepGeoAPI/config/maskrcnn_mscoco_config.json')
    app.engine.add_model('teeth','maskrcnn', '/home/DeepGeoAPI/config/maskrcnn_teeth_config.json')
    app.engine.add_model('roaddamage','yolo', '/home/DeepGeoAPI/config/yolo_road-damage_config.json')
    app.engine.add_model('mscoco_yolo','yolo', '/home/DeepGeoAPI/config/yolo_mscoco_config.json')

    app.register_blueprint(main_blueprint)

    # shell context for flask cli
    app.shell_context_processor({"app": app})
    return app
