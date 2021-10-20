class Pipe{
    constructor(){
        this.top = random(height/2);
        this.bottom = random(height/2);
        this.x = width;
        this.w = 20;
        this.speed = 5; //how fast the pipes move
    }

    show(){
        fill(225);
        rect(this.x, 0, this.w, this.top); //create the top pipe
        rect(this.x, height - this.bottom, this.w, this.bottom); //create the bottom pipe
    }

    update(){
        this.x -= this.speed; //make the pipe move
    }

    hits(bird){
        if (bird.y < this.top + (bird.h / 2) || bird.y > height - this.bottom - (bird.h / 2)){
            if (bird.x + (bird.w / 2) > this.x && bird.x -(bird.w / 2) < this.x + this.w){
                return true;
            }
        } else {
            return false;
        }
    }

    over(){
        this.speed = 0
    }

    offscreen(){
        if (this.x < - this.w){
            return true;
        } else {
            return false;
        }
    }
}