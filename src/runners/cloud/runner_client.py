from game_contracts.runner_client_abc import RunnerClientABC


class CloudRunnerClient(RunnerClientABC):

    def poll_for_server_response(self) -> dict: ...

    def post_to_server(self, payload) -> None: ...

    def get_games_for_player(self, game_configs) -> dict: ...

    def setup_new_game(self, game_configs: dict) -> dict: ...

    def initialize_server(self, params) -> bool: ...
