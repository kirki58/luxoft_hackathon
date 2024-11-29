import grid
import json
import algorithms

environmentGrid = grid.Grid() # Create a grid with specified parameters (in testCases/caseN.json).

agentStartData = json.load(open('testCases/case2.json'))["agent"]["position"] # Get the starting position of the agent from the json file.
agentStart = (agentStartData[0], agentStartData[1]) # Convert the agent's starting position to a tuple.

# optimalParkingSpot = algorithms.findOptimalParkingSpot(environmentGrid.matrix, agentStart, 0.5, 0.5) # Find the optimal parking spot for the agent.
# print("Optimal parking spot: ", optimalParkingSpot) # Print the optimal parking spot.

mostOptimalSpace = algorithms.findOptimalParkingSpot(environmentGrid.matrix, agentStart, 0.1, 0.9) # Find the most optimal parking spot for the agent.

print(mostOptimalSpace) # Find the path from the agent to the specified goal.

environmentGrid.display() # Display the grid.

