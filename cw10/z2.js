const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const inp = q => new Promise(resolve => rl.question(q, a => resolve(a)));

async function main() {
  const numbers = await inp('podział: ');
  const arr = numbers.split(' ').map(a => Number(a));
  const n = arr.reduce((a, b) => a + b);
  const newArr = [...Array(arr[0])].map(a => 1);

  for (let i = 2; i < n; i++) {
    for (let j = 1; j < arr[i - 1] + 1; j++) {
      newArr[j - 1]++;
    }
  }
  console.log(JSON.stringify(newArr));

  rl.close();
}

main();
