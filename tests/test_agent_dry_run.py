'''Test run_sync with dry_run paramenter set to True'''

from pydantic_ai_slim.pydantic_ai.agent import Agent


def test_dry_run():
    agent = Agent('test')

    result_sync = agent.run_sync('What is the capital of Italy?', dry_run=True)

    assert result_sync.output == "dry run completed successfully"
    
    #> dry run completed successfully