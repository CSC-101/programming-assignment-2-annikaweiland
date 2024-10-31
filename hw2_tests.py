import data
import hw2
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle(self):
        Point1 = data.Point(2, 2)
        Point2 = data.Point(10, 10)
        expected = data.Rectangle(data.Point(2,10), data.Point(10,2))
        result = hw2.create_rectangle(Point1, Point2)
        self.assertEqual(expected, result)

    def test_create_rectangle_2(self):
        Point1 = data.Point(20, 15)
        Point2 = data.Point(6, 8)
        expected = data.Rectangle(data.Point(6,15), data.Point(20,8))
        result = hw2.create_rectangle(Point1, Point2)
        self.assertEqual(expected, result)
    # Part 2

    def test_shorter_duration_than(self):
        duration1 = data.Duration(6, 53)
        duration2 = data.Duration(5, 7)
        expected = False
        result = hw2.shorter_duration_than(duration1, duration2)
        self.assertEqual(expected, result)

    def test_shorter_duration_than_2(self):
        duration1 = data.Duration(3, 53)
        duration2 = data.Duration(5, 7)
        expected = True
        result = hw2.shorter_duration_than(duration1, duration2)
        self.assertEqual(expected, result)

    # Part 3

    def test_songs_shorter_than(self):
        song1 = data.Song("Katy perry", "teenage dream", data.Duration(2, 30))
        song2 = data.Song("taylor swift", "22", data.Duration(3, 45))
        song3 = data.Song("post malone", "congratulations", data.Duration(5, 34))
        songlist = [song1, song2, song3]
        time = data.Duration(4, 40)
        expected = [data.Song('Katy perry', 'teenage dream', data.Duration(2, 30)), data.Song('taylor swift', '22', data.Duration(3, 45))]
        result = hw2.songs_shorter_than(songlist, time)
        self.assertEqual(expected, result)

    def test_songs_shorter_than_2(self):
        song1 = data.Song("Madeline Cordaro", "lalalala", data.Duration(200, 30))
        song2 = data.Song("Owen Lockery", "lelelele", data.Duration(3, 45))
        song3 = data.Song("John Locked", "I love python!", data.Duration(5, 34))
        songlist = [song1, song2, song3]
        time = data.Duration(30, 40)
        expected = [data.Song('Owen Lockery', 'lelelele', data.Duration(3, 45)), data.Song('John Locked', 'I love python!', data.Duration(5, 34))]
        result = hw2.songs_shorter_than(songlist, time)
        self.assertEqual(expected, result)


    # Part 4
    def test_running_time(self):
        song4 = data.Song("Madeline Cordaro", "lalalala", data.Duration(200, 30))
        song2 = data.Song("Owen Lockery", "lelelele", data.Duration(3, 45))
        song3 = data.Song("John Locked", "I love python!", data.Duration(5, 34))
        mysongs =[song4, song2, song3]
        ints = [0, 1, 0, 2, 2]
        result = hw2.running_time(mysongs, ints)
        expected = data.Duration(415, 53)
        self.assertEqual(expected, result)

    def test_running_time_2(self):
        song4 = data.Song("Madeline Cordaro", "lalalala", data.Duration(200, 30))
        song2 = data.Song("Owen Lockery", "lelelele", data.Duration(200, 45))
        mysongs =[song4, song2]
        ints = [0, 1, 0, 2, 2, 4] #FINISHHHHHHHHH
        result = hw2.running_time(mysongs, ints)
        expected = "integer in inputted playlist doesn't match with inputted songs index"
        self.assertEqual(expected, result)

    # Part 5

    def test_validate_route(self):
        cities = [['Tijuana', 'San Diego'], ["Los Angeles", "San Diego"], ["Los Angeles", "San Luis Obispo"]]
        input = ["Tijuana", "San Diego", "Los Angeles", "San Luis Obispo"]
        result = hw2.validate_route(cities, input)
        expected = True
        self.assertEqual(result, expected)

    def test_validate_route_2(self):
        cities = [["LA", "SF"], ["SF", "Portland"], ["Portland", "Stockholm"]]
        input = ["LA", "Stockholm"]
        result = hw2.validate_route(cities, input)
        expected = False
        self.assertEqual(result, expected)

    # Part 6
    def test_longest_repitition(self):
        input = [4, 4, 5, 5, 5, 3, 5, 7, 7, 7, 7]
        result = hw2.longest_repitition(input)
        expected = 7
        self.assertEqual(expected, result)

    def test_longest_repitition_2(self):
        input = [5, 5, 5, 5, 5, 5, 2, 3, 3, 4]
        result = hw2.longest_repitition(input)
        expected = 0
        self.assertEqual(expected, result)



if __name__ == '__main__':
    unittest.main()
