import asyncio

import click
import dotenv
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    """Main request handler"""

    def get(self) -> None:
        """GET request handler. Returns with "hello world"-like string"""
        self.write("<p>Hello, tornado</p>")


async def run_server(
    host: str,
    port: int,
    debug: bool,
) -> None:
    app = tornado.web.Application([(r"/", MainHandler)], debug=debug)

    app.listen(port=port, address=host)

    await asyncio.Event().wait()


@click.command()
@click.option("--host", default="0.0.0.0", help="The hostname to listen on")
@click.option("--port", default=8888, help="The port of the webserver")
@click.option("--debug", is_flag=True, default=False, help="Enable debug-mode")
@click.option(
    "--load-dotenv/--no-load-dotenv",
    default=True,
    help="Load the nearest .env and .flaskenv files to set environment variables",
)
def main(
    host: str,
    port: int,
    debug: bool,
    load_dotenv: bool,
) -> None:
    if load_dotenv:
        dotenv.load_dotenv()

    asyncio.run(run_server(host, port, debug))


if __name__ == "__main__":
    main()
