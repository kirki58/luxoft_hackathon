from collections import deque
import grid
import json

def bfs(matrix, start, goal):
    q = deque()
    q.append(start)

    # Left, up, right, down in specified order.
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    matrixWidth = len(matrix[0])  # Number of columns
    matrixHeight = len(matrix)    # Number of rows

    distancesArray = [[-1 for _ in range(matrixWidth)] for _ in range(matrixHeight)]
    parentArray = [[None for _ in range(matrixWidth)] for _ in range(matrixHeight)]  # To store parent positions

    distancesArray[start[1]][start[0]] = 0  # Initialize start position with distance 0

    while q:
        point = q.popleft()

        # Loop through the 4 directions of movement
        for i in range(4):
            x = point[0] + dx[i]
            y = point[1] + dy[i]

            # Check if the point is within grid boundaries
            if 0 <= y < matrixHeight and 0 <= x < matrixWidth:
                # If the cell is not visited and is not an obstacle
                if distancesArray[y][x] == -1 and matrix[y][x] != 2:
                    distancesArray[y][x] = distancesArray[point[1]][point[0]] + 1
                    parentArray[y][x] = (point[0], point[1])  # Store the parent of the current cell
                    q.append((x, y))

                    # If goal is found, backtrack the path
                    if (x, y) == goal:
                        path = []
                        current = (x, y)
                        while current != start:
                            path.append(current)
                            current = parentArray[current[1]][current[0]]  # Move to the parent
                        path.append(start)  # Add the start position
                        return path[::-1]  # Reverse the path to get it from start to goal

    return None  # Return None if no path found

def markSpace(matrix, x, y, width, height):
        for i in range(x, x + width):
            for j in range(y, y + height):
                matrix[j][i] = 4

# Distance and parking space size is considered to give an overall point to each parking space in this function
def findOptimalParkingSpot(matrix, start, distanceImportance, parkingAreaImportance):
    if(distanceImportance < 0 or parkingAreaImportance < 0):
        print("Invalid importance values. Please make sure that the sum of importance values is 1 and both values are greater than 0.")
        exit(-1)

    parkingSpaces = json.load(open('testCases/case2.json'))["parkables"]
    optimalParkingSpot = None

    prevPoint = None
    for parkingSpace in parkingSpaces:
        top_left_x, top_left_y = parkingSpace["position"]
        parkingSpaceWidth, parkingSpaceHeight = parkingSpace["size"]

        # Calculate the distance from the agent to the parking space
        distance = len(bfs(matrix, start, (top_left_x, top_left_y)))

        # Calculate the size of the parking space
        parkingArea = parkingSpaceWidth * parkingSpaceHeight

        # Calculate the overall point of the parking space

        data = json.load(open('testCases/case2.json'))
        maxDistance = data["width"] + data["height"]
        maxParkingArea = data["width"] * data["height"]

        normalizedDistance = distance / maxDistance
        normalizedParkingArea = parkingArea / maxParkingArea

        point = distanceImportance * (1 - normalizedDistance) + parkingAreaImportance * normalizedParkingArea
        if prevPoint is None or point > prevPoint:
            prevPoint = point
            optimalParkingSpot = parkingSpace

    markSpace(matrix, optimalParkingSpot["position"][0], optimalParkingSpot["position"][1], optimalParkingSpot["size"][0], optimalParkingSpot["size"][1])
    return optimalParkingSpot
