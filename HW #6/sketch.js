let bird;
let pipes = [];
let isGameover;

function setup() {
  createCanvas(windowWidth, windowHeight);
  bird = new Bird();
  pipes.push(new Pipe());
  isGameover = false;
}

function draw() {
  background(0);

  //for (i = 0; i < pipes.length; i ++){  // * What is the difference between the two lines?
  for (i = pipes.length-1; i >= 0; i--){
    if (pipes[i].hits(bird) && !isGameover){
      isGameover = true;
      //pipes.over();
    } else {
      pipes[i].show();
      pipes[i].update();
      isGameover = false;
      if (pipes[i].offscreen()){
        pipes.splice(i, 1); // to delete the pipes that are out of screen
      }
    }
  } 

  bird.show();
  bird.update();

  //console.log(pipes);
  if (!isGameover){
    if (frameCount % 100 == 0){
      pipes.push(new Pipe()); //add a new pipe every 100 frame
    }
  } else {
    gameOver();
  }
}

function keyPressed(){
  if (key == ' '){
    bird.up();
  }
}

function gameOver(){
  bird.vel = 0;
  //pipes.speed = 0;
}
