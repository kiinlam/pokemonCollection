const path = require('path')
const fs = require('fs')
const makeDir = require('make-dir')
const datalist = require('../database/1.json')

function getPath(prefix, pathname) {
  pathname = path.basename(pathname)
  pathname = path.join(prefix, pathname)
  return path.resolve(pathname)
}

function copy(datalist) {
  for (let item of datalist) {
    let source = getPath('./img/pm', item.file_name)
    let dist = getPath('./images', item.file_name)
    fs.createReadStream(source).pipe(fs.createWriteStream(dist))
  }
}

makeDir('./images')
copy(datalist)