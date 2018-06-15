## greetings
* greet
    - utter_greet
    - utter_ask_howcanhelp
> check_asked_howcanhelp

# serach director's movies
>check_asked_howcanhelp
* show spielberg movies {"director": "Spielberg"}
    <!-- - utter_ack_dosearch -->
    - action_search_movie

> check_showed_result

# search year of production
> check_asked_howcanhelp
* when was the matrix produced {"movie": "The Matrix"}
    <!-- - utter_ack_dosearch -->
    - action_search_year
> check_showed_result

# search director
> check_asked_howcanhelp
* who directed spider-man 3? {"movie":"Spider-Man 3"}
    <!-- - utter_ack_dosearch -->
    - action_search_director
> check_showed_result

# end

> check_showed_result
* thank you, bye
    - utter_welcome
    - utter_goodbye

> check_showed_result
* thank you
    - utter_welcome

> check_showed_result
* bye
    - utter_goodbye

* nothing
    - action_listen


# boh 
* hi
    - utter_greet
    - utter_ask_howcanhelp
* I want to know who is the director of Casablanca {"movie": "Casablanca"}
    <!-- - utter_ack_dosearch -->
    - action_search_director
    - utter_ask_howcanhelp
* nothing, thank you
    - utter_welcome
    - utter_goodbye

# boh 2

* hello
    - utter_greet
    - utter_ask_howcanhelp
* how much did The matrix cost? {"movie": "The matrix"}
    <!-- - utter_ack_dosearch -->
    - action_search_budget
    -utter_ask_howcanhelp
* how much did the matrix gain? {"movie": "The matrix"}
    <!-- - utter_ack_dosearch -->
    - action_search_gross
* thank you bye
    - utter_welcome
    - utter_goodbye
# boh 3
* who is the main character in star wars? {"movie": "star wars"}
    - action_cannot_do_this
* what can you do?
    - action_show_actions_list

## Generated Story -1370806963360449556
* hi
    - utter_greet
    - utter_ask_howcanhelp
* I want to know who is the director of Casablanca
    <!-- - utter_ack_dosearch -->
    - action_search_director
    - utter_ask_howcanhelp
* director
    - action_search_director
    - action_search_director
    - utter_ask_howcanhelp
* None
* budget
    - action_search_budget
    - action_search_director
* goodbye
    - utter_goodbye
    - utter_goodbye
    - export
## Generated Story 9112731220316799627
* actor
    - export
## Generated Story -1351447969531125165
* other
    - utter_greet
    - utter_ask_howcanhelp
* director{"movie.name": "thor"}
    <!-- - utter_ack_dosearch -->
    - action_search_director
* other
    - utter_goodbye
    - export
## Generated Story 1044213880634831777
* other
    - utter_greet
    - utter_ask_howcanhelp
* director{"movie.name": "star wars episode iv"}
    <!-- - utter_ack_dosearch -->
    - action_search_director
* media
    - utter_goodbye
    - export

## Generated Story 6169417479844847191
* media
    - utter_greet
    - utter_ask_howcanhelp
* director{"movie.name": "spider-man"}
    - action_search_director
    - export
## Generated Story 4544072419200717855
* movie
    - utter_greet
    - utter_ask_howcanhelp
* director{"movie.name": "spider-man"}
    - action_search_director
    - export
## Generated Story 1361820462911320687
* media
    - utter_greet
    - utter_ask_howcanhelp
* director{"movie.name": "spider-man"}
    - slot{"movie.name": "spider-man"}
    - action_search_director
* nothing
* goodbye
    - utter_goodbye
    - export
## Generated Story 4536708346992386963
* media
    - utter_greet
    - utter_ask_howcanhelp
* release_date{"movie.name": "spider-man"}
    - slot{"movie.name": "spider-man"}
    - action_search_year
    - export
## Generated Story 5708924795597757795
* media
    - utter_greet
    - utter_ask_howcanhelp
* release_date{"movie.name": "spider-man"}
    - slot{"movie.name": "spider-man"}
    - action_search_year
* release_date
    - action_search_year
    - export
## Generated Story 7356608724397526775
* movie
    - utter_greet
    - utter_ask_howcanhelp
* release_date
    - action_search_year
* release_date{"movie.name": "spider-man"}
    - slot{"movie.name": "spider-man"}
    - action_search_year
    - export
## Generated Story -1686094423650051910
* media
    - utter_greet
    - utter_ask_howcanhelp
* director{"movie.name": "spider-man"}
    - slot{"movie.name": "spider-man"}
    - action_search_director
    - export
## Generated Story 3392719778749881346
* media
    - utter_greet
    - utter_ask_howcanhelp
* director{"movie.name": "spider-man"}
    - slot{"movie.name": "spider-man"}
    - action_search_director
* director
    - action_search_director
    - action_search_director
* media
    - utter_goodbye
* nothing
* 
    - export
## Generated Story -3357543660275193625
* other
    - utter_greet
    - utter_ask_howcanhelp
* budget
    - action_search_gross
* director{"movie.name": "avatar"}
    - slot{"movie.name": "avatar"}
    - action_search_director
    - slot{"director.name": "James Cameron"}
    - export
## Generated Story 5657499674078307932
* movie
    - utter_greet
    - utter_ask_howcanhelp
* director{"movie.name": "spider-man"}
    - slot{"movie.name": "spider-man"}
    - action_search_director
    - slot{"director.name": "Sam Raimi"}
* release_date{"movie.name": "spider-man"}
    - slot{"movie.name": "spider-man"}
    - action_search_year
* release_date{"movie.name": "spider-man"}
    - slot{"movie.name": "spider-man"}
    - action_search_year
    - export
## Generated Story -1951248412566775693
* other
    - utter_greet
    - utter_ask_howcanhelp
* genre{"movie.name": "up?"}
    - slot{"movie.name": "up?"}
    - action_search_genres
* revenue{"movie.name": "the avengers"}
    - slot{"movie.name": "the avengers"}
    - action_search_gross
    - slot{"movie.gross_revenue": 623279547}
* language{"movie.name": "la dolce vita?"}
    - slot{"movie.name": "la dolce vita?"}
    - action_search_language
* runtime{"movie.name": "iron man"}
    - slot{"movie.name": "iron man"}
    - action_search_duration
    - slot{"runtime": 195}
* runtime{"director.name": "space odissey"}
    - slot{"director.name": "space odissey"}
    - action_search_duration
    - slot{"runtime": 195}
* nothing
* goodbye
    - utter_goodbye
    - export
