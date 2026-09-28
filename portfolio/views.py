from django.shortcuts import render
def home(request):
    skills = ['Python', 'Django', 'MySQL', 'HTML', 'CSS', 'Git & GitHub']
    projects = [
        {
            'title': 'Personal Portfolio Website',
            'description': 'This site. A responsive portfolio built with Django, where projects are added as data instead of hardcoded HTML.',
            'tech': ['Python', 'Django', 'HTML', 'CSS'],
            'github': '',
            'live_demo': '',
        },
        {
            'title': 'Task Manager (placeholder)',
            'description': 'Replace this with a real project once it is built.',
            'tech': ['Python', 'Django', 'MySQL'],
            'github': '',
            'live_demo': '',
        },
    ]

    return render(request, 'index.html', {'skills': skills, 'projects': projects})
