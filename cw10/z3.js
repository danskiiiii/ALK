const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const inp = q => new Promise(resolve => rl.question(q, a => resolve(a)));

const podzial = (n, b, m, arr) => {
  if (n === 0) {
    console.log(arr.slice(0, m));
  } else {
    for (let i = 1; i < Math.min(b, n) + 1; i++) {
      arr[m] = i;
      podzial(n - i, i, m + 1, arr);
    }
  }
};

async function main() {
  const n = Number(await inp('n = '));

  podzial(n, n, 0, [...Array(n)].map(a => 1));

  rl.close();
}

main();
