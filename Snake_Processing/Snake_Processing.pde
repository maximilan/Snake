Item item;
int Width;
int swidth;
int rows;
char current_key;
char[] possible_keys = {'a', 'A', 's', 'S', 'd', 'D', 'w', 'W'};
Boolean game;
Snake snake;


void setup(){
  snake = new Snake();
  game = true;
  current_key = 'd';
  swidth = 8;
  size(400, 400);
  rows = width/swidth;
  item = new Item();
  //possible_keys = {'a', 'A', 's', 'S', 'd', 'D', 'w', 'W'};
}

void keyPressed(){
  Boolean exit = false;
  if ((current_key == 'W' || current_key == 'w') && (key == 'S' || key == 's')) exit = true;
  else if ((current_key == 'S' || current_key == 's') && (key == 'W' || key == 'w')) exit = true;
  else if ((current_key == 'A' || current_key == 'a') && (key == 'D' || key == 'd')) exit = true;
  else if ((current_key == 'D' || current_key == 'd') && (key == 'A' || key == 'a')) exit = true;
  else{
    for (char p : possible_keys){
      if (p == key){
        current_key = key;
      }
    }
  }
}

void draw(){
  frameRate(7);
  background(0);
  item.show();
  snake.show();
  if (!game){
     fill(255);
     textSize(40);
     text("Game over!", 50, width/2 -50);
     textSize(30);
     text("Points: "+str(snake.body.size()), 50, width/2 + 50);
  }
}
