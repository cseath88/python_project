import pdb
from models.game import Game
from models.platform import Platform

import repositories.game_repository as game_repository
import repositories.platform_repository as platform_repository


game_repository.delete_all()
platform_repository.delete_all()


platform1 = Platform("PC")
platform_repository.save(platform1)

platform2 = Platform("PS5")
platform_repository.save(platform2)

platform3 = Platform("Xbox")
platform_repository.save(platform3)

platform4 = Platform("Nintendo Switch")
platform_repository.save(platform4)



game1 = Game("Half-Life 2", "Half-Life 2 is a 2004 first-person shooter (FPS) game developed by Valve.", "10", "5.00", "9.00", platform1)
game_repository.save(game1)

game2 = Game("Escape From Tarkov", "Escape from Tarkov is a multiplayer tactical first-person shooter video game.", "20", "10.00", "15.00", platform1)
game_repository.save(game2)

game3 = Game("Bloodborne", "Bloodborne is a souls game developed by FromSoftware.", "53", "12.00", "25.00", platform2)
game_repository.save(game3)

game4 = Game("The Last Of Us", "The Last of Us is a 2013 action-adventure game developed by Naughty Dog.", "36", "28.00", "30.00", platform2)
game_repository.save(game4)

game5 = Game("Super Mario Odyssey", "Super Mario Odyssey is a 2017 platform game developed and published by Nintendo.", "0", "26.00", "45.00", platform4)
game_repository.save(game5)

game6 = Game("Xenoblade Chronicles 2", "Xenoblade Chronicles 2[a] is a 2017 action role-playing game developed by Monolith Soft.", "12", "22.00", "40.00", platform4)
game_repository.save(game6)

game7 = Game("Halo Infinite", "Halo Infinite is a 2021 first-person shooter game developed by 343 Industries.", "27", "40.00", "60.00", platform3)
game_repository.save(game7)

game8 = Game("Forza Horizon 5", "Forza Horizon 5 is a 2021 racing video game developed by Playground Games.", "48", "46.00", "65.99", platform3)
game_repository.save(game8)
