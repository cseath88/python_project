import pdb
from models.game import Game
from models.platform import Platform

import repositories.game_repository as game_repository
import repositories.platform_repository as platform_repository


platform1 = Platform("PC")
platform_repository.save(platform1)
platform2 = Platform("PS5")
platform_repository.save(platform2)


game1 = Game("Half-Life 2", "Half-Life 2 is a 2004 first-person shooter (FPS) game developed by Valve.", "10", "5.00", "9.00", platform1)
game_repository.save(game1)
game2 = Game("Bloodborne", "Bloodborne is a 2015 action role-playing game developed by FromSoftware", "50", "10.00", "20.00", platform2)

