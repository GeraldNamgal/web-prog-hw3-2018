# Project 3

Web Programming with Python and JavaScript

The superuser name I created was "gerald" and the password is "pizza33a".

I put the menu on my "index.html" page (i.e., the main page) because there is no
other relevant information to display (at least for purposes of the project) that's
more important. If I were actually an owner of Pinnochio's, my main page might
be something else, like specials of the day for example.

For items that only have one price (e.g. only have one size), I use the "priceLarge"
field for the price, which is why I made the "priceSmall" field in the Item model
optional since a few items only have one price. I would explain to administrators
that when adding items to the menu for items with one price, leave the "priceSmall"
field blank and put the price for such items in the "priceLarge" field.

I defined my Special Pizza to be one with 4 or 5 toppings.

I chose to have a "ManyToManyField" between a Pizza Order model and a Topping
model. One of the reasons I chose to do this is because Django implements
many-to-many as a set relation so I don't have to worry about users adding the
same topping to the pizza over and over again. It also enforces the relationship
between a set of toppings and pizzas that administrators created; I don't have to
worry about anything being unaccounted for. It also automates the process of
checking whether a deletion or addition in one happened in one and/or the other
and handles the table consequences and such of situations like these for me. That
is, the "ManyToManyField" will allow me to associate a topping with multiple
pizzas and each pizza with multiple toppings.
