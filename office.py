import click
from models import  Office, session

@click.group()
def office():
    """Manage offices."""
    
@office.command()
@click.option('--name', prompt='Office name', help='Office name')
def add(name):
    """Add an office."""
    office = Office(office_name=name)
    session.add(office)
    session.commit()
    click.echo(f"Office {name} added.")

@office.command()
def list():
    """List all offices."""
    offices = session.query(Office).all()
    click.echo("Offices:")
    for office in offices:
        click.echo(f"ID: {office.office_id}, Name: {office.office_name}")


@office.command()
@click.argument('office_id', type=int)
@click.option('--new_name', prompt='Enter new name', help='New office name')
def update(office_id, new_name):
    """Update office information by ID."""
    office = session.query(Office).filter_by(office_id=office_id).first()
    if office:
        office.office_name = new_name
        session.commit()
        click.echo(f"Office with ID {office_id} updated.")
    else:
        click.echo(f"Office with ID {office_id} not found.")


@office.command()
@click.argument('office_id', type=int, required=True)
def delete(office_id):
    """Delete an office by ID."""
    office = session.query(Office).filter_by(office_id=office_id).first()
    if office:
        session.delete(office)
        session.commit()
        click.echo(f"Office with ID {office_id} deleted.")
    else:
        click.echo(f"Office with ID {office_id} not found.")