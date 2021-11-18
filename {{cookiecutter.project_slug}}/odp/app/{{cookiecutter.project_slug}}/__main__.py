from flask import Flask
import click

from typing import *


app = Flask("Hello world")

@app.route("/")
def root_endpoint() -> str:
    return "<p>Hello, World</p>"

@click.command()
@click.option("--host", default="0.0.0.0", help="The hostname to listen on")
@click.option("--port", default=None, help="The port of the webserver")
@click.option("--debug", is_flag=True, help="Enable debug-mode")
@click.option("--load-dotenv/--no-load-dotenv", default=True,
              help="Load the nearest .env and .flaskenv files to set environment variables")
def main(
        host: Optional[str],
        port: Optional[int],
        debug: Optional[bool],
        load_dotenv: bool,
) -> None:
    app.run(
        host=host,
        port=port,
        debug=debug,
        load_dotenv=load_dotenv
    )

if __name__ == "__main__":
    main()
