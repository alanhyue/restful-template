from flask import request, jsonify, render_template
from ..main import main
from . import api

@main.app_errorhandler(404)
def page_not_found(e):
  if request.accept_mimetypes.accept_json and \
    not request.accept_mimetypes.accept_html:
    res = jsonify({'error': 'not found'})
    res.status_code = 404
    return res
  return render_template('404.html'), 404

def unauthorized(message='unauthorized access'):
  resp = jsonify({'error': 'unauthorized', 'message': message})
  resp.status_code = 401
  return resp
  
def forbidden(message='forbidden access'):
  resp = jsonify({'error': 'forbidden', 'message': message})
  resp.status_code = 403
  return resp

def not_found(message='the requested resource cannot be found'):
  resp = jsonify({'error': 'not found', 'message': message})
  resp.status_code = 404
  return resp