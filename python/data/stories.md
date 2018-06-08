## greetings
* greet
    - utter_greet
    - utter_ask_howcanhelp
> check_asked_howcanhelp

# serach director's movies
>check_asked_howcanhelp
* movie {"director": "Spielberg"}
    - utter_ack_dosearch
    - action_search_movie

> check_showed_result

# search year of production
> check_asked_howcanhelp
* year {"movie": "The Matrix"}
    - utter_ack_dosearch
    - action_search_year
> check_showed_result

# search director
> check_asked_howcanhelp
* director {"movie":"Spider-Man 3"}
    - utter_ack_dosearch
    - action_search_director
> check_showed_result



# end
> check_showed_result
* thankyou
    - utter_welcome


* nothing
    - action_listen