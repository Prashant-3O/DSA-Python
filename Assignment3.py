class MovieNode:
    
    def __init__(self,movieName,relDate):
        self.movieName = movieName
        self.relDate = relDate
        self.next = None
        return
class NetflixMovieList:
    def __init__(self):
        self.head= None
        
    def addMovie(self, movieName, relDate):
        new = MovieNode(movieName, relDate)
        if self.head == None: #if head is null then it add to beginning node
            self.head = new
            return
        new.next = self.head #if head is not null then it add to next node
        self.head = new
        return
    def remMovie(self,key):
        temp = self.head
        if temp!= None:
            if temp.movieName  == key:
                self.head = temp.next
                temp = None
                return
        while (temp != None):
            if temp.movieName == key:
                break
            prev = temp
            temp = temp.next
        if(temp == None):
            return
        
        prev.next = temp.next

        temp = None        
    def displayMovies(self):
        if self.head == None:
            print("No Movies right now to show")
            return
        temp = self.head
        
        while(temp != None):
            print(temp.movieName,temp.relDate)
            temp = temp.next
        return

movie_List = NetflixMovieList()
movie_List.addMovie('IronMan', '2008')
movie_List.addMovie('IronMan 2', '2010')
movie_List.addMovie('IronMan 3', '2012')
movie_List.remMovie('IronMan 2')
movie_List.displayMovies()