let video;
let poseNet;
let noseX, noseY;
let lefteyeX, lefteyeY, righteyeX, righteyeY;
let hairX, hairY;
let hairImg = [];
let hairShown;
let eyeShown;

function preload(){
  hairImg[0] = loadImage('hair1.jpg');
  hairImg[1] = loadImage('hair2.jpg');
  hairImg[2] = loadImage('hair3.jpg');
  hairImg[3] = loadImage('hair5.png');
  hairImg[4] = loadImage('hair6.jpg');
  hairImg[5] = loadImage('hair7.jpg');
  eyeShown = loadImage('eye1.png');
  //hairShown = loadImage('hair1.jpg');
  hairShown = random(hairImg);
}

function setup() {
  createCanvas(windowWidth, windowHeight);
  video = createCapture(VIDEO);
  video.hide();
  poseNet = ml5.poseNet(video, modelReady);
  poseNet.on('pose', gotPoses); //?
  //imageMode(CENTER);
}

function keyPressed(){
  if (key === ' '){
    hairShown = random(hairImg);
  }
}

function gotPoses(poses){
  if (poses.length > 0){
    lefteyeX = poses[0].pose.keypoints[1].position.x;
    lefteyeY = poses[0].pose.keypoints[1].position.y;
    
    righteyeX = poses[0].pose.keypoints[2].position.x;
    righteyeY = poses[0].pose.keypoints[2].position.y;

    noseX = poses[0].pose.keypoints[0].position.x;
    noseY = poses[0].pose.keypoints[0].position.y;
  }
}

function modelReady(){
  console.log('model ready');
}

function draw() {
  background(255);
  image(video, 0, 0);

  let d = dist(lefteyeX, lefteyeY, righteyeX, righteyeY);

  // fill(255, 0, 0);
  // ellipse(lefteyeX, lefteyeY, d/2);
  // ellipse(righteyeX, righteyeY, d/2);

  hairX = lefteyeX - d*2.8;
  hairY = lefteyeY - d*3.4;

  image(hairShown, hairX, hairY, d*4.5, d*4.5);
  //image(eyeShown, righteyeX - d/2, righteyeY - d/4, d, d/2);
}
