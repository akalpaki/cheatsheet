from flask import Flask, redirect, url_for


def create_app():
    """Application factory."""
    app = Flask(__name__, template_folder='templates')
    app.config.from_pyfile('../config.py')

    # Initialize the database
    from . import db
    db.init_app(app)

    # Webapp routes are here.
    from . import routes
    app.register_blueprint(routes.api)

    @app.route('/')
    def home_redirect():
        """Redirects to homepage when you load the site."""
        return redirect(url_for('cheat_sheet.frontpage'))

    return app

# Application entrypoint (?)


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
