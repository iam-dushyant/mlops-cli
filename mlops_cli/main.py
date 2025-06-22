import typer
from mlops_cli.train import app as train_app

app = typer.Typer()

def version_callback(value: bool):
    if value:
        typer.echo("mlops-cli version 0.2.0")
        raise typer.Exit()

@app.callback()
def main(
    version: bool = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit",
        callback=version_callback,
        is_eager=True,
    )
):
    pass

@app.command()
def hello():
    print("Hello from MLOps CLI!")

app.add_typer(train_app, name="train")
    
if __name__ == "__main__":
    app()
