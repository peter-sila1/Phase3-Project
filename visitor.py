import click
import re
from models import Visitor, session

# Define a regular expression pattern for email validation
email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

@click.group()
def visitor():
    """Manage Visitors"""

@visitor.command()
@click.option('--name', prompt='Enter name', help='Visitor name')
@click.option('--email', prompt='Enter email', help='Visitor email')
def add(name, email):
    """Add a visitor."""
    if not re.match(email_pattern, email):
        click.echo("Invalid email format. Please enter a valid email address.")
        return

    visitor = Visitor(full_name=name, email=email)
    session.add(visitor)
    session.commit()
    click.echo(f"{name} has been added.")

# ... rest of your code ...


@visitor.command()
def list():
    """List all visitors."""
    visitors = session.query(Visitor).all()
    click.echo("Visitors:")
    for visitor in visitors:
        click.echo(f"ID: {visitor.visitor_id}, Name: {visitor.full_name}, Email: {visitor.email}")


@visitor.command()
@click.argument('visitor_id', type=int)
@click.option('--name', prompt='Enter new name', help='New visitor name')
@click.option('--email', prompt='Enter new email', help='New visitor email')
def update(visitor_id, name, email):
    """Update visitor information by ID."""
    visitor = session.query(Visitor).filter_by(visitor_id=visitor_id).first()
    if visitor:
        visitor.full_name = name
        visitor.email = email
        session.commit()
        click.echo(f"Visitor with ID {visitor_id} updated.")
    else:
        click.echo(f"Visitor with ID {visitor_id} not found.")


@visitor.command()
@click.argument('visitor_id', type=int)
def delete(visitor_id):
    """Delete a visitor by ID."""
    visitor = session.query(Visitor).filter_by(visitor_id=visitor_id).first()
    if visitor:
        session.delete(visitor)
        session.commit()
        click.echo(f"Visitor with ID {visitor_id} deleted.")
        
    else:
        click.echo(f"Visitor with ID {visitor_id} not found.")

