import turbo_pygame
import turbo_pygame.utils
import random

pygame = turbo_pygame.pygame
pymunk = turbo_pygame.pymunk
    
class Sandbox(turbo_pygame.Scene):
    def on_create(self):
        self.background_color = "gray"
        if turbo_pygame.utils.is_web():
            self.text_font = "freesans"
        else:
            self.text_font = "consolas"

    def start(self):
        self.objects = turbo_pygame.Objects(self,render=self.Camera)
        self.objects.set_gravity((0,100))

        self.text_pos = []
        self.render_amount_in_Camera = 0
        self.res = self.Display.res

        self.Event.create("update_text",state=0)
        self.Event.schedule("update_text",100)
        self.Event.post("update_text") # manual post to init vars   

        self.box = []
        box_size = (500,500)
        gap_x = 1000
        gap_y = 1000

        seen_positions = set()
        box_amount = 4
        for i in range(-box_amount, box_amount+1) : 
            for j in range(-box_amount, box_amount+1):
                box_pos = (i * gap_x, j * gap_y)

                if box_pos in seen_positions:
                    continue

                seen_positions.add(box_pos)

                obj_size = random.randint(10, 20)
                ball_amount = 30
                obj_type = random.choice(["circle", "rect"])

                self.box.append(
                    self.create_box(box_pos, box_size, obj_size, ball_amount, obj_type)
                )

        self.update_visable()
        self.update_text_pos()


    def on_keydown(self,key):
        key == "p" and self.Manager.pause()
        key == "r" and self.Manager.restart()
        key == "f2" and self.objects.toggle_hitbox()
        key == "f5" and self.Display.toggle_fullscreen()

    def on_keypressed(self,keys):
        zoom = self.Camera.get_zoom_factor()

        Camera_speed = 3000 * self.dt / zoom if zoom > 0 else 3000 * self.dt * abs(zoom)

        "w" in keys and self.Camera.move((0,-Camera_speed)) 
        "s" in keys and self.Camera.move((0,Camera_speed)) 

        "a" in keys and self.Camera.move((-Camera_speed,0)) 
        "d" in keys and self.Camera.move((Camera_speed,0))

        self.update_text_pos()

    def on_mousewheel(self,wheel):
        mouse_pos = self.get_mouse_pos()
        wheel == "up" and self.Camera.zoom(2)
        wheel == "down" and self.Camera.zoom(-2)

    def on_paused_keydown(self,key):
        key == "p" and self.Manager.resume()

    def update(self):
        self.objects.update()
        self.update_visable()
        self.update_text()

    def draw(self):
        self.objects.draw()
        self.draw_texts()

    @turbo_pygame.utils.event_listener("update_text")
    def update_text(self):
        pos = turbo_pygame.vector(self.res[0]-100,10)
        text = f"Fps: {int(self.fps)}"
        self.text_fps = turbo_pygame.Text(pos,text,"black",self.text_font)

        pos = turbo_pygame.vector(0,0)
        text = f"Total Balls: {self.objects.counter}"
        self.text_data = turbo_pygame.Text(pos,text,"black",self.text_font)

        pos = turbo_pygame.vector(0,30)
        text = f"Camera Render: {self.render_amount_in_Camera}"
        self.text_data2 = turbo_pygame.Text(pos,text,"black",self.text_font)

        pos = turbo_pygame.vector(0,50)
        text = f"Pos: ({int(self.Camera.pos[0])},{int(self.Camera.pos[1])})"
        self.text_data3 = turbo_pygame.Text(pos,text,"black",self.text_font)

        pos = turbo_pygame.vector(0,70)
        text = f"Zoom: {self.Camera.get_zoom_factor()}x"
        self.text_data4 = turbo_pygame.Text(pos,text,"black",self.text_font)


    @turbo_pygame.utils.run_every(100)
    def update_visable(self):
        counter = 0
        for obj in self.objects:
            if self.Camera.is_visible(obj.hitbox):
                counter += 1

        for text in self.text_pos:
            if self.Camera.is_visible(text):
                counter += 1


        self.render_amount_in_Camera = counter


    @turbo_pygame.utils.run_every(50)
    def update_text_pos(self):
        self.text_pos = []
        gape_x = 1000
        gape_y = 1000
        offset_x = self.Camera.pos[0] // gape_x + 1
        offset_y = self.Camera.pos[1] // gape_x + 1
        for sign_x in [-1, 1]:
            for sign_y in [-1, 1]:
                for i in range(5):
                    for j in range(5):
                        world_x = i * gape_x * sign_x + (offset_x * gape_y)
                        world_y = j * gape_y * sign_y + (offset_y * gape_x)
                        pos = turbo_pygame.vector(world_x, world_y)
                        text = f"({int(world_x)},{int(world_y)})"
                        self.text_pos.append(turbo_pygame.Text(pos,text,"black",self.text_font,100,"center"))


    def draw_texts(self):
        for text_pos in self.text_pos:
            self.Camera.draw_text(text_pos)

        Sandbox.Display.draw_text(self.text_fps)
        Sandbox.Display.draw_text(self.text_data)
        Sandbox.Display.draw_text(self.text_data2)
        Sandbox.Display.draw_text(self.text_data3)
        Sandbox.Display.draw_text(self.text_data4)


    def create_box(self, box_center, box_size, obj_size, obj_amount, obj_type):
        world_size = turbo_pygame.vector(*box_size)
        half_world = world_size / 2
        box_center = turbo_pygame.vector(*box_center)

        background = turbo_pygame.Rect(box_center - half_world, world_size, "white")

        for _ in range(obj_amount):
            min_x = box_center.x - half_world.x + obj_size
            max_x = box_center.x + half_world.x - obj_size
            min_y = box_center.y - half_world.y + obj_size
            max_y = box_center.y + half_world.y - obj_size

            pos = turbo_pygame.vector(
                random.uniform(min_x, max_x),
                random.uniform(min_y, max_y)
            )

            if obj_type == "circle":
                obj = turbo_pygame.Object(pos, obj_size,image="default",shape_type=2)
            else:
                rect_size = turbo_pygame.vector(obj_size * 2, obj_size * 2)
                obj = turbo_pygame.Object(pos, rect_size,image="default",shape_type=1)

            obj.add_physics()
            obj.add_script(self.Assets.get("scripts","test"))
            self.objects.add(obj)

        # Walls (ground, top, left, right)
        wall_thickness = 10
        half_thickness = wall_thickness / 2

        # Ground
        ground_size = turbo_pygame.vector(world_size.x, wall_thickness)
        ground_pos = turbo_pygame.vector(box_center.x, box_center.y + half_world.y + half_thickness)
        ground = turbo_pygame.Object(ground_pos, ground_size, shape_type=1)
        ground.add_physics(static=True)
        self.objects.add(ground)

        # Top wall
        top_wall_pos = turbo_pygame.vector(box_center.x, box_center.y - half_world.y - half_thickness)
        top_wall = turbo_pygame.Object(top_wall_pos, ground_size, shape_type=1)
        top_wall.add_physics(static=True)
        self.objects.add(top_wall)

        # Left wall
        left_wall_size = turbo_pygame.vector(wall_thickness, world_size.y)
        left_wall_pos = turbo_pygame.vector(box_center.x - half_world.x - half_thickness, box_center.y)
        left_wall = turbo_pygame.Object(left_wall_pos, left_wall_size, shape_type=1)
        left_wall.add_physics(static=True)
        self.objects.add(left_wall)

        # Right wall
        right_wall_pos = turbo_pygame.vector(box_center.x + half_world.x + half_thickness, box_center.y)
        right_wall = turbo_pygame.Object(right_wall_pos, left_wall_size, shape_type=1)
        right_wall.add_physics(static=True)
        self.objects.add(right_wall)