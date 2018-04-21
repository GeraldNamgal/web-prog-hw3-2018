# Project 3

Web Programming with Python and JavaScript

My file and folder hierarchy follows closely with the standard Django project, i.e.,
templates are in the Templates folder, css files are in the static folder, etc. I
made my own classes called Cart and OrderGetter which are located in cart.py and
orderGetter.py respectively. I didn't create any additional apps besides "orders".

To run my program, navigate to the "project3" folder of my files. Then run
"winpty python manage.py runserver" in the command line if you have Windows. Run
just "python manage.py runserver" if that doesn't work or if you have another
operating system. Copy and paste the url that gets displayed, to your browser.

The superuser name I created for the database is "gerald" and the password is
"pizza33a".

I put the menu on my "index.html" page (i.e., the main page) because there is no
other relevant information to display (at least for purposes of the project) that's
more important. If I were actually an owner of Pinnochio's, my main page might
be something else, like specials of the day for example. Thus, "index.html" is
both the menu and the main page. You can only access the restaurant's orders and
your own orders (part of my personal touch) on the main page. To check out, users
need to be on the Cart page. There's a Check Out button there they can press.

For my personal touch. I allowed the restaurant owners to mark orders as pending
and complete. On the Restaurant Orders link on the main page, restaurant owners
can see all the orders made and also click a button to mark orders as complete.
For non-owners, they can see the status of their order by going to the main page
and clicking the My Orders link.

For items that only have one price (i.e. only have one size), I use the "priceLarge"
field for the price, which is why I made the "priceSmall" field in the Item model
optional since a few items only have one price. I would explain to administrators
that when adding items to the menu for items with one price, leave the "priceSmall"
field blank and put the price for such items in the "priceLarge" field. I would also
tell them that the way the database is set up doesn't necessarily reflect the logic
of how it's displayed on the website. For example, each row in the Order table in
the database represents a selection the user made, not an order (an order can have
multiple selections). I realized late in the development process that Selection,
Suborder, or some similar name might have been a better name than Order for the Order
model; likewise for the PizzaOrder and SubOrder models. Nonetheless, I grouped
rows in the database with the same 'orderNumber', a field I created, in order to get
at an actual order in the real-world sense of the word. Also, I defaulted order number
counts in the database to 1 when a new customer or restaurant is created. So if a
restaurant and customer's order number is 1 and 2 respectively, then they made 0 and
1 order respectively (I made a str function for these models that should clarify what
the order number represents and how it makes sense).

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

There shouldn't be much data in the database when you begin. I don't know how you
plan to grade it so to err on the side of caution, I left it up to you to add users
(besides the superuser) and orders to your preference. Hopefully this makes grading
easier.

I used Google Chrome mostly for testing and debugging.
