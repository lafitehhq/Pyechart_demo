from django.shortcuts import render

from django.db import connection
from django.http import HttpResponse
from django.template import loader
from pyecharts import Bar
REMOTE_HOST = "https://pyecharts.github.io/assets/js"
def exc_sql(sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def index(request):
    template = loader.get_template('mycharts/pyecharts.html')
    b=bar()
    context = dict(
        myechart=b.render_embed(),
        host=REMOTE_HOST,
        script_list=b.get_js_dependencies()
    )
    return HttpResponse(template.render(context, request))


# from pyecharts import Bar
#
# attr = ["{}月".format(i) for i in range(1, 13)]
# v1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
# v2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
# bar = Bar("柱状图示例")
# bar.add("蒸发量", attr, v1, mark_line=["average"], mark_point=["max", "min"])
# bar.add("降水量", attr, v2, mark_line=["average"], mark_point=["max", "min"])
# bar.render()

def bar():
    #_data = []
    query_sql = "select  nation_name,nation_quant from Nation_Demo"
    data_list = exc_sql(query_sql)
    x=[i[0] for i in data_list]
    y=[i[1] for i in data_list]
    #_data.append()
    bar=Bar("各国GDP柱状图",width=1000,height=700)
    bar.add("各国GDP量",x, y, type="effectScatter", border_color="#ffffff", symbol_size=2,
            is_label_show=True, label_text_color="#0000FF", label_pos="inside", symbol_color="yellow",
            bar_normal_color="#006edd", bar_emphasis_color="#0000ff")
    return bar



