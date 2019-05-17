const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const inp = q => new Promise(resolve => rl.question(q, a => resolve(a)));

async function main() {
  const n = Number(await inp('n = '));

  if (n === 1) {
    console.log([1]);
    rl.close();

    return;
  }

  let f = [...Array(n).keys()].map(x => 1);
  let fmax = [...Array(n).keys()].map(x => 2);

  let j = n - 1;
  while (j !== 0) {
    console.log(JSON.stringify(f));
    j = n - 1;
    while (f[j] >= fmax[j]) {
      j--;
    }

    f[j]++;

    for (let i = j + 1; i < n; i++) {
      f[i] = 1;

      if (f[j] === fmax[j]) {
        fmax[i] = fmax[j] + 1;
      } else {
        fmax[i] = fmax[j];
      }
    }
  }

  rl.close();
}

main();
