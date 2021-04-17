import click
from . import gui
import traceback

@click.command()
def cli():
    gui.main()

def main():
    cli()

if __name__ == '__main__':
    main()