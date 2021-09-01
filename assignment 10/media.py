import pytube
from actor import Actor


class Media():
    def __init__(self,id,Name,Director,Casts,Score,URL,Duration,Episodes):
        self.id=id
        self.name=Name
        self.director=Director
        self.casts=Casts
        self.score=Score
        self.url=URL
        self.duration=Duration
        self.episodes=Episodes
def showInfo(self):
        if self.type=='Film':
            print('id:', self.id, 'name:', self.name, 'director:', self.director, 'casts:', self.casts,'score:', self.score, 'url:', self.url, 'duration:', self.duration)
        elif self.type == 'Series':
            print('id:', self.id, 'name:', self.name, 'director:', self.director, 'casts:', self.casts,'score:', self.score, 'url:', self.url, 'duration:', self.duration,'year:', self.year, 'episodes:', self.episodes)

        elif self.type == 'Documentary':
            print('id:', self.id,'name:', self.name, 'director:', self.director, 'casts:', self.casts,'score:', self.score, 'url:', self.url, 'duration:', self.duration)

        elif self.type == 'Clip':
            print('id:', self.id,'name:', self.name, 'director:', self.director, 'casts:', self.casts,'score:', self.score, 'url:', self.url, 'duration:', self.duration)
def download(self):
        pytube.YouTube(self.url).streams.first().download()
        print('download success')

    def show_casts(self):
        print(self.casts)
