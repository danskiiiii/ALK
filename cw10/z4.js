const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const inp = q => new Promise(resolve => rl.question(q, a => resolve(a)));

async function main() {
  const n = Number(await inp('n = '));
  const k = Number(await inp('k = '));

  console.log(n, k);

  rl.close();
}

main();
