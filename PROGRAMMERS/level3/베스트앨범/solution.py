from queue import PriorityQueue

def solution(genres, plays):
    answer = []
    music={}
    genres_plays={}
    order=[]
    n=len(genres)
    for i in range(n):
        genre,play=genres[i],plays[i]
        if genre not in music:
            order+=[genre]
            que=PriorityQueue()
            que.put((-play,i))
            music[genre]=que
        else:
            music[genre].put((-play,i))
        if genre not in genres_plays:
            genres_plays[genre]=play
        else:
            genres_plays[genre]+=play
    order.sort(key=lambda x:genres_plays[x],reverse=True)
    for genre in order:
        for _ in range(2):
            if music[genre].empty():
                break
            answer+=[music[genre].get()[-1]]
    return answer