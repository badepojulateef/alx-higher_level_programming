#!/usr/bin/node

const fs = require('fs');

async function concatFiles () {
  try {
    if (process.argv.length !== 5) {
      console.log('Usage: node concat.js file1 file2 dest');
      return;
    }

    const [, , file1, file2, dest] = process.argv;

    const readStream1 = fs.createReadStream(file1);
    const readStream2 = fs.createReadStream(file2);
    const writeStream = fs.createWriteStream(dest, { flags: 'a' });

    await readStream1.pipe(writeStream);
    await readStream2.pipe(writeStream);

    writeStream.on('finish', () => {
      console.log('Usage: node concat.js file1 file2 dest');
      console.log(`Successfully concatenated ${file1} and ${file2} to ${dest}`);
    });
  } catch (err) {
    console.error(err);
  }
}

concatFiles();
