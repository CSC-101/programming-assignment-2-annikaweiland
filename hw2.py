from operator import truediv

import data

# Write your functions for each part in the space below.

# Part 1
#input: two inputs of class Point.
#output: One output of class Rectangle.
#purpose: To create a rectangle output that matches up the bottom right and top left from the inputs.
def create_rectangle(input1: data.Point, input2 = data.Point) -> data.Rectangle:
    if input1.x > input2.x:
        bottomright_x = input1.x
        topleft_x = input2.x
    else:
        bottomright_x = input2.x
        topleft_x = input1.x

    if input1.y > input2.y:
        topleft_y = input1.y
        bottomright_y = input2.y
    else:
        topleft_y = input2.y
        bottomright_y = input1.y

    top_left = data.Point(topleft_x, topleft_y)
    bottom_right = data.Point(bottomright_x, bottomright_y)

    return data.Rectangle(top_left, bottom_right)

# Part 2
#input: two inputs of class type Duration.
#output: a boolean output, returning true if the first inputted time is less than the 2nd inputted time.
#purpose: To find out if one input is a shorter duration than the other input.
def shorter_duration_than(input1: data.Duration, input2: data.Duration) -> bool:
    total_time_1 = input1.minutes*60 + input1.seconds
    total_time_2 = input2.minutes*60 + input2.seconds
    if total_time_1<total_time_2:
        return True
    else:
        return False

# Part 3
#input: two inputs, one a list of class Songs, then another input of class Duration.
#output: A list of songs that are shorter than the inputted duration.
#purpose: To determine the songs from the inputted list that are shorter than the given duration.
def songs_shorter_than(songs: list[data.Song], time: data.Duration) -> list[data.Song]:
    #return [song for song in songs if shorter_duration_than(song.duration, time)]
    return [song for song in songs if shorter_duration_than(song.duration, time)]

# Part 4
#input: Two inputs, one of a list of class Songs, then the other is a list of integers. The list of integers (if appropriate numbers) corresponds to the indicies of songs that will be in a playlist.
#output: the total duration of the playlist.
#purpose: to find the total duration of a playlist (playlist is made up of the indicies given in the ints input)
def running_time(songs: list[data.Song], ints: list[int]) -> data.Duration:
    total_mins = 0
    total_secs = 0
    for i in ints:
       if i>len(songs)-1:
           return "integer in inputted playlist doesn't match with inputted songs index"
    for i in ints:
        if i<0:
            return "integers must be positive."
    for num in ints:
        song = songs[num]
        total_mins = total_mins + song.duration.minutes
        total_secs = total_secs + song.duration.seconds
    if total_secs>60:
        minss = total_secs//60
        total_mins = total_mins + minss
        total_secs = total_secs - minss*60
    return data.Duration(total_mins, total_secs)

# Part 5
#input: two inputs - one is a list of lists (that contain str), which are connections between cities/places. The other input is the given travel plan
#output: Boolean output - if travel plan works with given connections in city_links
#purpose: To determine if a travel plan is valid with the given city_links
def validate_route(city_links: list[list[str]], input: list[str]) -> bool:
   if len(input) <= 1:
       return True
   for i in range(1, len(input)):
       curr_city = input[i]
       prev_city = input[i-1]
       if [curr_city, prev_city] not in city_links and [prev_city, curr_city] not in city_links:
           return False
   else:
       return True

# Part 6
#input: a list of integers
#output: the index at the start of the longest repitition of an integer.
#purpose: To determine the longest repitition of an integer.
def longest_repitition(input: list[int]) -> [int]:
    if len(input)==0:
        return None
    max_list_count = 0
    max_list_type = 0
    num_list = 1
    num_type = 0
    max_starting_index = 0
    for i in range((len(input)-1)):
        if input[i+1] == input[i]:
            num_list = num_list+1
            num_type = input[i]
            if num_list>max_list_count:
                max_list_count = num_list
                max_list_type = num_type
                max_starting_index = i-num_list+2
        else:
            num_list = 1
            num_type = 0

    return max_starting_index



