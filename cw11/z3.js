const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const inp = q => new Promise(resolve => rl.question(q, a => resolve(a)));

async function main() {
  const list = await inp('kod = ');

  const prufer = list.split(' ').map(n=> Number(n)-1)

 
const n = prufer.length +2

let rank = 0
let j =0
for (let i = prufer.length -1;i>=0;i--){
    rank+= prufer[j] * (n**i) 
    j++

}

  console.log(rank);

  rl.close();
}

main();