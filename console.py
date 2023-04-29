import pdb
from models.game import Game
from models.platform import Platform

import repositories.game_repository as game_repository
import repositories.platform_repository as platform_repository



platform1 = Platform("PC")
platform_repository.save(platform1)

platform2 = Platform("PS5")
platform_repository.save(platform2)

platform3 = Platform("Xbox")
platform_repository.save(platform3)

game_repository.select_all()

game1 = Game("Half-Life 2", "Half-Life 2 is a 2004 first-person shooter (FPS) game developed by Valve.", "10", "5.00", "9.00", platform1)
game_repository.save(game1)

game2 = Game("Escape From Tarkov", "Escape from Tarkov is a multiplayer tactical first-person shooter video game.", "20", "10.00", "15.00", platform1)
game_repository.save(game2)

game3 = Game("Bloodborne", "Bloodborne is a souls game developed by FromSoftware.", "20", "10.00", "15.00", platform2)
game_repository.save(game3)

