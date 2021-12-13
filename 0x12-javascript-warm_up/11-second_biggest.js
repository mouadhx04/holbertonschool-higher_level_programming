#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const args = process.argv.map(Number);
  args.slice(2, process.argv.length);
  args.sort((a, b) => a - b);
  console.log(args[args.length - 2]);
}
