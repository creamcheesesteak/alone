from django.shortcuts import render
from django.http import HttpResponse
import sqlite3
import pandas as pd
import collections
import json
import mpld3
import matplotlib.pyplot as plt
import numpy as np


# Create your views here.

def home(request):
    result = {'first':'Multi_A3', 'second':'TEAM EasterEgg'}
    return render(request, 'home.html', context=result)


def graph(nation):
    db_nation = sqlite3.connect('./nation2.db')
    c = db_nation.cursor()
    df = pd.read_sql("SELECT * FROM i_f_" + nation + "", db_nation, index_col=None)
    counts = collections.Counter(df['App_cat'])
    dict = {'Life': ['Food and Drink (Applications)', 'Health and Fitness (Applications)', 'Lifestyle (Applications)',
                     'Weather (Applications)', 'Medical (Applications)', 'Navigation (Applications)',
                     'Finance (Applications)'],
            'Leisure': ['Entertainment (Applications)', 'Shopping (Applications)', 'Social Networking (Applications)',
                        'Sports (Applications)', 'Travel (Applications)', 'Music (Applications)',
                        'Photo and Video (Applications)'],
            'Work': ['Business (Applications)', 'Developer Tools (Applications)', 'Graphics & Design (Applications)',
                     'Productivity (Applications)'],
            'Edu': ['Books (Applications)', 'Catalogs (Applications)', 'Education (Applications)',
                    'Reference (Applications)', ' Magazines and Newspapers (Applications)', 'News (Applications)',
                    'Utilities (Applications)']}
    set_group = ['Life', 'Leisure', 'Work', 'Edu']
    count_group = []
    group = []
    sum = 0
    for group in set_group:  # group : key = Life
        name = dict[group]
        group = dict[group]  # dict['Life']
        for category in group:  # Food and Drink (Applications)
            for key, value in counts.items():
                if key == category:
                    sum = value + sum
        count_group.append(sum)
        print(sum)
        sum = 0
    set_group = {x: y for x, y in zip(set_group, count_group)}

    plt.rcParams['figure.figsize'] = [12, 8]
    Application = set_group.get('Life') + set_group.get('Leisure') + set_group.get('Work') + set_group.get('Edu')
    Life = set_group.get('Life')
    Leisure = set_group.get('Leisure')
    Work = set_group.get('Work')
    Edu = set_group.get('Edu')
    Games = counts.get('Games')
    Kids = counts.get('Kids')
    if Kids is None:
        Kids = 0
    # info. of groups

    group_names = ['Application', 'Games', 'Kids']
    group_sizes = [Application, Games, Kids]

    # info. of subgroups
    subgroup_names = ['Life', 'Leisure', 'Work', 'Edu', 'Games', 'Kids']
    subgroup_sizes = [Life, Leisure, Work, Edu, Games, Kids]

    # colors
    a, b, c = [plt.cm.Reds, plt.cm.Greens, plt.cm.Blues]

    # width
    width_num = 0.4
    # Outside Ring

    fig, ax = plt.subplots()
    # ax.scatter([1, 10], [5, 9])
    ax.axis('equal')
    pie_outside, _ = ax.pie(group_sizes,
                            radius=1.3,
                            labels=group_names,
                            labeldistance=0.8,
                            colors=[a(0.6), b(0.6), c(0.6)])

    plt.setp(pie_outside,
             width=width_num,
             edgecolor='white')

    # Inside Ring

    pie_inside, plt_labels, junk = \
        ax.pie(subgroup_sizes,
               radius=(1.3 - width_num),
               labels=subgroup_names,
               labeldistance=0.75,
               autopct='%1.1f%%',
               colors=[a(0.5), a(0.4), a(0.3), a(0.2),
                       b(0.5),
                       c(0.5)])

    plt.setp(pie_inside,
             width=width_num,
             edgecolor='white')

    plt.title('Donut Plot with Subgroups', fontsize=20)

    plt.show()
    fig.savefig('./1.png')
    return fig

