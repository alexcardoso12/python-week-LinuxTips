from typer.testing import CliRunner
from beerlog.cli import main

runner = CliRunner()

def test_add_beer():
    result = runner.invoke(
        main, ["add", "Brahma", "Lager", "--flavor=5", "--image=6", "--cost=2"]
    )
    assert result.exit_code == 0
    assert "Beer added" in result.stdout