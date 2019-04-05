const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const inp = q => new Promise(resolve => rl.question(q, a => resolve(a)));

const func = (n, k) => {
  if (k === 0) return [];
  if (k === 1) return [...Array(n).keys()].map(x => [x + 1]);
  if (n === k) return [[...Array(n).keys()].map(x => x + 1)];
  return func(n - 1, k).concat(
    func(n - 1, k - 1)
      .reverse()
      .map(x => (typeof x === "number" ? [x, n] : [...x, n]))
  );
};

async function main() {
  const n = Number(await inp("n = "));
  const k = Number(await inp("k = "));
  console.log(func(n, k));
  rl.close();
}

main();
