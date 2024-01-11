import datetime


class Course:

    LIST_OF_COURSES = [
        {
            'title': 'Introduction to Python',
            'subtitle': "Discover the World of Python: A Step-by-Step Guide",
            'users_story': '''This course is for beginners and for those 
                        who want to refresh on basic python programming Fundamentals.
                        We adopt a very simple approach to teaching.''',
            'date_created': datetime.date(2023, 10, 10),
            'category': 'Basic', # basic, concepts
            'edition': '1',
            'price': 0.00,
            'is_available': True,
            'url_name': 'basic-python'
        },
        {
            'title': 'Cascading Style Sheet (CSS) Basics',
            'subtitle': 'Learn or Refresh on basic CSS',
            'users_story': '''CSS can be very powerful but also very crowded with syntax. Having a course that
                            simplifies learning for newbies or refreshes for experts.''',
            'date_created': datetime.date(2024, 1, 15),
            'category': 'Basic', # basic, concepts
            'edition': '1',
            'price': 0.00,
            'is_available': True,
            'url_name': 'basic-python'
        },
        {
            'title': 'Instant Bootstrap',
            'subtitle': 'Bootstrap is HTML + CSS + JS at once. A smart frontend to know',
            'users_story': """'Instant Bootstrap' is your essential guide to harnessing HTML, 
                                CSS, and JS in Bootstrap for rapid, powerful frontend development. 
                                Elevate your skills and productivity—let's embark on 
                                this transformative journey together, unlocking your full web development potential!""",
            'date_created': datetime.date(2024, 3, 12),
            'category': 'Concept',
            'edition': '1',
            'price': 10,
            'is_available': True,
            'url_name': 'basic-python'
        },
        {
            'title': "Introduction to Javascript",
            'subtitle': "JavaScript Made Simple: A Step-by-Step Introduction",
            'users_story': """This book is tailored to aspiring web developers like you. 
                                You'll find clear explanations, practical examples, and hands-on exercises 
                                that cover the essentials of JavaScript and its application in web development. 
                                Starting with basics like variables, functions, and DOM manipulation.""",
            'date_created': datetime.date(2024, 3, 12),
            'category': 'Concept',
            'edition': '1',
            'price': 0,
            'is_available': True,
            'url_name': 'basic-python'
        },
        {
            'title': 'Object Oriented Program',
            'subtitle': 'OOP made easy',
            'users_story': """This sections takes OOP head on, I bet you the step by step thorough guide to
            will help you understand this concept that takes ages to learn.""",
            'date_created': datetime.date(2024, 3, 12),
            'category': 'Concept',
            'edition': '1',
            'price': 10.00,
            'is_available': True,
            'url_name': 'oop'
        }
    ]