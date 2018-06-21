
## Generated Story -1370806963360449556
* hi
    - utter_greet
    - utter_ask_howcanhelp
* I want to know who is the director of Casablanca {"movie.name": "Casablanca"}
    - slot{"movie.name": "Casablanca"}
    <!-- - utter_ack_dosearch -->
    - action_search_director
* director_name
    - action_search_director
    - action_is_title_right
* None
* budget
    - action_search_budget
    - action_is_title_right

* goodbye
    - utter_goodbye
    - export
## Generated Story 9112731220316799627
* actor
    - export
## Generated Story -1351447969531125165
* other
    - utter_greet
    - utter_ask_howcanhelp
* director_name{"movie.name": "thor"}
    <!-- - utter_ack_dosearch -->
    - action_search_director
    - action_is_title_right
* other
    - utter_goodbye
    - export
## Generated Story 1044213880634831777
* other
    - utter_greet
    - utter_ask_howcanhelp
* director_name{"movie.name": "star wars episode iv"}
    <!-- - utter_ack_dosearch -->
    - action_search_director
* media
    - utter_goodbye
    - export

## Generated Story 6169417479844847191
* media
    - utter_greet
    - utter_ask_howcanhelp
* director_name{"movie.name": "spider-man"}
    - action_search_director
    - export
## Generated Story 4544072419200717855
* movie_name
    - utter_greet
    - utter_ask_howcanhelp
* director_name{"movie.name": "spider-man"}
    - action_search_director
    - export
## Generated Story 1361820462911320687
* media
    - utter_greet
    - utter_ask_howcanhelp
* director_name{"movie.name": "spider-man"}
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
* movie_name
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
* director_name{"movie.name": "spider-man"}
    - slot{"movie.name": "spider-man"}
    - action_search_director
    - export
## Generated Story 3392719778749881346
* media
    - utter_greet
    - utter_ask_howcanhelp
* director_name{"movie.name": "spider-man"}
    - slot{"movie.name": "spider-man"}
    - action_search_director
* director_name
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
* director_name{"movie.name": "avatar"}
    - slot{"movie.name": "avatar"}
    - action_search_director
    - slot{"director.name": "James Cameron"}
    - export
## Generated Story 5657499674078307932
* movie_name
    - utter_greet
    - utter_ask_howcanhelp
* director_name{"movie.name": "spider-man"}
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
* language{"movie.name": "la dolce vita"}
    - slot{"movie.name": "la dolce vita"}
    - action_search_language
* runtime{"movie.name": "iron man"}
    - slot{"movie.name": "iron man"}
    - action_search_duration
    - slot{"runtime": 195}
* runtime{"movie.name": "space odissey"}
    - slot{"movie.name": "space odissey"}
    - action_search_duration
* nothing
* goodbye
    - utter_goodbye
    - export
## Generated Story 326004781424288375
* hi
    - utter_greet
    - utter_ask_howcanhelp
* director_name
    - action_search_year
* bye
    - utter_goodbye
    - export
    
## Generated Story -4713355473569836652
* director_name
    - action_search_director
* movie_name
    - action_search_movie
* language
    - action_search_language
    - export

## Generated Story -8051403426547174045
* hello
    - utter_greet
    - utter_ask_howcanhelp
* when back to the future came out?
    - action_search_year
* who is the director of spider-man?
    - export



## Generated Story -6115205396404006567
* hey
    - utter_greet
    - utter_ask_howcanhelp
* director_name {"movie.name": "avatar"}
    - action_search_director
* who is the director of avatar?
    - action_search_director
* rating
    - action_search_rating
* release_date {"movie.name": "star wars"}
    - action_search_year
    - export

