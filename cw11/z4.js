const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const inp = q => new Promise(resolve => rl.question(q, a => resolve(a)));

async function main() {
    const n = Number(await inp('n = '));
    let r = Number(await inp('r = '));

    const prufer =[]
    prufer.push(r % n)
    let i = n-3
    while(i){
        r = Math.floor( r / n)
        prufer.unshift(r % n)
        i--
    }



  console.log(prufer.map(a=>a+1));

  rl.close();
}

main();