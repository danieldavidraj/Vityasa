# Vityasa Internship
## Question 1
POST https://vityasa.herokuapp.com/items

[1, 4, -1, "hello", "world", 0, 10, 7]

{
  "valid_entries": 4,
  "invalid_entries": 4,
  "min": 1,
  "max": 10,
  "average": 5.5
}

<img src="1.png">

## Question 2

POST https://vityasa.herokuapp.com/booking

{
  "slot": 1, "name": "John"
}

{"status":"confirmed booking for John in slot 1"}

<img src="2.png">

GET https://vityasa.herokuapp.com/booking

{'slot': 1, 'name': ['John', 'Diana']}

<img src="3.png">

POST https://vityasa.herokuapp.com/cancel

{
  "slot": 1, "name": "Diana"
}

{ "status":"canceled booking for Diana in slot 1"}

<img src="4.png">

POST https://vityasa.herokuapp.com/cancel

{
  "slot": 2, "name": "Riker"
}

{"status":"slot full, unable to save booking for Riker in slot 2"}

<img src="7.png">

POST https://vityasa.herokuapp.com/cancel

{
  "slot": 2, "name": "Diana"
}

{ "status":"no booking for the name Diana in slot 2"}

<img src="8.png">

## Question 3

POST https://vityasa.herokuapp.com/plot

{
  "x": 1, "y": 1
}

{"status": "accepted"}

<img src="5.png">

POST https://vityasa.herokuapp.com/plot

{
  "x": 5, "y": 5
}

{"status": "Success (1, 1) (1, 5) (5, 1) (5, 5)"}

<img src="6.png">
