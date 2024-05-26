import click

@click.group()
def cli():
    pass

@cli.command()
@click.argument('feature_name')
def new_feature(feature_name):
    """Generate a new project space for the feature."""
    print(f"Creating a new feature: {feature_name}")

@cli.command()
@click.argument('feature_name')
def test(feature_name):
    """Test the given feature."""
    print(f"Testing feature: {feature_name}")

@cli.command()
@click.argument('feature_name')
def modify_feature(feature_name):
    """Modify the given feature."""
    print(f"Modifying feature: {feature_name}")

@cli.command()
def config():
    """Configure settings."""
    print("Configuring settings")

@cli.command()
@click.argument('feature_name')
def setup_feature(feature_name):
    """Set up a new feature."""
    print(f"Setting up feature: {feature_name}")

if __name__ == "__main__":
    cli()
