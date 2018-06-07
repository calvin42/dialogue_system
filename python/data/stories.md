## greetings
* greet
    - utter_greet
    - utter_ask_howcanhelp
> check_asked_howcanhelp

# serach director's movies
>check_asked_howcanhelp
* search_movie {"director": "Spielberg"}
    - utter_ack_dosearch
    - action_search_movie

> check_showed_result

# search year of production
> check_asked_howcanhelp
* search_year {"movie": "The Matrix"}
    - utter_ack_dosearch
    - action_search_year
> check_showed_result

> check_showed_result
* thankyou
    - utter_welcome