from flask import Blueprint

clothesmall = Blueprint('clothesmall', __name__, template_folder='./templates', static_folder='./static')
