from flask_combo_jsonapi import ResourceList, ResourceDetail

from schemas import TagSchema
from models import Tag
from models.database import db



class TagList(ResourceList):
    schema = TagSchema
    data_layer = {
        'session': db.session, 
        'model': Tag
    
    }

class TagDetail(ResourceDetail):
    schema = TagSchema
    data_layer = {
        'session': db.session, 
        'model': Tag
    
    }