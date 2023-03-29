import typer
import rich
from BatchBacktesting import run_backtests, run_backtests_strategies
from strategies import Ema

app = typer.Typer()


@app.command(help="Run backtests for a list of instruments using a specified strategy")
def run_backtests(
    instruments: list = typer.Argument(..., help="List of instruments to run backtests for"),
    strategy: str = typer.Argument(..., help="Strategy to run backtests for"),
    num_threads: int = typer.Option(4, help="Number of threads to use. Defaults to 4."),
    generate_plots: bool = typer.Option(True, help="Generate plots. Defaults to True."),
):
    """
    Run backtests for a list of instruments using a specified strategy.
    """
    typer.echo(f"Running backtests for {instruments} using {strategy}...")
    run_backtests(instruments, strategy)

@app.command(
    help="Run backtests for a list of instruments using a specified strategy"
)
def run_backtests_strategies(
    instruments: list = typer.Argument(..., help="List of instruments to run backtests for"),
    strategies: list = typer.Argument(..., help="List of strategies to run backtests for"),
    num_threads: int = typer.Option(4, help="Number of threads to use. Defaults to 4."),
    generate_plots: bool = typer.Option(True, help="Generate plots. Defaults to True.")
):
    """
    Run backtests for a list of instruments using a specified strategy.
    """
    typer.echo(f"Running backtests for {instruments} using {strategies}...")
    run_backtests_strategies(instruments, strategies)

if __name__ == "__main__":
    app(
        help="Run backtests for a list of instruments using a specified strategy"
    )