from flask_combo_jsonapi import ResourceList, ResourceDetail

from schemas import TagSchema, UserSchema
from models import Tag, User
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


class UserDetail(ResourceDetail):
    shcschema = UserSchema
    data_layer = {
        'session': db.session, 
        'model': User
    
    }

class UserList(ResourceList):
    shcschema = UserSchema
    data_layer = {
        'session': db.session, 
        'model': User
    
    }