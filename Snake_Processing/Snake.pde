class Snake{
  ArrayList<Point> body;
  Point head;
  int counter, bodylength;
  Boolean grow;
  
  Snake(){
    grow = false;
    body = new ArrayList<Point>();
    body.add(new Point(0, 0, "Snake"));
    body.add(new Point(swidth, 0, "Snake"));
    head = body.get(0);
    counter = 1;
    bodylength = 2;
    
  }
  
  void show(){
    
    //move last bodypart to the front of snake
    if (game){
      int change = int(counter % bodylength);
      body.set(change, head.add(current_key));
      head = body.get(change);
      
      //update counter
      counter++;
      
      //check if snake collided with wall
      
      if (head.x < 0 || head.y < 0 || head.x > width || head.y > width) game = false;
    }
    
    //check if snake collided with other part of body
    //draw snake
    //check if snake has eaten item
    for (Point p : body){
        p.show();
        if (p != head){
          if (p.equals(head)){
            game = false;
          }
        }
        if (head.equals(item.location)) grow = true;
  }
  if (grow){
    grow();
    grow();
    item = new Item();
    grow = false;
  }
  }
  
  void grow(){
    body.add(new Point(head.x, head.y, "Snake"));
    int prev = int(counter % bodylength);
    bodylength++;
    counter = 1;
    while (int(counter % bodylength) != prev) counter++;
  }
}
    
