README.md

프로젝트파일에서 필요한 부분만 떼와서 시험작동해보고 있는 파일입니다





## url : path('', views.home)

홈페이지 입니다



## 검색나라선택 : Brazil

여기서는 nation2 라는 sqlite에 brazil에 대한 내용만 저장했습니다

- 저장하는 방법은 home  - sqlite_save.py 입니다



## search

검색을 하시게 되면 home.html 에서 

```
<form name="search" action="/analysis" method="GET">
```

/analysis로 가게 했습니다

- url

```
path('analysis', views.analysis)
```

* views에 그래프 생성내용은  

```
def graph(nation)
```

로 만들었고  두개를 띄우면 어떻게 되는지 궁금해서 같은내용으로 이름만 바꿔서 def 를 넣었습니다

## 분석화면

분석화면의 정의는

```
def analysis(request):
    nation = request.GET.get('nation')

    fig = graph(nation)
    html_graph = mpld3.fig_to_html(fig)
    fig1 = graph1(nation)
    html_graph1 = mpld3.fig_to_html(fig1)

    context = {
        'nation': nation,
        'graph':[html_graph],
        'graph1':[html_graph1]
    }
    return render(request, 'analysis.html', context)
```

했습니다

## analysis.html 에서 입력방식

그래프는 

```
% for elem in graph %}
  {{elem|safe}}
{% endfor %}
```

라고 써서 나오도록 했습니다





# Q. 문제

1. 검색 눌렀을 때, 팝업안뜨기
2. 표시되는 그래프 크기 조절하기?
