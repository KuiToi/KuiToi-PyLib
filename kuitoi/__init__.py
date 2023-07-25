from logging import Logger


# noinspection PyUnreachableCode
class Player:
    raise ImportError("Use with server only!")

    def __init__(self):
        raise NotImplementedError

    @property
    def log(self) -> Logger:
        raise NotImplementedError

    @property
    def addr(self) -> str:
        raise NotImplementedError

    @property
    def cid(self) -> int:
        raise NotImplementedError

    @property
    def pid(self) -> int:
        raise NotImplementedError

    @property
    def key(self) -> str:
        raise NotImplementedError

    @property
    def guest(self) -> bool:
        raise NotImplementedError

    @property
    def ready(self) -> bool:
        raise NotImplementedError

    @property
    def identifiers(self) -> dict:
        raise NotImplementedError

    @property
    def cars(self) -> list:
        raise NotImplementedError

    @property
    def focus_car(self) -> int:
        raise NotImplementedError

    @property
    def last_position(self) -> dict:
        raise NotImplementedError

    async def kick(self, reason: str = None) -> None:
        raise NotImplementedError

    async def send_message(self, message: str, to_all: bool = True) -> None:
        raise NotImplementedError

    async def send_event(self, event_name: str, event_data: str | dict | list | Any, to_all: bool = True) -> None:
        raise NotImplementedError

    async def delete_car(self, car_id: int) -> None:
        raise NotImplementedError


# noinspection PyUnreachableCode
class KuiToi:
    raise ImportError("Use with server only!")

    def __init__(self, name):
        """
        Library for KuiToi-Server


        Usage:

        >>> kt = KuiToi("PluginName")
        >>> kt.log.info("My plugin logger!")

        """

    @property
    def log(self) -> Logger:
        """
        Constant
        Returns a pre-configured logger

        :return: Logger instance
        """

        raise NotImplementedError

    @property
    def name(self) -> str:
        """
        Constant
        Returns the name of the plugin

        :return: plugin name
        """

        raise NotImplementedError

    @property
    def dir(self):
        """
        Constant
        Returns the directory of the plugin

        :return: Plugin directory
        """

        raise NotImplementedError

    @contextmanager
    def open(
            self,
            file: str | bytes | PathLike[str] | PathLike[bytes] | int,
            mode: str,
            buffering: int = ...,
            encoding: str | None = ...,
            errors: str | None = ...,
            newline: str | None = ...,
            closefd: bool = ...,
            opener: (str, int) | None = ...
    ) -> IO:
        """
        Parameters are the same as for open()

        :return: IO object with <plugin_dir>/<file>
        """

        # path = os.path.join(self.__dir, file)
        # f = None
        # try:
        #     f = open(path, mode, buffering, encoding, errors, newline, closefd, opener)
        #     yield f
        # except Exception as e:
        #     raise e
        # finally:
        #     if f is not None:
        #         f.close()

        raise NotImplementedError

    def register_event(self, event_name: str, event_func: function) -> None:
        """
        Register event to call function

        In `event_func`, you can pass both regular functions and async functions - you don't need to make them async beforehand.
        You can also create your own events with your own names.
        You can register an unlimited number of events.

        Data is passed to all events in the form of: `{"event_name": event_name, "args": args, "kwargs": kwargs}`\
        `args: list` -> Represents an array of data passed to the event\
        `kwargs: dict` -> Represents a dictionary of data passed to the event
        The data will be returned from all successful attempts in an array.

        :param event_name: -> The name of the event that `event_func` will be called on.
        :param event_func: -> The function that will be called.
        :return: None
        """

        raise NotImplementedError

    def call_event(self, event_name: str, *args, **kwargs) -> List[Any]:
        """
        Call not async events

        :param event_name: -> The name of the event to call.
        :param args: -> Arguments to be passed to the function.
        :param kwargs: -> KWArguments to be passed to the function.
        :return: List with returns from functions
        """

        raise NotImplementedError

    async def call_async_event(self, event_name: str, *args, **kwargs) -> List[Any]:
        """
        Call async events

        :param event_name: -> The name of the event to call.
        :param args: -> Arguments to be passed to the function.
        :param kwargs: -> KWArguments to be passed to the function.
        :return: List with returns from async functions
        """

        raise NotImplementedError

    async def call_lua_event(self, event_name: str, *args) -> List[Any]:
        """
        Call async events

        :param event_name: -> The name of the event to call.
        :param args: -> Arguments to be passed to the function.
        :return: List with returns from lua functions
        """

        raise NotImplementedError

    def get_player(self, pid: int = None, nick: str = None) -> Player | None:
        """

        :param pid: -> Player ID - The identifier of the player.
        :param nick: -> Player Nickname - The name of the player.
        :return: Player class
        """

        if pid is None and nick is None:
            raise ValueError("You must provide a player ID or player nick")

        raise NotImplementedError

    def get_players(self) -> List[Player] | List:
        """
        Returns an array with all players.

        The array will be empty if there are no players.

        :return: Array with players
        """

        raise NotImplementedError

    def players_counter(self) -> int:
        """
        How many players are in the game.

        :return: returns the number of players currently online
        """

        raise NotImplementedError

    def is_player_connected(self, pid: int = None, nick: str = None) -> Bool:
        """

        :param pid: -> Player ID - The identifier of the player.
        :param nick: -> Player Nickname - The name of the player.
        :return: bool
        """

        if pid is None and nick is None:
            raise ValueError("You must provide a player ID or player nick")

        raise NotImplementedError
