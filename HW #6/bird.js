class Bird {
    constructor(){
        this.y = height/2;
        this.x = 25;
        this.gravity = 0.5; 
        this.vel = 0;
        this.acc = -20;
        this.w = 20;
        this.h = 20;
    }

    show(){
        fill(255);
        ellipse(this.x, this.y, this.w, this.h);
    }

    update(){
        this.vel += this.gravity;
        this.vel *= 0.9;  //add air resistance to limit lift speed
        this.y += this.vel;

        if (this.y > height){
            this.y = height;
            this.vel = 0;
        }
        if (this.y < 0){
            this.y = 0;
            this.vel = 0;
        }
    }

    up(){
        this.vel += this.acc;
    }
}