def graph1(nation):
    db_nation = sqlite3.connect('./nation2.db')
    c = db_nation.cursor()
    df = pd.read_sql("SELECT * FROM i_f_" + nation + "", db_nation, index_col=None)
    counts = collections.Counter(df['App_cat'])
    dict = {'Life': ['Food and Drink (Applications)', 'Health and Fitness (Applications)', 'Lifestyle (Applications)',
                     'Weather (Applications)', 'Medical (Applications)', 'Navigation (Applications)',
                     'Finance (Applications)'],
            'Leisure': ['Entertainment (Applications)', 'Shopping (Applications)', 'Social Networking (Applications)',
                        'Sports (Applications)', 'Travel (Applications)', 'Music (Applications)',
                        'Photo and Video (Applications)'],
            'Work': ['Business (Applications)', 'Developer Tools (Applications)', 'Graphics & Design (Applications)',
                     'Productivity (Applications)'],
            'Edu': ['Books (Applications)', 'Catalogs (Applications)', 'Education (Applications)',
                    'Reference (Applications)', ' Magazines and Newspapers (Applications)', 'News (Applications)',
                    'Utilities (Applications)']}
    set_group = ['Life', 'Leisure', 'Work', 'Edu']
    count_group = []
    group = []
    sum = 0
    for group in set_group:  # group : key = Life
        name = dict[group]
        group = dict[group]  # dict['Life']
        for category in group:  # Food and Drink (Applications)
            for key, value in counts.items():
                if key == category:
                    sum = value + sum
        count_group.append(sum)
        print(sum)
        sum = 0
    set_group = {x: y for x, y in zip(set_group, count_group)}

    plt.rcParams['figure.figsize'] = [12, 8]
    Application = set_group.get('Life') + set_group.get('Leisure') + set_group.get('Work') + set_group.get('Edu')
    Life = set_group.get('Life')
    Leisure = set_group.get('Leisure')
    Work = set_group.get('Work')
    Edu = set_group.get('Edu')
    Games = counts.get('Games')
    Kids = counts.get('Kids')
    if Kids is None:
        Kids = 0
    # info. of groups

    group_names = ['Application', 'Games', 'Kids']
    group_sizes = [Application, Games, Kids]

    # info. of subgroups
    subgroup_names = ['Life', 'Leisure', 'Work', 'Edu', 'Games', 'Kids']
    subgroup_sizes = [Life, Leisure, Work, Edu, Games, Kids]

    # colors
    a, b, c = [plt.cm.Reds, plt.cm.Greens, plt.cm.Blues]

    # width
    width_num = 0.4
    # Outside Ring

    fig, ax = plt.subplots()
    # ax.scatter([1, 10], [5, 9])
    ax.axis('equal')
    pie_outside, _ = ax.pie(group_sizes,
                            radius=1.3,
                            labels=group_names,
                            labeldistance=0.8,
                            colors=[a(0.6), b(0.6), c(0.6)])

    plt.setp(pie_outside,
             width=width_num,
             edgecolor='white')

    # Inside Ring

    pie_inside, plt_labels, junk = \
        ax.pie(subgroup_sizes,
               radius=(1.3 - width_num),
               labels=subgroup_names,
               labeldistance=0.75,
               autopct='%1.1f%%',
               colors=[a(0.5), a(0.4), a(0.3), a(0.2),
                       b(0.5),
                       c(0.5)])

    plt.setp(pie_inside,
             width=width_num,
             edgecolor='white')

    plt.title('Donut Plot with Subgroups', fontsize=20)

    plt.show()
    fig.savefig('./2.png')
    return fig

def analysis(request):
    nation = request.GET.get('nation')

    fig = graph(nation)
    html_graph = mpld3.fig_to_html(fig)
    fig1 = graph1(nation)
    html_graph1 = mpld3.fig_to_html(fig1)
    # f = plt.figure()
    # plt.plot([1, 2, 3], [4, 5, 6])
    #
    # print(mpld3.fig_to_html(f, figid='THIS_IS_FIGID'))

    # graph(nation)
    # fig = graph(nation)
    # html_graph = mpld3.fig_to_html(fig)
    context = {
        'nation': nation,
        'graph':[html_graph],
        'graph1':[html_graph1]
    }
    return render(request, 'analysis.html', context)