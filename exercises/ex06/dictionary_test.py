"""Dictionary Testing."""

from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance

_author_ = "730464992"


def test_invert_expected_1():
    """Test inverts expected output."""
    dictionary = {'a': 'apple', 'b': 'banana', 'c': 'coconut'}
    expected_output = {'apple': 'a', 'banana': 'b', 'coconut': 'c'}
    assert invert(dictionary) == expected_output


def test_invert_expected_2():
    """Test invert expected outcome part 2."""
    dictionary = {'x': 'xylophone', 'y': 'yellow', 'z': 'zebra'}
    expected_output = {'xylophone': 'x', 'yellow': 'y', 'zebra': 'z'}
    assert invert(dictionary) == expected_output


def test_invert_edge():
    """Test invert with an empty dictionary."""
    dictionary = {}  # Empty dictionary
    expected_output = {}
    assert invert(dictionary) == expected_output


def test_favorite_color_expected_1():
    """Test favorite color function with an expected color."""
    color_data = {'Tomato': 'red', 'Ocean': 'blue', 'Apple': 'red', 'Grass': 'green'}
    expected_color = 'red'
    assert favorite_color(color_data) == expected_color


def test_favorite_color_expected_2():
    """Test favorite color function with an expected color part two."""
    color_data = {'Ocean': 'blue', 'Grass': 'green', 'Lemon': 'yellow'}
    expected_color = 'blue'
    assert favorite_color(color_data) == expected_color


def test_favorite_color_edge():
    """Test favorite color function with an empty dictionary."""
    color_data = {}  # Empty dictionary
    expected_color = ''
    assert favorite_color(color_data) == expected_color


def test_count_expected_1():
    """Test if the count function correctly counts the number of occurence of a value in the list."""
    values = ['apple', 'banana', 'apple', 'coconut', 'banana']
    expected_count = {'apple': 2, 'banana': 2, 'coconut': 1}
    assert count(values) == expected_count


def test_count_expected_2():
    """Test count function again."""
    values = ['red', 'blue', 'green', 'blue']
    expected_count = {'red': 1, 'blue': 2, 'green': 1}
    assert count(values) == expected_count


def test_count_edge():
    """Test count with an empty dictionary."""
    values = []  # Empty list
    expected_count = {}
    assert count(values) == expected_count


def test_alphabetizer_expected_1():
    """Test alphabetizer and if it puts values in alphabetical order."""
    words = ['apple', 'banana', 'coconut', 'avocado']
    expected_output = {'a': ['apple', 'avocado'], 'b': ['banana'], 'c': ['coconut']}
    assert alphabetizer(words) == expected_output


def test_alphabetizer_expected_2():
    """Test alphabetizer and alphabetical order again."""
    words = ['zebra', 'yacht', 'xylophone']
    expected_output = {'z': ['zebra'], 'y': ['yacht'], 'x': ['xylophone']}
    assert alphabetizer(words) == expected_output


def test_alphabetizer_edge():
    """Test alphabetizer with an empty dictionary."""
    words = []  # Empty list
    expected_output = {}
    assert alphabetizer(words) == expected_output


def test_update_attendance_expected_1():
    """Tests if the update attendance function correctly adds student to the attendance."""
    students = {'Monday': ['Alice', 'Brian'], 'Tuesday': ['Charlie']}
    day = 'Monday'
    student = 'David'
    expected_updated_attendance = {'Monday': ['Alice', 'Brian', 'David'], 'Tuesday': ['Charlie']}
    assert update_attendance(students, day, student) == expected_updated_attendance


def test_update_attendance_expected_2():
    """Test if the update attendance function again correctly adds a student."""
    students = {'Monday': ['Alice', 'Alice'], 'Wednesday': ['Alice']}
    day = 'Tuesday'
    student = 'Frank'
    expected_updated_attendance = {'Monday': ['Alice', 'Alice'], 'Wednesday': ['Alice'], 'Tuesday': ['Frank']}
    assert update_attendance(students, day, student) == expected_updated_attendance


def test_update_attendance_edge():
    """Tests update attendace with an empty dictionay but then adds a value."""
    students = {}  # Empty dictionary
    day = 'Monday'
    student = 'Alice'
    expected_updated_attendance = {'Monday': ['Alice']}
    assert update_attendance(students, day, student) == expected_updated_attendance
