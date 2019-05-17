const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const inp = q => new Promise(resolve => rl.question(q, a => resolve(a)));

async function main() {
  const n = Number(await inp('n = '));
  let rgf = await inp('rgf = ');
  rgf = rgf.split(' ').map(a => Number(a));

  let k = 1;
  rgf.forEach(element => {
    if (element > k) {
      k = element;
    }
  });

  let blocks = [...Array(k)].map(a => []);

  for (let i = 1; i < n + 1; i++) {
    blocks[rgf[i - 1] - 1].push(i);
  }

  console.log(blocks);
  rl.close();
}

main();
