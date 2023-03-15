#!/usr/bin/node

const fs = require('fs');

async function concatFiles () {
  try {
    if (process.argv.length < 3) {
      console.log('Usage1: node concat.js file1 file2 dest');
      return;
    }

    const [, , dest, file1, file2] = process.argv;

    const readStream1 = file1 && fs.createReadStream(file1);
    const readStream2 = file2 && fs.createReadStream(file2);
    const writeStream = fs.createWriteStream(dest, { flags: 'a' });

    await readStream1 && readStream1.pipe(writeStream);
    await readStream2 && readStream2.pipe(writeStream);

    writeStream.on('finish', () => {
      // console.log('Usage2: node concat.js file1 file2 dest');
      console.log(`Successfully concatenated ${file1} and ${file2} to ${dest}`);
    });
  } catch (err) {
    console.log('err =>', err);
  }
}

concatFiles();
