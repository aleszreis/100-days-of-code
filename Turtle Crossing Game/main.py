import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Scoreboard()

loop = 6

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()
    car_manager.generate_new_car()
    car_manager.move_cars()

    for car in car_manager.cars:
        if player.distance(car) < 20:
            score.game_over_message()
            game_is_on = False

    if player.is_finish_line():
        player.go_to_start()
        car_manager.level_up()
        score.set_level()

screen.exitonclick()

