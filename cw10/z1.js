const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const inp = q => new Promise(resolve => rl.question(q, a => resolve(a)));

async function main() {
  const n = Number(await inp('n = '));
  const k = Number(await inp('k = '));

  const P = [...Array(n + 1)].map(a => [...Array(k + 1)]);

  P[0][0] = 1;

  for (let i = 1; i <= n; i++) {
    P[i][0] = 0;
  }

  for (let i = 1; i <= n; i++) {
    for (let j = 1; j < k + 1; j++) {
      if (i < 2 * j) {
        P[i][j] = P[i - 1][j - 1];
      } else {
        P[i][j] = P[i - 1][j - 1] + P[i - j][j];
      }
    }
  }

  console.log(P[n][k]);

  rl.close();
}

main();
