import axinite.tools as axtools
import click

@click.command("live")
@click.argument("path", type=click.Path(exists=True))
@click.option("-f", "--frontend", type=str, default="plotly")
def live(path, frontend):
    name_to_frontend = {
        "vpython": axtools.vpython_frontend,
        "plotly": axtools.plotly_frontend,
    }
    args = axtools.read(path)
    axtools.live(args, name_to_frontend[frontend](args, "show"))