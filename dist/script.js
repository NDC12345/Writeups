///
(function() {
  function Circle(config) {
    this.x = config.x || 0;
    this.y = config.y || 0;
    this.radius = config.radius || 40;
    this.numPoints = this.radius * Math.PI/8;
    this.delta = this.radius / 20.5;
    this.points = this.getPoints();
    this.colour = this.getColour();
  }

  Circle.prototype = {
    getPoints: function() {
      var points = [];
      var x, y;
      for (var i=0; i<this.numPoints; i++) {
        x = (Math.random() * this.delta) - (this.delta / 2);
        y = (Math.random() * this.delta) - (this.delta / 2);
        points[i] = {x: x, y: y};
      }
      return points;
    },
    getColour: function() {
      var r = Math.floor(Math.random() * 240);
      var g = Math.floor(Math.random() * 245);
      var b = Math.floor(Math.random() * 225);
      var a = (Math.random() * 0.2) + 0.1;
      return "rgba(" + r + "," + g + "," + b + "," + a + ")";
    },
    draw: function(ctx) {
      ctx.save();
      ctx.lineWidth = Math.round(this.radius / 350);
      ctx.strokeStyle = this.colour;
      ctx.fillStyle = this.colour;
      ctx.beginPath();
      
      var progress, x, y;
      x = this.x + (this.radius + this.points[0].x) * Math.cos(0);
      y = this.y + (this.radius + this.points[0].y) * Math.sin(0);
      ctx.moveTo(x, y);
      for (var i=1; i<this.numPoints; i++) {
        progress = 4 * Math.PI / this.numPoints * i;
        x = this.x + (this.radius + this.points[i].x) * Math.cos(progress);
        y = this.y + (this.radius + this.points[i].y) * Math.sin(progress);
        ctx.lineTo(x, y);
      }
      
      ctx.fill();
      //ctx.stroke();
      ctx.closePath();
      ctx.restore();
    }
  };
  
  window.Circle = Circle;
})();

var can = document.getElementById("canvas");
can.width = window.innerWidth;
can.height = window.innerHeight;
var ctx = can.getContext("2d");

var NUMBER = Math.round(1000);
for (var i=0; i<NUMBER; i++) {
  var circle = new Circle({
    x: Math.random() * can.width,
    y: Math.random() * can.height,
    radius: Math.round(Math.random() * (Math.min(can.width, can.height) / 10))
  });
  circle.draw(ctx);
    ctx.globalCompositeOperation = "overlay";
}

///////////
//////
/* The idea: black and white checkerboard. Black squares grow a white border, white grows a black. When they've changed colors, begin again. */
var board = document.getElementById("d");
var board = new Sketch.create({ interval: 2 }),
    squares = [],
    w = 40,
    h = 40;
var Square = function(x, y, reverse) {
  this.x = x+2;
  this.y = y+2;
  this.color1 = 'hsla(30, 40%, 52%,.8)';
  this.color2 = 'hsla(76,50%,50%,.4)';
  this.reverse = reverse;
  this.line = 1;
  this.update = function() {
    if (++this.line >= w/random(.2,.9)) {
      this.reverse ^= true;
      this.line = random(.1,.9);
      this.globalCompositeOperation = 'xor';
    }
  }
  this.draw = function() {
    board.fillStyle = this.reverse ? this.color1 : this.color2;
    board.strokeStyle = this.reverse ? this.color2 : this.color1;
    board.lineWidth = this.line;
    board.fillRect(this.x, this.y, w, h);
    board.strokeRect(this.x + this.line / Math.abs(random(2,3)), this.y + this.line / random(2,3), w - this.line, h - this.line);
    ctx.globalCompositeOperation = "color-dodge";
  }
}
function random(min, max) {
  return Math.random() * (max - min) + min;
}  

board.setup = function() {
  squares = [];
  var cols = ceil(this.width/w),
      rows = ceil(this.height/h);
  for(var r=0; r<rows; r++) {
    for (var c=0; c<cols; c++) {
      squares.push(new Square(w * c, h * r, (r + c) % 4 ? true : false));
    }
  }
}
board.update = function() {
  var s = squares.length;
  while(s--) {
    squares[s].update();
  }
}
board.draw = function() {
  var s = squares.length;
  while(s--) {
    squares[s].draw();
  }
}
board.resize = function() {
  board.setup();
}

var svg = Snap("#paper");
var circ = svg.polygon("26 10.5, 28.5 5.5, 33 3, 36.5 3, 40 3.5, 43 5.5, 45 9, 47 13, 47 17.5, 46.5  23, 44 29, 41 34, 38 37, 34.5 40, 30.5 43, 27 46, 25 47.5, 22 45.5, 16.5 40.5, 13.5 37.5, 10 34, 7 30, 4.5 24.5, 3 20, 2.5 16.5, 3.5 12, 5 8.5, 8 5.5, 11 3.5, 15 3, 19 3.5, 21.5 5, 23.5 7, 24.5 9, 25 10.5")
  .attr({fill:"rgba(8, 24, 67,.8)"})
 .attr({stroke:"rgba(250,250,250,.1)"})
   .attr({strokeWidth:"1"})
  .pattern(0,0,90,90)
  .attr({patternTransform: "rotate(-15)"});
svg.rect(0,0,'100%','100%').attr({fill: circ});


var svg = Snap("#poper");
var circ = svg.polygon("26 10.5, 28.5 5.5, 33 3, 36.5 3, 40 3.5, 43 5.5, 45 9, 47 13, 47 17.5, 46.5  23, 44 29, 41 34, 38 37, 34.5 40, 30.5 43, 27 46, 25 47.5, 22 45.5, 16.5 40.5, 13.5 37.5, 10 34, 7 30, 4.5 24.5, 3 20, 2.5 16.5, 3.5 12, 5 8.5, 8 5.5, 11 3.5, 15 3, 19 3.5, 21.5 5, 23.5 7, 24.5 9, 25 10.5")
  .attr({fill:"rgba(250,0,0,.9)"})
 .attr({stroke:"rgba(250,250,250,.3)"})
   .attr({strokeWidth:"1"})
  .pattern(0,0,100,120)
  .attr({patternTransform: "rotate(20)"});
svg.rect(0,0,'100%','100%').attr({fill: circ});