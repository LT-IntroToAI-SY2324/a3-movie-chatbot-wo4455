from movies import movie_db
from match import match
from typing import List, Tuple, Callable, Any

def get_title(movie: Tuple[str, str, int, List[str]]) -> str:
    return movie[0]



def get_director(movie: Tuple[str, str, int, List[str]]) -> str:
    return movie[1]


def get_year(movie: Tuple[str, str, int, List[str]]) -> int:
    return movie[2]


def get_actors(movie: Tuple[str, str, int, List[str]]) -> List[str]:
    return movie[3]



def title_by_year(matches: List[str]) -> List[str]:
    
    results = []
    for movie in movie_db:
        if int(matches[0]) == get_year(movie):
            # print(get_title(movie))
            results.append(get_title(movie))
    return results

def title_by_year_range(matches: List[str]) -> List[str]:
    
    results = []
    for movie in movie_db:
        if int(matches[0]) <= get_year(movie) <= int(matches[1]):
            results.append(get_title(movie))
    return results


def title_before_year(matches: List[str]) -> List[str]:
    
    results = []
    for movie in movie_db:
        if get_year(movie) < int(matches[0]):
            results.append(get_title(movie))
    return results


def title_after_year(matches: List[str]) -> List[str]:
    
    results = []
    for movie in movie_db:
        if get_year(movie) > int(matches[0]):
            results.append(get_title(movie))
    return results


def director_by_title(matches: List[str]) -> List[str]:

    results = []
    for movie in movie_db:
        if get_title(movie) == matches[0]:
            results.append(get_director(movie))
    return results


def title_by_director(matches: List[str]) -> List[str]:

    results = []
    for movie in movie_db:
        if get_director(movie) == matches[0]:
            results.append(get_title(movie))
    return results


def actors_by_title(matches: List[str]) -> List[str]:
    
    results = []
    for movie in movie_db:
        if get_title(movie) == matches[0]:
            results = get_actors(movie)
    return results


def year_by_title(matches: List[str]) -> List[int]:
    
    results = []
    for movie in movie_db:
        if get_title(movie) == matches[0]:
            results.append(get_year(movie))
    return results


def title_by_actor(matches: List[str]) -> List[str]:
   
    results = []
    for movie in movie_db:
        if matches[0] in get_actors(movie):
            results.append(get_title(movie))
    return results

def movies_by_genre(matches: List[str]) -> List[str]:
    """Finds movies that belong to a specific genre.
    Args:
        matches - a list of 1 string, which is the genre to search for.
    Returns:
        a list of movie titles in that genre.
    """
    genre = matches[0].lower()
    results = []
    for movie in movie_db:
        if genre in [g.lower() for g in movie[3]]:
            results.append(get_title(movie))
    return results



def bye_action(dummy: List[str]) -> None:
    raise KeyboardInterrupt



pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("what movies were made in _"), title_by_year),
    (str.split("what movies were made between _ and _"), title_by_year_range),
    (str.split("what movies were made before _"), title_before_year),
    (str.split("what movies were made after _"), title_after_year),
   
    (str.split("who directed %"), director_by_title),
    (str.split("who was the director of %"), director_by_title),
    (str.split("what movies were directed by %"), title_by_director),
    (str.split("who acted in %"), actors_by_title),
    (str.split("when was % made"), year_by_title),
    (str.split("% appeared in what movies"), title_by_actor),
    (str.split("in what movies did % appear"), title_by_actor),

    (str.split("movies in the genre _"), movies_by_genre),
    (["bye"], bye_action),
]


def search_pa_list(src: List[str]) -> List[str]:
    
    for pat, act in pa_list:
        mat = match(pat, src)
        if mat is not None:
            answer = act(mat)
            return answer if answer else ["No answers"]   
    return ["I don't understand"]


def query_loop() -> None:
    
    print("Welcome to the movie database!\n")
    while True:
        try:
            print()
            query = input("Your query? ").replace("?", "").lower().split()
            answers = search_pa_list(query)
            for ans in answers:
                print(ans)

        except (KeyboardInterrupt, EOFError):
            break

    print("\nSo long!\n")

query_loop()

if __name__ == "__main__":
    assert isinstance(title_by_year(["1974"]), list), "title_by_year not returning a list"
    assert isinstance(title_by_year_range(["1970", "1972"]), list), "title_by_year_range not returning a list"
    assert isinstance(title_before_year(["1950"]), list), "title_before_year not returning a list"
    assert isinstance(title_after_year(["1990"]), list), "title_after_year not returning a list"
    assert isinstance(director_by_title(["jaws"]), list), "director_by_title not returning a list"
    assert isinstance(title_by_director(["steven spielberg"]), list), "title_by_director not returning a list"
    assert isinstance(actors_by_title(["jaws"]), list), "actors_by_title not returning a list"
    assert isinstance(year_by_title(["jaws"]), list), "year_by_title not returning a list"
    assert isinstance(title_by_actor(["orson welles"]), list), "title_by_actor not returning a list"
    
    assert sorted(title_by_year(["1974"])) == sorted(
        ["amarcord", "chinatown"]
    ), "failed title_by_year test"
    assert sorted(title_by_year_range(["1970", "1972"])) == sorted(
        ["the godfather", "johnny got his gun"]
    ), "failed title_by_year_range test"
    assert sorted(title_before_year(["1950"])) == sorted(
        ["casablanca", "citizen kane", "gone with the wind", "metropolis"]
    ), "failed title_before_year test"
    assert sorted(title_after_year(["1990"])) == sorted(
        ["boyz n the hood", "dead again", "the crying game", "flirting", "malcolm x"]
    ), "failed title_after_year test"
    assert sorted(director_by_title(["jaws"])) == sorted(
        ["steven spielberg"]
    ), "failed director_by_title test"
    assert sorted(title_by_director(["steven spielberg"])) == sorted(
        ["jaws"]
    ), "failed title_by_director test"
    assert sorted(actors_by_title(["jaws"])) == sorted(
        [
            "roy scheider",
            "robert shaw",
            "richard dreyfuss",
            "lorraine gary",
            "murray hamilton",
        ]
    ), "failed actors_by_title test"
    assert sorted(actors_by_title(["movie not in database"])) == [], "failed actors_by_title not in database test"
    assert sorted(year_by_title(["jaws"])) == sorted(
        [1975]
    ), "failed year_by_title test"
    assert sorted(title_by_actor(["orson welles"])) == sorted(
        ["citizen kane", "othello"]
    ), "failed title_by_actor test"
    assert sorted(search_pa_list(["hi", "there"])) == sorted(
        ["I don't understand"]
    ), "failed search_pa_list test 1"
    assert sorted(search_pa_list(["who", "directed", "jaws"])) == sorted(
        ["steven spielberg"]
    ), "failed search_pa_list test 2"
    assert sorted(
        search_pa_list(["what", "movies", "were", "made", "in", "2020"])
    ) == sorted(["No answers"]), "failed search_pa_list test 3"
    assert sorted(movies_by_genre(["drama"])) == sorted(
        ["casablanca", "citizen kane", "gone with the wind", "the godfather", "the shawshank redemption"]
    ), "failed movies_by_genre test"

    print("All tests passed!")