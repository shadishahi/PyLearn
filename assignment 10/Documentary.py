from Media import Media

class Documentary(Media):
    def __init__(self,id,Name,Director,Casts,Score,URL,Duration):
        Media.__init__(self,id,Name,Director,Casts,Score,URL,Duration)
    

    def editdocumentary(self):
        self.id = input('enter id: ')
        self.name = input('enter name:')
        self.director = input('enter director:')
        self.score = input('enter score: ')
        self.url = input('enter url: ')
        self.duration = input('enter duration:')
        number = int(input('enter the number of actors:'))
        print('Please show after each actor')
        self.casts = []
        for cast in range(number):
            person = input('cast' + str(cast))
            self.casts.append(person)


        print('information editing done')
