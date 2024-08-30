from snake import fragmentData, Fragment


def basisSnake():
    initialsnake = []
    for i in fragmentData:
        fragment = Fragment(i["turtle"], i["color"], i["shape"], i["position"])
        initialsnake.append(fragment)
    return initialsnake
