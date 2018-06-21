## story 0
* greet
    - utter_greet
    - utter_ask_howcanhelp
* goodbye
    - utter_goodbye

## story 1
* greet
    - utter_greet
    - utter_ask_howcanhelp
    - action_listen
* director_name{"movie.name": "spider-man"}
    - slot{"movie.name": "spider-man"}
    - action_search_director
    - slot{"director.name": "Sam Raimi"}
* goodbye
    - utter_goodbye

## story 1.2
* greet
    - utter_greet
    - utter_ask_howcanhelp
    - action_listen
* director_name{"movie.name": "spider-man"}
    - slot{"movie.name": "spider-man"}
    - action_search_director
    - slot{"director.name": "Sam Raimi"}
* runtime
    - action_search_duration
    - slot{"movie.runtime": 120}

## story 2
* greet
    - utter_greet
    - utter_ask_howcanhelp
    - action_listen
* release_date{"movie.name": "back to the future"}
    - slot{"movie.name": "back to the future"}
    - action_search_year
    - slot{"movie.release_date": "1985"}
* goodbye
    - utter_goodbye

## story 2.2
* greet
    - utter_greet
    - utter_ask_howcanhelp
    - action_listen
* release_date{"movie.name": "back to the future"}
    - slot{"movie.name": "back to the future"}
    - action_search_year
    - slot{"movie.release_date": "1985"}
* director_name
    - action_search_director
    - slot{"director.name": "Robert Zemeckis"}
* goodbye
    - utter_goodbye

## story 3
* greet
    - utter_greet
    - utter_ask_howcanhelp
    - action_listen
* actor_name{"movie.name": "spider-man"}
    - slot{"movie.name": "spider-man"}
    - action_search_actor
    - slot{"actor.name": "James Franco"}
* goodbye
    - utter_goodbye

## story 3.1
* greet
    - utter_greet
    - utter_ask_howcanhelp
    - action_listen
* actor_name{"movie.name": "spider-man"}
    - slot{"movie.name": "spider-man"}
    - action_search_actor
    - slot{"actor.name": "James Franco"}
* budget
    - action_search_budget
    - slot{"movie.budget": 424242}

## story 4
* greet
    - utter_greet
    - utter_ask_howcanhelp
    - action_listen
* genre{"movie.name": "spider-man"}
    - slot{"movie.name": "spider-man"}
    - action_search_genre
    - slot{"movie.genre": "Action"}
* goodbye
    - utter_goodbye

## story 4.1
* country{"movie.name": "spider-man"}
    - slot{"movie.name": "spider-man"}
    - action_search_country
    - slot{"movie.location":"USA"}
* director_name
    - action_search_director
    - slot{"director.name": "Sam Raimi"}
* language
    - action_search_language
    - slot{"movie.language": "English"}

## story 4.2
* greet
    - utter_greet
    - utter_ask_howcanhelp
    - action_listen
* gross{"movie.name": "spider-man"}
    - slot{"movie.name": "spider-man"}
    - action_search_gross
    - slot{"movie.gross": 42424242}
* star_rating
    - action_search_rating
    - slot{"movie.star_rating": 7.0}

# story 4.3
* greet
    - utter_greet
    - utter_ask_howcanhelp
    - action_listen
* runtime{"movie.name": "spider-man"}
    - slot{"movie.name": "spider-man"}
    - action_search_duration
    - slot{"movie.runtime": 121}
* release_date
    - action_search_year
    - slot{"movie.release_date": "2005"}
* goodbye
    - utter_goodbye

# story 5
* greet
    - utter_greet
    - utter_ask_howcanhelp
    - action_listen
* other
    - utter_cant_do_this
    - action_show_actions_list

########################################################
########################################################
########################################################
########################################################
########################################################


## Generated Story 1296530003059149405
* greet
    - utter_greet
    - utter_ask_howcanhelp
* director_name{"movie.language": "black", "movie.name": "man"}
    - slot{"movie.name": "man"}
    - slot{"movie.language": "black"}
    - action_search_director
* director_name{"movie.name": "hunger games"}
    - slot{"movie.name": "hunger games"}
    - action_search_director
    - slot{"director.name": "Gary Ross"}
    - export

## Generated Story 1570103838777864257
* greet
    - utter_greet
    - utter_ask_howcanhelp
* director_name{"movie.name": "spider-man"}
    - slot{"movie.name": "spider-man"}
    - action_search_director
    - slot{"director.name": "Sam Raimi"}
* release_date
    - action_search_year
    - slot{"movie.release_date": "2002"}
* runtime
    - action_search_duration
    - slot{"movie.runtime": 121}
* actor_name{"movie.name": "avatar"}
    - slot{"movie.name": "avatar"}
    - action_search_actor
    - slot{"actor.name": "CCH Pounder"}
* goodbye
    - export
## Generated Story -6649703117503380606
* greet
    - utter_greet
    - utter_ask_howcanhelp
* director_name{"movie.name": "star wars?"}
    - slot{"movie.name": "star wars?"}
    - action_search_director
* director_name{"movie.name": "star wars iv?"}
    - slot{"movie.name": "star wars iv?"}
    - action_search_director
* director_name{"movie.name": "black?"}
    - slot{"movie.name": "men"}
    - slot{"movie.name": "black?"}
    - action_search_director
* director_name{"movie.name": "lord of the rings"}
    - slot{"movie.name": "lord of the rings"}
    - action_search_director
* release_date
    - action_search_year
* director_name{"movie.name": "hunger games"}
    - slot{"movie.name": "hunger games"}
    - action_search_director
    - slot{"director.name": "Gary Ross"}
* release_date
    - action_search_year
    - slot{"movie.release_date": "2012"}
* actor_name
    - action_search_actor
    - slot{"actor.name": "Jennifer Lawrence"}
* country
    - action_search_country
    - slot{"movie.location": "USA"}
* language
    - action_search_language
    - export



