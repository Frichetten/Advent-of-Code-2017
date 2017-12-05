// Javascript implementation

var lines = require('fs').readFileSync('input2.txt', 'utf-8')
    .split('\n')
    .map(Number);

lines.pop();

var steps = 0;
var i = 0;
while(1 === 1){
    var n = lines[i];
    if (n >= 3) { lines[i] -= 1; }
    else { lines[i] += 1; }
    i += n;
    steps += 1;
    if (!(i in lines)) {
      console.log(steps);
      process.exit();
    }
}
