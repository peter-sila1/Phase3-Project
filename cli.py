import click
from visitor import visitor
from office import office
from visits import visits

@click.group()
def cli():
    """VMS CLI"""

cli.add_command(visitor)   
cli.add_command(office)
cli.add_command(visits)

if __name__ == '__main__':
    cli()