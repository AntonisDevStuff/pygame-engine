import pygame

class SoundEffect:
    _volume = 1.0

    def __init__(self, effect:pygame.mixer.Sound, volume:float = 1.0) -> None:
        """
        Initialize a SoundEffect object

        Args:
            effect (pygame.mixer.Sound): The sound effect.
            volume (float): The volume level of the music.
        """
        self._effect = effect
        self._local_volume = volume

    @property
    def playing(self) -> bool:
        """The playing status of the effect."""
        return bool(self._effect.get_num_channels())

    @property
    def channels(self) -> int:
        """The number of channels the effect is playing on."""
        return self._effect.get_num_channels()

    @property
    def length(self) -> float:
        """The length of the sound effect in seconds."""
        return self._effect.get_length()

    @property
    def raw(self) -> bytes:
        """The raw data of the sound effect in byes"""
        return self._effect.get_raw()

    @property
    def volume(self) -> float:
        """The volume of the music (volume * local_volume)."""
        return self._volume * self._local_volume

    @classmethod
    def change_volume(cls,value: float) -> None:
        """Change the volume of all music."""
        cls._volume = value
        # self._effect.set_volume(cls.volume)

    def change_local_volume(self,value: float) -> None:
        """Change the volume of the music."""
        self._local_volume = value
        self._effect.set_volume(self.volume)

    def play(self,loops:int = -1, maxtime:int = 0, fade_ms:int = 0) -> None:
        """
        Starts the sound effect.

        Parameters:
            loops (int): Number of times to repeat the sound effect after the first play.
                        -1 means the sound effect will play once.
                        0 means indefinitely.
                        >=1 means play n times.

            maxtime (int): Max Milliseconds to play the sound effect.

            fade_ms (int): Milliseconds to fade in the sound effect.
        """
        self._effect.stop()  # stop and play a new one
        self._effect.play(loops+1,maxtime,fade_ms)

    def stop(self) -> None:
        """
        Stop the sound effect.
        """
        self._effect.stop()
