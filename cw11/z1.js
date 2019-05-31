const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const inp = q => new Promise(resolve => rl.question(q, a => resolve(a)));

async function main() {
  try {
    const n = Number(await inp('n = '));
    const edges = [];

    console.log('krawedzie w formacie: v1 spacja v2 enter');
    for (let i = 0; i < n - 1; i++) {
      let edge = await inp(`krawedz ${i + 1} = `);
      edges.push(edge.split(' ').map(a => Number(a)));
    }
    const degr = Array(n).fill(0);

    edges.forEach(e => {
      degr[e[0] - 1]++;
      degr[e[1] - 1]++;
    });

    L = [];

    while (L.length < n - 2) {
      let i = degr.length - 1;
      for (i; i >= 0; i--) {
        if (degr[i] === 1) {
          degr[i]--;
          const idx = edges.findIndex(e => e[0] === i + 1 || e[1] === i + 1);
          edges[idx][0] === i + 1
            ? (degr[edges[idx][1] - 1]--, L.push(edges[idx][1]))
            : (degr[edges[idx][0] - 1]--, L.push(edges[idx][0]));
          edges.splice(idx, 1);
          break;
        }
      }
    }
    console.log(L.join(', '));
  } catch (e) {
    console.log(e.message);
  }
  rl.close();
}

main();
