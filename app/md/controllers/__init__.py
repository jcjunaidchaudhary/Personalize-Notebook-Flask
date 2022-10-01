from flask_restful import Api
from flask import Blueprint
from app.auth.controllers.login import LoginView

from app.auth.controllers.signup import SignUpView
from app.md.controllers.note import NoteView


md_blueprint =Blueprint("md",__name__,url_prefix="/md")
api=Api(md_blueprint)

# http://127.0.0.1:5000/api/md/note
api.add_resource(NoteView,"/note/") 
