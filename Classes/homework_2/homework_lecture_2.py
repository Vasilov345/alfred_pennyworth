class Maths:
    """
    Make class with one method "add_num" with 2 parameters, which returns sum of these parameters.
    Note: this method should not take instance as first parameter.
    """


class Pizza:
    """
    Make class which takes 1 parameter on init - list of ingredients and defines instance attribute ingredients.
    It should have 2 methods:
    margherita (['mozzarella', 'tomatoes']) and prosciutto (['mozzarella', 'tomatoes', 'ham'])
    which should create Pizza instances with predefined list of ingredients.
    Example:
        pizza1 = Pizza(["tomato", "cucumber"])
        pizza1.ingredients will equal to ["tomato", "cucumber"]
        pizza2 = Pizza.prosciutto()
        pizza2.ingredients will equal to ['mozzarella', 'tomatoes', 'ham']
    """


class Concert:
    """
    Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
    In case of setting visitors_count - max_visitors_num should be checked,
    if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
    Example:
        Concert.max_visitor_num = 50
        concert = Concert()
        concert.visitors_count = 1000
        print(concert.visitors_count)  # 50
    """


class BookDataclass:
    """
    Create dataclass with 3 fields - title (str), author (str), pages_num (int)
    """


class Book:
    """
    Create regular class taking 3 params on init - title, author, pages_num
    Make its str() representation the same as for BookDataclass defined above.
    """
