class Point{
  int x, y;
  String function;
  
  
  Point(int x_, int y_, String function_ ){
    x = x_;
    y = y_;
    function = function_;
  }
  
  Boolean equals(Point p){
    if (p.x == x && p.y == y){
      return true;
    }
    else{
      return false;
    }
  }
  
  Point add(char direction){
    if (direction == 'w' || direction == 'W') return new Point(x, y-swidth, "Snake");
    
    if (direction == 's' || direction == 'S') return new Point(x, y+swidth, "Snake");
    
    if (direction == 'a' || direction == 'A') return new Point(x-swidth, y, "Snake");
    
    if (direction == 'd' || direction == 'D') return new Point(x+swidth, y, "Snake");
    
    else return new Point(0, 0, "Item");
    
  }
  
  void show(){
    noStroke();
    if (function.equals("Snake")){
      fill(0, 189, 121);
      rect(x, y, swidth, swidth);
    }
    else{
      fill(232, 0, 0);
      rect(x ,  y, swidth, swidth);
    }
  }
}
