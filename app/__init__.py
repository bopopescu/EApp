# Init File
from flask import Flask

app = Flask(__name__,
            instance_relative_config=False,
            template_folder="templates",
            static_folder="static")

from app import config
from app import data
from app import forms
from app import details
from app import links
from app import models
from app import myRequests
from app import userRoutes
from app import adminRoutes
yhfyjyrjy
