


def timerFired(mode):
    mode.x1 = random.randint(20, mode.width)
    mode.y1 = randomg.randint(20, mode.height)
    mode.x2 = mode.x1 + 70
    mode.y2 = mode.y1 + 12
    newPlatform = (mode.x1, mode.y1, mode.x2, mode.y2)
    if len(mode.platforms) < 10:
        if mode.checkPlatform(newPlatform):
            mode.platforms.append(newPlatform)

def checkPlatform(mode, newPlatform):
    if (within the bounds):
        return True
    else:
        return False
