const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const inp = q => new Promise(resolve => rl.question(q, a => resolve(a)));

const binomial = (n, k) => {
  let coeff = 1;
  for (let x = n - k + 1; x <= n; x++) coeff *= x;
  for (let x = 1; x <= k; x++) coeff /= x;
  return coeff;
};

async function main() {
  const n = Number(await inp('n = '));

  B = [1];

  for (let i = 1; i < n; i++) {
    let nxt = 0;
    for (let k = 0; k < i; k++) {
      nxt += binomial(i - 1, k) * B[k];
    }
    B.push(nxt);
  }

  console.log(B[n - 1]);

  rl.close();
}

main();
