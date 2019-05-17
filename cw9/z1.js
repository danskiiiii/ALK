const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const inp = q => new Promise(resolve => rl.question(q, a => resolve(a)));

async function main() {
  const n = Number(await inp('n = '));
  const k = Number(await inp('k = '));
  const blocks = [];

  for (let i = 0; i < k; i++) {
    let block = await inp(`blok ${i + 1} = `);
    blocks.push(block.split(' ').map(a => Number(a)));
  }

  rgf = Array(n);

  blocks.sort((a, b) => Math.min(...a) - Math.min(...b));

  blocks.forEach((bl, idx) => bl.forEach(element => (rgf[element - 1] = idx + 1)));

  console.log(JSON.stringify(rgf));

  rl.close();
}

main();
