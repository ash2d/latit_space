from latit_space.__main__ import main

from click.testing import CliRunner


def test_latit_space_cli():
    runner = CliRunner()
    result = runner.invoke(main, ())
    assert result.exit_code == 0
