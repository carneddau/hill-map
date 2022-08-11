from pathlib import Path

from typer import Option, Typer

from .data import display_csv_data

app = Typer()


@app.command()
def main(
    file: Path = Option(
        ...,
        readable=True,
        resolve_path=True,
        exists=True,
        dir_okay=False,
        file_okay=True,
    )
):
    display_csv_data(file)
