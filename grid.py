import matplotlib.pyplot as plt
import json

data = json.load(open('testCases/case2.json')) # define which case to use here!

class Grid:
    def __init__(self):
        self.matrix = [[0 for _ in range(data["width"])] for _ in range(data["height"])] # use list comprehension to create a 2D array with given parameters.
        self.placeParkables() # place the parkables in the scene
        self.placeObstacles() # place the obstacles in the scene
        self.placeAgent() # place the agent in the scene

    def display(self):
        plt.imshow(self.matrix, cmap='viridis', interpolation='nearest') # Display the grid using a heat map. "Purples" is the color set used, and "nearest" is the interpolation method used (no blending).
        plt.colorbar()
        plt.title("Grid Visualization")

        plt.show() # Display the plot.

    def placeParkables(self):
        # Placing the parkables:
        # Obstacles are defined by x, y positions and their width and height.
        # Loop through each defined obstacle in json
        # top_left_x -> top_left_x + parkable_width = 1
        # top_left_y -> top_left_y + parkable_height = 1
        for parkable in data["parkables"]:
            top_left_x, top_left_y = parkable["position"]
            parkable_width, parkable_height = parkable["size"]

            for i in range(top_left_x, top_left_x + parkable_width):
                for j in range(top_left_y, top_left_y + parkable_height):
                    if(self.matrix[j][i] != 0):
                        print("Parkable overlap detected at position: ", i, j)
                        exit(-1)

                    self.matrix[j][i] = 1
    
    def placeObstacles(self):
        for obstacle in data["obstacles"]:
            top_left_x, top_left_y = obstacle["position"]
            obstacle_width, obstacle_height = obstacle["size"]

            for i in range(top_left_x, top_left_x + obstacle_width):
                for j in range(top_left_y, top_left_y + obstacle_height):
                    if(self.matrix[j][i] != 0):
                        print("Obstacle overlap detected at position: ", i, j)
                        exit(-1)

                    self.matrix[j][i] = 2
            
    def placeAgent(self):
        top_left_x, top_left_y = data["agent"]["position"]
        agent_width, agent_height = data["agent"]["size"]

        for i in range(top_left_x, top_left_x + agent_width):
            for j in range(top_left_y, top_left_y + agent_height):
                if(self.matrix[j][i] != 0):
                        print("Agent overlap detected at position: ", i, j)
                        exit(-1)

                self.matrix[j][i] = 3