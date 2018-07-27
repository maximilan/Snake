class Item{
  Point location;
  Boolean inSnake;
  
  Item(){
    inSnake = true;
    while(inSnake){
      location = new Point(int(random(0, rows)) * swidth, int(random(0, rows)) * swidth, "Item");
      for (Point p : snake.body){
        if (p.equals(location)){
          inSnake = true;
          break;
        }
        inSnake = false;
      }
    }
    
  }
  
  void show(){
    location.show();
  }
}
