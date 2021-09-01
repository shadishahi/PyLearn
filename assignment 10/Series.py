from Media import Media

class Series(Media):
    def __init__(self,id,Name,Director,Casts,Score,URL,Duration,Episodes):
        Media.__init__(self, id,Name,Director,Casts,Score,URL,Duration,Episodes)

    
    def editSeries(self):
        print('Do you want to edit?\n 1-name  2-director  3-score  4-url  5-episodes')
        item = input('number of item: ')
        newitem = input('please enter the new item: ')
        if item == '1':
            self.name = newitem
        elif item == '2':
            self.director = newitem
        elif item == '3':
            self.imdb_score = newitem
        elif item == '4':
            self.url = newitem
        elif item == '5':
            self.episodes = newitem
        else:
            print('wrong input')
        return self.media
