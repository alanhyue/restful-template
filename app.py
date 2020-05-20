from app import create_app, db
from flask_migrate import Migrate
import click

import os
app = create_app(os.environ.get('APP_CONFIG') or 'default')
Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(
        db=db, 
        )

@app.cli.command()
@click.argument('test_names', nargs=-1)
def test(test_names):
    """Run unit tests."""
    import unittest
    if test_names:
        tests = unittest.TestLoader().loadTestsFromNames(test_names)
    else:
        tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    