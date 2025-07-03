import turbo_pygame

async def main():
    """initializing the engine and starting the main scene."""

    turbo_pygame.debug = False

    # Initialize the display (window size, title, etc.)
    turbo_pygame.Display.init(
        title="Example", 
        resolution=(1024, 720),
        fullscreen = False,
        resizable = True,
        dynamic_zoom = True,
        stretch=True
    )

    # Load game assets (e.g., images, sounds, etc.)
    turbo_pygame.Assets.init(
        path_data="/data",
        path_scenes="/scenes",
        path_scripts="/scripts",
        pre_load = True
    )

    # Create and configure the initial scene (scene name,**kwargs)
    turbo_pygame.Scene.Manager.create("sandbox", max_fps=-1)

    # Start the async scene
    await turbo_pygame.Scene.Manager.start()

if __name__ == "__main__":
    turbo_pygame.run(main)