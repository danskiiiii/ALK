// szukam najwiekszego stopniem od prawej

const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const inp = q => new Promise(resolve => rl.question(q, a => resolve(a)));

async function main() {
  const n = Number(await inp('n = '));
//   const k = Number(await inp('k = '));
  const edges = [];

  for (let i = 0; i < n; i++) {
    let edge = await inp(`krawedz ${i + 1} = `);
    edges.push(edge.split(' ').map(a => Number(a)));
  }



  console.log(JSON.stringify(edges));

  rl.close();
}

main();