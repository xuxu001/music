from django.shortcuts import render
from .models import *
# Create your views here.
def indexView(request):
    #热搜歌曲  通过dynamic 查询dynamic_search 排序查找song表中的内容并取前8
    search_song = Dynamic.objects.select_related('song').order_by('-dynamic_search').all()[:8]

    #音乐分类  取出label全部数据
    label_list = Label.objects.all()
    #热门歌曲  同热搜歌曲取前10
    play_hot_song = Dynamic.objects.select_related('song').order_by('-dynamic_search').all()[:10]
    #新歌推荐  通过搜索时间排序
    daily_recommendation = Song.objects.order_by('-song_release').all()[:3]
    #热门搜索
    search_ranking = search_song[:6]
    #热门下载
    down_ranking = Dynamic.objects.select_related('song').order_by('-dynamic_down').all()[:6]

    all_ranking = [search_ranking,down_ranking]
    return render(request,'index.html',locals())
    # return render(request, 'index.html')

