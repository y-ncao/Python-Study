#####10/2 Second Round Interview with Linkedin

__iter__()

next()


/** A reference to a file. */
public class TextFile implements Iterable<String>
{
  public TextFile(String fileName) { // please implement this
  }
 
  /** Begin reading the file, line by line. The returned Iterator.next() will return a line. */
  @Override
  public Iterator<String> iterator() { // please implement this
  }
}




class TextFile:
  def __init__(self, fileName):         
         f = open(fileName)
         self.file = f

          
  class Iterator():
      def __init__(self, file_inside)
         self.file_inside = file_inside
         self.index = -1
      def next()
          self.index += 1
          line = self.file_inside.get_line_by_index(self.index)
          if self.index == max
                          
          if '\eof' in line:
              f.close()
          return line
          
      
  def __iter__(self):
        return Iterator(self.file)
        
t1 = TextFile()

'\n'

eof

[1,2,3,4,5]

def f1(t):
    i1 = t.__iter__()
    i1.next()
    i1.next()
    i1.next()
    
def f2(t):
    i2 = t.__iter__()
    i2.next()    
    i2.next()    
    i2.next()    

t1.next()  # 1

t1.next()  # 2




public interface PointsOnAPlane {
 
    /**
     * Stores a given point in an internal data structure
     */
    void addPoint(Point point);
 
    /**
     * For given 'center' point returns a subset of 'p' stored points
     * that are closer to the center than others.
     *
     * E.g.
     * Stored:
     * (0, 1)
     * (0, 2)
     * (0, 3)
     * (0, 4)
     * (0, 5)
     *
     * findNearest(new Point(0, 0), 3) -> (0, 1), (0, 2), (0, 3)
     */
    Collection<Point> findNearest(Point center, int p);
 
    class Point {
 
        final int x;
 
        final int y;
 
 
        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}



(key, value)
(distance_to_center, Point)
from heap import heappush, heappop

class Find_Near():
    def __init__(self):
        self.point_list = []
        
    def add_point(self, Point):
        self.point_list.append(Point)
        
    def find_nearest(self, center, p):
        if len(self.point_list) < p:
            raise 'Not enough points stored'
        elif len(self.point_list) == p:
            return self.point_list
            
        heap = []
        for point in self.point_list:
            distance = self.calculate_distance(point, center)
            heappush(heap, (distance, point))
                           distance , point
                           
        nearest = []
        for i in range(p):
            nearest.append(heappop(heap)[1])
            
        return nearrest
        
max_heap
p points into the max_heap



O(n*logn)
+
O(k*logn)