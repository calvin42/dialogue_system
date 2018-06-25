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

# story 5
* greet
    - utter_greet
    - utter_ask_howcanhelp
    - action_listen
* director_and_movie_name
    - action_search_director_and_movie
    - action_listen

# story 6
* greet
    - utter_greet
    - utter_ask_howcanhelp
    - action_listen
* movie_and_revenue
    - action_search_movie_and_revenue
* thankyou
    - utter_welcome
    
# story 7
* greet
    - utter_greet
    - utter_ask_howcanhelp
    - action_listen
* info
    - action_show_actions_list

## story 8
* greet
    - utter_greet
    - utter_ask_howcanhelp
    - action_listen
* runtime{"movie.name": "spider-man"}
    - slot{"movie.name": "spider-man"}
    - action_search_duration
    - slot{"movie.runtime": 121}
* thankyou
    - utter_welcome
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



## Generated Story 683486225072283268
* greet
    - utter_greet
    - utter_ask_howcanhelp
* director_name{"movie.name": "hunger games"}
    - slot{"movie.name": "hunger games"}
    - action_search_director
    - slot{"director.name": "Gary Ross"}
* director_name
    - action_search_director
    - slot{"director.name": "Gary Ross"}
* director_name
    - action_search_actor
    - slot{"actor.name": "Jennifer Lawrence"}
* other{"actor.name": "jennifer lawrence"}
    - slot{"actor.name": "jennifer lawrence"}
    - utter_cant_do_this
* nothing
    - export
## Generated Story 7352693122555740752
* greet
    - utter_greet
    - utter_ask_howcanhelp
* director_name{"movie.name": "spider-man"}
    - slot{"movie.name": "spider-man"}
    - action_search_director
    - slot{"director.name": "Sam Raimi"}
* other
    - utter_cant_do_this
* info
    - action_show_actions_list
    - export
## Generated Story -5914550205216335249
* nothing
* greet
    - utter_greet
    - utter_ask_howcanhelp
* info
    - action_show_actions_list
* release_date{"movie.name": "la dolce vita"}
    - slot{"movie.name": "la dolce vita"}
    - action_search_year
* movie
    - action_search_movies_list
* movie_and_revenue{"actor.name": "sam raimi"}
    - slot{"actor.name": "sam raimi"}
    - action_search_movie_and_revenue
    - export
## Generated Story -7820743457175455027
* greet
    - utter_greet
    - utter_ask_howcanhelp
* info
    - action_show_actions_list
* movie_and_revenue{"actor.name": "sam raimi"}
    - slot{"actor.name": "sam raimi"}
    - action_search_movie_and_revenue
    - export
## Generated Story 2598663290258141021
* revenue{"actor.name": "sam raimi"}
    - slot{"actor.name": "sam raimi"}
    - action_search_movie_and_revenue
* movie_and_revenue
    - action_search_movie_and_revenue
* goodbye
    - utter_goodbye
    - export
## Generated Story -1898655558839599541
* greet
    - utter_greet
    - utter_ask_howcanhelp
* movie{"actor.name": "sam raimi"}
    - slot{"actor.name": "sam raimi"}
    - action_search_movie_and_revenue
* movie_and_director
    - action_search_director_and_movie
    - export
## Generated Story 5682593394523054112
* greet
    - utter_greet
    - utter_ask_howcanhelp
* director_name{"movie.name": "spider-man"}
    - slot{"movie.name": "spider-man"}
    - action_search_director
    - slot{"director.name": "Sam Raimi"}
* revenue
    - action_search_movie_and_revenue
* movie
    - action_search_movies_list
* movie_and_director
    - action_search_director_and_movie
* goodbye
    - utter_goodbye
    - export
## Generated Story -1879576400447415797
* greet
    - utter_greet
    - utter_ask_howcanhelp
* movie
    - action_search_director_and_movie
    - export
## Generated Story 4324119877895871810
* greet
    - utter_greet
    - utter_ask_howcanhelp
* language{"movie.name": "moulin rouge"}
    - slot{"movie.name": "moulin rouge"}
    - action_search_language
* budget{"movie.name": "spider-man"}
    - slot{"movie.name": "spider-man"}
    - action_search_budget
    - slot{"movie.budget": 139000000}
* director_name{"movie.name": "it?"}
    - slot{"movie.name": "it?"}
    - action_search_director
* star_rating{"movie.name": "spider-man 3"}
    - slot{"movie.name": "spider-man 3"}
    - action_search_rating
* genre
    - action_search_genre
    - slot{"movie.genre": "Action"}
* movie
    - action_search_movie
* thankyou
    - utter_welcome
* goodbye
    - utter_goodbye
    - export
## Generated Story 6030050495401165095
* greet
    - utter_greet
    - utter_ask_howcanhelp
* goodbye
    - export
## Generated Story -2583380479904270457
* greet
    - utter_greet
    - utter_ask_howcanhelp
* director_name{"movie.name": "spider-man"}
    - slot{"movie.name": "spider-man"}
    - action_search_director
    - slot{"director.name": "Sam Raimi"}
* director_name{"movie.name": "spider-man"}
    - slot{"movie.name": "spider-man"}
    - action_search_director
    - slot{"director.name": "Sam Raimi"}
* goodbye
    - export
