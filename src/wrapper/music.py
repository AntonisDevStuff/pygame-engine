from ..utils import engine
import pygame

class Music:
    _volume = 1.0
    _active = None

    def __init__(self, path:str, volume:float = 1.0) -> None:
        """
        Initialize a Music object with a path and volume.

        Args:
            path (str): The path to the music file.
            volume (float): The volume level of the music.
        """
        self._path = path
        self._local_volume = volume

    @property
    def playing(self) -> bool:
        """The playing status of the music."""
        if self is not Music._active:
            return False
        return pygame.mixer.music.get_busy()

    @property
    def time(self) -> int:
        """The current time position of the music."""
        if self is not Music._active:
            return 0
        return pygame.mixer.music.get_pos()

    @property
    def volume(self) -> float:
        """
        The volume of the music (volume * local_volume)."""
        return self._volume * self._local_volume

    @property
    def metadata(self) -> dict:
        """The metadata of the music."""
        return pygame.mixer.music.get_metadata(self._path)

    @classmethod
    def change_volume(cls,value: float) -> None:
        """Change the volume of all music."""
        cls._volume = value
        pygame.mixer.music.set_volume(cls.volume)

    def change_local_volume(self,value: float) -> None:
        """Change the volume of the music."""
        self._local_volume = value
        pygame.mixer.music.set_volume(self.volume)

    def play(self,loops:int = -1, start:float = 0.0, fade_ms:int = 0) -> None:
        """
        Starts the music.

        Parameters:
            loops (int): Number of times to repeat the music after the first play.
                        -1 means the music will play once.
                        0 means indefinitely.
                        >=1 means play n times.

            start (float): Position (in seconds) to start the music from.

            fade_ms (int): Milliseconds to fade in the music.
        """
        pygame.mixer.music.load(self._path)
        pygame.mixer.music.set_volume(self.volume)
        pygame.mixer.music.play(loops+1,start,fade_ms)
        Music._active = self

    def resume(self) -> None:
        """
        Resume the music.
        """
        if self is not Music._active:
            engine.warning(f"Music object {self} is not active.")
            return
        pygame.mixer.music.unpause()

    def pause(self) -> None:
        """
        Pause the music.
        """
        if self is not Music._active:
            engine.warning(f"Music object {self} is not active.")
            return
        pygame.mixer.music.pause()

    def stop(self) -> None:
        """
        Stop the music.
        """
        if self is not Music._active:
            engine.warning(f"Music object {self} is not active.")
            return
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        Music._active = None
