## greet
* greet
    - utter_greet
    - utter_ask_howcanhelp
    - action_listen
> greeted

> greeted
* director_name{"movie.name": "spider-man"}
    - slot{"movie.name": "spider-man"}
    - action_search_director
    - slot{"director.name": "Sam Raimi"}
> searched_movie

> greeted
* movie
    - action_search_movie
> searched_movie


> greeted
* release_date{"movie.name": "back to the future"}
    - slot{"movie.name": "back to the future"}
    - action_search_year
    - slot{"movie.release_date": "1985"}
> searched_movie

> greeted
* actor_name{"movie.name": "spider-man"}
    - slot{"movie.name": "spider-man"}
    - action_search_actor
    - slot{"actor.name": "James Franco"}
> searched_movie

> greeted
* genre{"movie.name": "spider-man"}
    - slot{"movie.name": "spider-man"}
    - action_search_genre
    - slot{"movie.genre": "Action"}
> searched_movie

> greeted
* country{"movie.name": "spider-man"}
    - slot{"movie.name": "spider-man"}
    - action_search_country
    - slot{"movie.location":"USA"}
> searched_movie

> greeted
* language{"movie.name": "spider-man"}
    - slot{"movie.name": "spider-man"}
    - action_search_language
    - slot{"movie.language": "English"}
> searched_movie

> greeted
* gross{"movie.name": "spider-man"}
    - slot{"movie.name": "spider-man"}
    - action_search_gross
    - slot{"movie.gross": 42424242}
> searched_movie

> greeted
* budget{"movie.name": "spider-man"}
    - slot{"movie.name": "spider-man"}
    - action_search_budget
    - slot{"movie.budget": 424242}
> searched_movie

> greeted
* star_rating{"movie.name": "spider-man"}
    - slot{"movie.name": "spider-man"}
    - action_search_rating
    - slot{"movie.star_rating": 7.0}
> searched_movie

> greeted
* runtime{"movie.name": "spider-man"}
    - slot{"movie.name": "spider-man"}
    - action_search_duration
    - slot{"movie.runtime": 121}
> searched_movie


> searched_movie
* release_date
    - action_search_year
    - slot{"movie.release_date": "2010"}
> searched_again

> searched_movie
* runtime
    - action_search_duration
    - slot{"movie.runtime": 120}
> searched_again

> searched_movie
* goodbye
    - utter_goodbye
> greeted
> searched_again
* goodbye
    - utter_goodbye



