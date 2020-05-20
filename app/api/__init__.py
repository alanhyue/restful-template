from flask import Blueprint
from flask_restful import Api
from ..utils import dotdict


api = Blueprint('api', __name__)
restful = Api(api, catch_all_404s=True)

URL = dotdict()

# Add Your Resources Here
# Example:
#
# from .resource import Profile
# URL.PROFILE = '/profile/'
# restful.add_resource(Profile, URL.PROFILE)
