# MakeCode https://makecode.com/_YqHLw7KEXg0X

# viens stabs
def build_pillar(height):
    for x in range(height):
        agent.move(UP, 1)
        agent.place(DOWN)
    agent.move(FORWARD, 1)
    agent.move(DOWN, height)

# viena siena
def build_wall(height, length):
    for x in range(length - 1):
        build_pillar(height)

# 4 sienas
def build_walls(height, length):
    player.say("Building walls, height " + height + ", length + " + length)
    agent.set_item(STONE_BRICKS, 64, 1)
    agent.set_slot(1)
    # 4 sienas
    for s in range(4):
        build_wall(height, length)
        agent.turn(LEFT_TURN)

# buildwalls čata komanda
def on_build_walls(height, length):
    build_walls(height, length)
player.on_chat("buildwalls", on_build_walls)

# grīda
def build_floor(length, width):
    player.say("Building floor, length " + length + ", width + " + width)
    agent.move(UP, 1)
    for w in range(width):
        # viena līnija
        for l in range(length):
            agent.place(DOWN)
            agent.move(FORWARD, 1)
        agent.move(LEFT, 1)
        agent.move(BACK, length)
        
# buildfloor čata komanda
def on_build_floor(length, width):
    build_floor(length, width)
player.on_chat("buildfloor", on_build_floor)

# māja
def on_build_house(height, length):
    build_floor(length, length)
    agent.move(RIGHT, length)
    build_walls(height, length)
    build_floor(length, length)

player.on_chat("buildhouse", on_build_house)
