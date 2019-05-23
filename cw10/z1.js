const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const inp = q => new Promise(resolve => rl.question(q, a => resolve(a)));

async function main() {
  const n = Number(await inp('n = '));
  const k = Number(await inp('k = '));

  const arr = [...Array(n + 1)].map(a => [...Array(k + 1)]);
  arr[0][0] = 1;
  for (let i = 1; i <= n; i++) {
    arr[i][0] = 0;
  }

  for (let i = 1; i <= n; i++) {
    for (let j = 1; j < Math.min(i, k) + 1; j++) {
      if (i < 2 * j) {
        arr[i][j] = arr[i - 1][j - 1];
      } else {
        arr[i][j] = arr[i - 1][j - 1] + arr[i - j][j];
      }
    }
  }

  console.log(arr[n][k]);

  rl.close();
}

main();
