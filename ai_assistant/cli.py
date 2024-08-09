import click
from click_default_group import DefaultGroup

from aws import list_profiles, list_models

@click.group(
    cls=DefaultGroup,
    default="hello",
    default_if_no_args=True,
)
def cli():
    """
    XXX
    """

@cli.command(name="hello")
def hello():
    """
    XXX
    """
    click.echo("Hello, World!")

@cli.group(
    cls=DefaultGroup,
    default="list",
    default_if_no_args=True,
)
def profiles():
    "Manage stored AWS profiles"

@cli.group(
    cls=DefaultGroup,
    default="list",
    default_if_no_args=True,
)
def models():
    "Manage available models on Amazon Bedrock"

@models.command(name="list")
@click.option("--all", is_flag=True, help="Show all models", default=False,)
@click.option("--provider", help="Filter by provider name", default=None,)
def models_list(all: bool, provider: str):
    "List names of all available models on Amazon Bedrock"
    click.echo("List of available models on Amazon Bedrock")
    for model in list_models(all, provider):
        click.echo(f"{model["providerName"]}: {model["modelName"]} ({model["modelId"]})")

@profiles.command(name="list")
def profiles_list():
    "List names of all stored AWS profiles"
    message, profiles = list_profiles()
    click.echo(message)
    for profile in profiles:
        click.echo(profile)

if __name__ == "__main__":
    cli()


