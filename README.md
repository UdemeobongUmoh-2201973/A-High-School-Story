# A-High-School-Story

TITLE: A HIGH SCHOOL STORY
Genre: Strategy

Dear Python programmer,
This is a project for a game development competition.

It is required for you to see this before you start coding.

Based on the scene management used, there is a particular way required to code each scene.

The full game object is found in game_object.py as the FullGameObject class.
Each scene has its own string_id and method.
For instance, the home scene has an id "home" and method home_scene(self).

FORMAT:
def demo_scene(self):
    self.current_scene = "scene_id"

    # In-scene variables and objects

    while self.app and self.current_scene == "scene_id":
        # drawing functions

        pygame.display.update()
        Clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.app = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # code
            elif event.type == pygame.KEYDOWN:
                self.current_scene = "new_scene_id"    # this is to change to a different scene

Note:
When creating a scene, make sure to:
1. Write the scene as a method using the format above
2. In self.scenes_dict, make sure you add the new scene and its ID to the dictionary.  

REFERENCE CODE:
GUI Widgets: check gui.py
For Specific Game objects and variables: check objects.py and variables.py
