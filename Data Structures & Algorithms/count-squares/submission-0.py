class CountSquares:

    def __init__(self):
        self.points = {}
        
        

    def add(self, point: List[int]) -> None:
        x,y = point
        self.points[(x,y)] = self.points.get((x,y),0) + 1
        

    def count(self, point: List[int]) -> int:
        x,y = point
        res = 0
        for (nx,ny) in self.points:
            if nx == x and ny !=y:
                d = abs(ny-y)
                if (x+d, y) in self.points and  (x+d,ny) in self.points:
                    
                    res += (self.points[(nx,ny)]
                    *self.points[(x+d, y)]
                    *self.points[(x+d, ny)])
                
                if (x-d, y) in self.points and (x-d , ny) in self.points:
                    res += (self.points[(nx,ny)]
                    *self.points[(x-d, y)]
                    *self.points[(x-d, ny)])
        return res
        
