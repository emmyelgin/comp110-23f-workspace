"""River simulation."""

from exercise.ex08.river import river

_author_ = "730464992"

my_river = river(num_fish=10, num_bears=2)

my_river.view_river()

my_river.one_river_day()

my_river.one_river_week()