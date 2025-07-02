# /// script
# dependencies = [
#   "pyxora",
#   "pygame-ce"
# ]
# ///

import pyxora


async def main():
    """initializing the engine and starting the main scene."""

    pyxora.debug = False

    # Initialize the display (window size, title, etc.)
    pyxora.Display.init(
        title="Test",
        resolution=(500, 500),
        fullscreen=False,
        dynamic_zoom=True,
        resizable=True,
        stretch=True,
    )

    # Load game assets (e.g., images, sounds, etc.)
    pyxora.Assets.init(path_scenes="/scenes", pre_load=True)

    # Create and configure the initial scene (scene name,**kwargs)
    pyxora.Scene.manager.create("test", max_fps=-1)

    # Start the async scene
    await pyxora.Scene.manager.start()


if __name__ == "__main__":
    pyxora.asyncio.run(main)
