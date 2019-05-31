const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const inp = q => new Promise(resolve => rl.question(q, a => resolve(a)));

async function main() {
  const list = await inp('kod = ');

  const prufer = list.split(' ').map(n => Number(n));
  const d = Array(prufer.length + 2).fill(1);
  prufer.forEach(element => {
    d[element - 1]++;
  });

  prufer.push(1);

  const tree = [];

  let i = prufer.length + 1;
  while (i) {
    let l = d.length - 1;
    for (l; l >= 0; l--) {
      if (d[l] === 1) {
        tree.unshift([l + 1, prufer.shift()]);
        d[l] -= 1;
        d[tree[0][1] - 1] -= 1;
        break;
      }
    }
    i--;
  }

  console.log(tree);

  rl.close();
}

main();
