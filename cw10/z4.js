const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const inp = q => new Promise(resolve => rl.question(q, a => resolve(a)));

const podzial = (n, b, m, arr) => {
  if (n === 0) {
    const newArr = [...Array(arr[0])].map(_ => 0);

    arr.slice(0, m).forEach(element => {
      let i = 0;
      while (element) {
        newArr[i]++;
        i++;
        element--;
      }
    });

    console.log(JSON.stringify(newArr));
  } else {
    for (let i = 1; i < Math.min(b, n) + 1; i++) {
      arr[m] = i;
      podzial(n - i, i, m + 1, arr);
    }
  }
};

async function main() {
  const n = Number(await inp('n = '));
  const k = Number(await inp('k = '));

  podzial(n - k, k, 1, [...Array(n)].map(_ => k));

  rl.close();
}

main();
