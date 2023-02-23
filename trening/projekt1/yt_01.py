import click
from commands import cli, setup_command, add_command, index_command, list_command
from os import getenv            #getenv 
from dotenv import load_dotenv   #getenv                 
load_dotenv()           #getenv




cli.add_command(setup_command)
cli.add_command(add_command)
cli.add_command(index_command)
cli.add_command(list_command)

if __name__ == '__main__':
    cli()
