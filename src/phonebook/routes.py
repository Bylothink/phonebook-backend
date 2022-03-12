from strawberry.flask.views import GraphQLView

from .api import schema
from .app import app


@app.route('/')
def index_page():
    return "<h1>It works!</h1>"


app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))
