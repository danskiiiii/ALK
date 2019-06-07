const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const inp = q => new Promise(resolve => rl.question(q, a => resolve(a)));

async function main() {
  try {
    const n = Number(await inp('n = '));
    const k = Number(await inp('k = '));

    const s = new Array(n + 1).fill().map(_ => Array(k + 1).fill(0));

    for (let i = 1; i < n + 1; i++) {
      s[i][i + 1] = 0;
      s[i][0] = 0;
    }
    s[0][0] = 1;

    for (let i = 1; i < n + 1; i++) {
      for (let j = 1; j < k + 1; j++) {
        s[i][j] = s[i - 1][j - 1] - (i - 1) * s[i - 1][j];
      }
    }

    console.log(s[n][k]);
  } catch {}
  rl.close();
}

main();
