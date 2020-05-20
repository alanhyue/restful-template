from functools import wraps
from flask import g

from ..model import Permission
from .errors import forbidden, not_found, unauthorized

def permission_required(permission):
  def decorator(f):
    @wraps(f)
    def check_permission(*args, **kwargs):
      if not g.current_user.can(permission):
        return forbidden('Insufficient permissions')
      return f(*args, **kwargs)
    return check_permission
  return decorator


def admin_required(f):
  return permission_required(Permission.ADMIN)(f)

def get_or_404(id_arg, model, to):
  """Use id_arg to query the model and put result in the to variable.
  Returns 404 if target is not found. Otherwise put the target under 
  variable name specified by {to}.
  """
  def decorator(f):
    @wraps(f)
    def query_db(*args, **kwargs):
      id = kwargs.pop(id_arg)
      target = model.query.get(id)
      if target is None:
        return not_found()
      else:
        kwargs[to] = target
        return f(*args, **kwargs)
    return query_db
  return decorator

def author_or_admin_required(target_arg):
  """Check if the current user can edit the target.
  That is, is the author of the target or an administrator.
  """
  def decorator(f):
    @wraps(f)
    def check_author_admin(*args, **kwargs):
      target = kwargs.get(target_arg)
      if not g.current_user.can_edit(target):
        return unauthorized()
      return f(*args, **kwargs)
    return check_author_admin
  return decorator